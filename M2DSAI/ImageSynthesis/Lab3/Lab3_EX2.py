from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

# Global variables for triangle position and movement direction
x_pos = -1.0
y_pos = 0.0
speed = 0.001
direction_x = 1  # 1 for right, -1 for left
direction_y = 0  # 1 for up, -1 for down, 0 for no movement

# Display callback function
def display():
    global x_pos, y_pos
    # Clear the background
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Draw the triangle
    glLoadIdentity()
    glTranslatef(x_pos, y_pos, 0)
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.1, -0.1, 0)
    glVertex3f(0.1, -0.1, 0)
    glVertex3f(0, 0.1, 0)
    glEnd()
    
    # Swap buffers
    glutSwapBuffers()

# Idle callback function
def idle():
    global x_pos, y_pos, direction_x, direction_y, speed

    # Update the position of the triangle
    x_pos += direction_x * speed
    y_pos += direction_y * speed

    # Check for wrapping behavior
    if x_pos > 1.0:
        x_pos = -1.0
    elif x_pos < -1.0:
        x_pos = 1.0
    if y_pos > 1.0:
        y_pos = -1.0
    elif y_pos < -1.0:
        y_pos = 1.0

    # Request redisplay
    glutPostRedisplay()

# Keyboard callback function for arrow keys
def special_keys(key, x, y):
    global direction_x, direction_y

    if key == GLUT_KEY_RIGHT:
        direction_x = 1
        direction_y = 0
    elif key == GLUT_KEY_LEFT:
        direction_x = -1
        direction_y = 0
    elif key == GLUT_KEY_UP:
        direction_x = 0
        direction_y = 1
    elif key == GLUT_KEY_DOWN:
        direction_x = 0
        direction_y = -1

# Main function
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Triangle Animation")
    
    # Set the clear color
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
    # Set the display callback
    glutDisplayFunc(display)
    # Set the idle callback
    glutIdleFunc(idle)
    # Set the special keys callback
    glutSpecialFunc(special_keys)
    
    # Start the GLUT event loop
    glutMainLoop()

# Run the program
if __name__ == "__main__":
    main()
