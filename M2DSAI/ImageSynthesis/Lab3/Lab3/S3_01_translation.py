from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def get_modelview_matrix():
    """Retrieves the current modelview matrix from OpenGL."""
    modelview_matrix = (GLfloat * 16)()
    glGetFloatv(GL_MODELVIEW_MATRIX, modelview_matrix)
    return modelview_matrix

def print_matrix(matrix):
    """Prints a 4x4 matrix in a readable format."""
    for i in range(4):
        for j in range(4):
            print(f"{matrix[i * 4 + j]:.4f}", end=" ")
        print()  # Newline after each row

def display():
    """Display callback function."""
    glClear(GL_COLOR_BUFFER_BIT)

    # Print modelview matrix before transformation
    print("Modelview Matrix (Before Transformation):")
    modelview_matrix_before = get_modelview_matrix()
    print_matrix(modelview_matrix_before)

    # Render scene
    glColor3f(0, 1, 0)
    glTranslatef(0.05, -0.1, 0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.8, -0.3, -0.1)
    glVertex3f(-0.3, 0.5, 0.0)
    glVertex3f(0.2, 0.3, 0.2)
    glEnd()

    # Print modelview matrix after transformation
    print("Modelview Matrix (After Transformation):")
    modelview_matrix_after = get_modelview_matrix()
    print_matrix(modelview_matrix_after)

    glutSwapBuffers()

def render_scene():
    """Scene render function (unused in this example)."""
    pass  # Empty implementation since display() handles rendering

# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)

# Create the window and give it a title
glutCreateWindow("Drawing 1  a triangle with translation & CTM Printing")

# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)

# Define callbacks
glutDisplayFunc(display)

# Begin event loop
glutMainLoop()