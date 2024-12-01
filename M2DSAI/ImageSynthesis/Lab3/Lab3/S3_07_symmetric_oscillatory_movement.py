# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

first_time = True
move = 0.2

# Disply callback function
def display():
    # Reset background
    glClearColor(0.0, 0.0, 0.0, 1.0);
    glClear(GL_COLOR_BUFFER_BIT)
    # Render scene
    render_Scene()
    # Swap buffers
    glutSwapBuffers() 

def idle():
    global move, first_time
    if(first_time):
        glTranslatef(move,0,0) #glTranslatef(0,move,0) # w.r.t. x-axis
        first_time = False
    else:
        glTranslatef(2*move,0,0) #glTranslatef(0,2*move,0) # x-axis
    move *= -1
    time.sleep(0.2)
    glutPostRedisplay();

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
