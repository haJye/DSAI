import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping, LearningRateScheduler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Data Preparation
train_gen = ImageDataGenerator(
    validation_split=0.2,
    rescale=1.0 / 255.0,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    zoom_range=0.2,
)

valid_gen = ImageDataGenerator(
    validation_split=0.2,
    rescale=1.0 / 255.0
)

train_flow = train_gen.flow_from_directory(
    directory=r"D:\Downloads\classification_dataset\Nouveau dossier",
    target_size=(256, 256),
    color_mode="rgb",
    class_mode="categorical",
    batch_size=75,
    seed=54,
    subset="training",
)

valid_flow = valid_gen.flow_from_directory(
    directory=r"D:\Downloads\classification_dataset\Nouveau dossier",
    target_size=(256, 256),
    color_mode="rgb",
    class_mode="categorical",
    batch_size=75,
    seed=54,
    subset="validation",
)

# Model Architecture
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(256, 256, 3),
    include_top=False,
    weights="imagenet"
)

x = base_model.output
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Dense(6, activation="softmax")(x)

my_model = tf.keras.Model(inputs=base_model.input, outputs=x)

# Transfer Learning
for layer in base_model.layers[:50]:
    layer.trainable = False

# Compile the Model
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
my_model.compile(optimizer=optimizer, loss="categorical_crossentropy", metrics=["accuracy"])

# Callbacks
# early_stopping = EarlyStopping(monitor='val_loss', patience=10)

def learningRate_scheduler(epoch):
    # Decrease learning rate for first 10 epochs
    if epoch < 10:
        return 0.001
    # Use lower learning rate for remaining epochs
    else:
        return 0.0001

learningRate_schedule = LearningRateScheduler(learningRate_scheduler)

# Train the Model
history = my_model.fit(
    train_flow,
    validation_data=valid_flow,
    epochs=30,
    # callbacks=[early_stopping],
    callbacks=[learningRate_schedule]
)

# Evaluate the Model
accuracy = my_model.evaluate(valid_flow)
print("Validation Accuracy:", accuracy[1])

# Confusion Matrix
y_true = valid_flow.classes
y_pred = my_model.predict(valid_flow)
y_pred_classes = tf.argmax(y_pred, axis=1)
confusion_mtx = confusion_matrix(y_true, y_pred_classes)
ConfusionMatrixDisplay(confusion_mtx, display_labels=valid_flow.class_indices).plot(cmap='viridis')
plt.title("Confusion Matrix")
plt.show()

# Training and Validation Loss Plot
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')

# Training and Validation Accuracy Plot
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.legend()
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Training and Validation Accuracy')

plt.show()
