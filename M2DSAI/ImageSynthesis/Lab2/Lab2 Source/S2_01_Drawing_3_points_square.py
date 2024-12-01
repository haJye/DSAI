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

    # Swap buffers
    glutSwapBuffers()  

# Scene render function
def render_Scene():

    # Draw the first point (red)
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(-0.4, 0.5)
    glEnd()  
    
    # Draw the second point (green)
    glColor3f(0.0,1.0,0.0)
    glPointSize(20.0)   
    glBegin(GL_POINTS)
    glVertex2f(-0.2, -0.4)
    glEnd()

    # Draw the third point (blue)
    glColor3f(0.0,0.0,1.0)
    glPointSize(30.0)
    glBegin(GL_POINTS)
    glVertex2f(0.5, 0.2)
    glEnd()

# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)

# Create the window and give it a title
glutCreateWindow("Drawing 3 squared-points")

# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)

# Define callbacks
glutDisplayFunc(display)

# Begin event loop
glutMainLoop()
