# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
choice = 0;

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
    global choice
    choice += 1
    #Draw a green triangle
    glColor3f(0,1,0)
    if choice%3 == 1:
        glRotatef(90, 0,0,1) 		# rotate the triangle
    if choice%3 == 2:
        glScale(1.1, 1.05, 1.0) 	# scale the triangle
    if choice%3 ==0:    
        glTranslatef(0.2, -0.3, 0) 	# translate the triangle
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.3, -0.2, 0)
    glVertex3f(0.3, -0.2, 0.0)
    glVertex3f(-0.1,0.8, 0.0)
    glEnd()

# Initialize GLUT
glutInit()
# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)
# Create the window and give it a title
glutCreateWindow("Animating a triangle")
# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)
# Define display callback
glutDisplayFunc(display)

# Define idle callback

# Begin event loop
glutMainLoop()
