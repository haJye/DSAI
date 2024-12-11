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
    glLineWidth(4.0)
    glBegin(GL_LINE_LOOP)

    glColor3f(1.0,0.0,0.0) # First point
    glVertex2f(-0.5,0.2);
    glColor3f(0.0,1.0,0.0) # Second point
    glVertex2f(-0.2,0.6);
    glColor3f(0.0,1.0,0.0) # Third point
    glVertex2f(0.6,0.3);
    glColor3f(1.0,0.0,0.5) # Fourth point
    glVertex2f(-0.1,-0.6)

    glEnd();

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
