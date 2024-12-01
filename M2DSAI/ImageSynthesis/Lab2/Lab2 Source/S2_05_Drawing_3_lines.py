# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Disply callback function
def display():
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT)

    # Render scene
    render_Scene()

    # Flush buffer
    glFlush()

    # Swap buffers
    glutSwapBuffers()  


# Scene render function
def render_Scene():
    # Draw the first line (in red)
    glColor3f(1.0,0.0,0.0)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex2f(-0.8, -0.4)
    glVertex2f(0.2, -0.2)
    glEnd()
    
    # Draw the second line (in green)
    glColor3f(0.0,1.0,0.0)
    glLineWidth(4.0)
    glBegin(GL_LINES)
    glVertex2f(-0.7, 0.6)
    glVertex2f(0.2, 0.4)
    glEnd()

    # Draw the third  line (in blue)
    glColor3f(0.0,0.0,1.0)
    glLineWidth(8.0)
    glBegin(GL_LINES)
    glVertex2f(0.8, -0.6)
    glVertex2f(0.2, 0.2)
    glEnd()

# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)

# Create the window and give it a title
glutCreateWindow("Drawing Lines")

# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)

# Define callbacks
glutDisplayFunc(display)

# Begin event loop
glutMainLoop()
