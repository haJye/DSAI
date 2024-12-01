# Drawing several triangles using the primitive GL_TRIANGLES
# all the vertices of each triangle have the same color

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
    # Draw the first triangle (in red)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.3,-0.1,-0.8)
    glVertex3f(0.3,-0.1,-1)
    glVertex3f(0,0.3,-0.9)    
    # Draw the second triangle (in yellow)
    glColor3f(1.0,1.0,0.0)
    glVertex3f(-0.3,0.2,0.0)
    glVertex3f(-0.7,0.5,0.0)
    glVertex3f(-0.5,0.7,0.0)
    # Draw the third triangle (in cyan)
    glColor3f(0.0,1.0,1.0)
    glVertex3f(0.3,-0.2,0.0)
    glVertex3f(0.7,-0.7,0.0)
    glVertex3f(0.6,0.3,0.0)
    glEnd()

# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)

# Create the window and give it a title
glutCreateWindow("Drawing Triangles")

# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)

# Define callbacks
glutDisplayFunc(display)

# Begin event loop
glutMainLoop()
