# Translating separately the first triangle among two
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
    # Perform a transformation (e.g. a translation)
    glTranslated(0.0,-0.1,0)

    # Push the current matrix stack
    glPushMatrix()

    # Draw first triangle in Red
    glColor3f(1.0,0.0,0.0);
    glBegin(GL_TRIANGLES);
    glVertex3f(-0.3,-0.1,-0.8);
    glVertex3f(0.3,-0.1,-1);
    glVertex3f(0,0.3,-0.9);
    glEnd();

    glLoadIdentity()

    # Draw second triangle in Yellow
    glColor3f(1.0,1.0,0.0);
    glBegin(GL_TRIANGLES);
    glVertex3f(-0.3,0.2,0.0);
    glVertex3f(-0.7,0.5,0.0);
    glVertex3f(-0.5,0.7,0.0);
    glEnd();  

    # Pop the current matrix stack
    glPopMatrix()
	   
# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)

# Create the window and give it a title
glutCreateWindow("Drawing a triangle with rotation")

# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)

# Define callbacks
glutDisplayFunc(display)

# Begin event loop
glutMainLoop()
