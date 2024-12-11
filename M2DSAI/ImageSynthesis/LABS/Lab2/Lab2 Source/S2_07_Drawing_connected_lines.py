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
    glColor3f(1.0,0.0,0.0)
    glLineWidth(4.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(-0.5,0.2)
    glVertex2f(-0.2,0.6)
    glVertex2f(0.6,0.3)
    glVertex2f(-0.1,-0.6)
    glEnd()

# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)

# Create the window and give it a title
glutCreateWindow("Drawing connected Lines")

# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)

# Define callbacks
glutDisplayFunc(display)

# Begin event loop
glutMainLoop()
