# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
move = 0.3

# Disply callback function
def display():
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT)
    # Render scene
    render_Scene()
    # Swap buffers
    glutSwapBuffers() 

def idle():
    global move
    glTranslatef(move,0,0)
    move *= -1
    time.sleep(0.2)
    glutPostRedisplay()

# Scene render function
def render_Scene():
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.3,-0.1,0.1)
    glVertex3f(0.3,-0.1,0.0)
    glVertex3f(0,0.3,-0.2)
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
glutIdleFunc(idle)

# Begin event loop
glutMainLoop()
