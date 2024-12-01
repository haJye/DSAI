from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Number of sides for the polygon (e.g., 8 for an octagon)
n = 9  # Change this to any desired number of sides

# Display callback function
def display():
    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw the polygon
    draw_polygon()

    # Swap buffers
    glutSwapBuffers()

# Function to draw the polygon using GL_TRIANGLE_FAN
def draw_polygon():
    radius = 0.8  # Radius of the polygon
    angle_step = 2 * math.pi / n  # Angle between vertices

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)  # Wireframe mode
    glColor3f(1.0, 0, 0)  # Set polygon color (red)

    glBegin(GL_TRIANGLE_FAN)

    # Center vertex of the polygon
    glVertex2f(0.0, 0.0)

    # Vertices of the polygon
    for i in range(n + 1):  # Loop to include the first and last vertex
        angle = i * angle_step
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)

    glEnd()

# Initialize GLUT
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(500,250)
glutCreateWindow("Regular Polygon with GL_TRIANGLE_FAN")
glutDisplayFunc(display)
glutMainLoop()
