from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Global variables to track rotation angles
rotate_x = 0
rotate_y = 0

# Display callback function
def display():
    global rotate_x, rotate_y

    # Clear screen and Z-buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Reset transformations
    glLoadIdentity()

    # Apply rotations
    glRotatef(rotate_x, 1.0, 0.0, 0.0)  # Rotate about x-axis
    glRotatef(rotate_y, 0.0, 1.0, 0.0)  # Rotate about y-axis

    # Render the cube
    render_Scene()

    # Swap buffers
    glutSwapBuffers()

# Scene render function
def render_Scene():
    # Multi-colored side - FRONT
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.5, -0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.5, 0.5, -0.5)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.5, 0.5, -0.5)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glEnd()

    # White side - BACK
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glEnd()

    # Purple side - RIGHT
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glEnd()

    # Green side - LEFT
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glEnd()

    # Blue side - TOP
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glEnd()

    # Red side - BOTTOM
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glEnd()

# Special key callback function
def special_keys(key, x, y):
    global rotate_x, rotate_y

    if key == GLUT_KEY_UP:      # Rotate up
        rotate_x += 5
    elif key == GLUT_KEY_DOWN:  # Rotate down
        rotate_x -= 5
    elif key == GLUT_KEY_LEFT:  # Rotate left
        rotate_y -= 5
    elif key == GLUT_KEY_RIGHT: # Rotate right
        rotate_y += 5

    # Redisplay after rotation
    glutPostRedisplay()

# Reshape callback function
def reshape(width, height):
    # Set a new projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(40, width / height, 1, 10)
    glTranslatef(0.0, 0.0, -5)

    # Set the viewport to cover the new window
    glViewport(0, 0, width, height)

# Main function
def main():
    # Initialize GLUT
    glutInit()

    # Set display mode
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    # Set the window size
    glutInitWindowSize(500, 500)

    # Create the window
    glutCreateWindow("3D Rotating Cube")

    # Enable depth test
    glEnable(GL_DEPTH_TEST)

    # Set callback functions
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutSpecialFunc(special_keys)

    # Start the main loop
    glutMainLoop()

if __name__ == "__main__":
    main()
