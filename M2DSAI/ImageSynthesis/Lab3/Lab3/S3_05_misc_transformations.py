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
    #Draw a green triangle
    glColor3f(0,1,0)
    glRotatef(-90, 0,0,1) 		# rotate the triangle
    glScale(1.1, 1.05, 1.0) 	# scale the triangle
    glTranslatef(0.2, -0.3, 0) 	# translate the triangle
    # The last transformation (Translation) will be done first
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.2, -0.3, 0.1)
    glVertex3f(-0.3, 0.1, 0.0)
    glVertex3f(0.2, 0.1, -0.2)
    glEnd()
    
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
