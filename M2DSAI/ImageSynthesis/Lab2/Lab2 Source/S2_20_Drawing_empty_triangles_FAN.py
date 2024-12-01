# Using the directive GL_TRIANGLE_FAN

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
    glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0,0.0,0.0)
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(-0.8,-0.3,0.0)
    glVertex3f(-0.4,0.5,0.0)
    glVertex3f(0.2,0.8,0.0)
    glVertex3f(0.6,-0.3,0.0)
    glVertex3f(0.2,-0.7,0.0)
    glEnd()
    
# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)

# Create the window and give it a title
glutCreateWindow("Drawing Triangles with GL_TRIANGLE_FAN")

# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)

# Define callbacks
glutDisplayFunc(display)

# Begin event loop
glutMainLoop()
