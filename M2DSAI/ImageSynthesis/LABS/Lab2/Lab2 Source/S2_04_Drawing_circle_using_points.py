# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

###############################################
import math

# Disply callback function
def display():
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT)

    # Render scene
    render_Scene()

    # Swap buffers
    glutSwapBuffers() 

# Scene render function
def render_Scene():
    # Set current color to red
    glColor3f(1.0,0.0,0.0)
    glPointSize(5.0)   
    ################################################################
    for i in range(64):	# We draw 64 points
        angle = 2*math.pi * i / 64
        x = 0.5 * math.cos(angle)
        y = 0.5 * math.sin(angle)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)

# Create the window and give it a title
glutCreateWindow("Drawing a circle using points")

# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)

# Define callbacks
glutDisplayFunc(display)

# Begin event loop
glutMainLoop()
