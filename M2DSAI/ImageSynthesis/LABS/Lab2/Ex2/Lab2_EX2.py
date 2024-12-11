from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    render_Scene()
    glutSwapBuffers()

def render_Scene():
    # Draw X-Y axes
    glColor3f(1, 0, 0)  # Red color for axes
    glBegin(GL_LINES)
    # X-axis
    glVertex2f(-1, 0)
    glVertex2f(1, 0)
    # Y-axis
    glVertex2f(0, -1)
    glVertex2f(0, 1)
    glEnd()

    # Coordinates for the triangle
    triangle_coords = [(0.3, 0.2), (0.7, 0.5), (0.5, 0.7)]

    # Draw the triangle in all four quadrants
    glColor3f(1, 0, 0)  # Red color for triangles
    for reflection in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
        glBegin(GL_LINE_LOOP)
        for x, y in triangle_coords:
            glVertex2f(reflection[0] * x, reflection[1] * y)
        glEnd()

# Initialize GLUT
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow("Triangle Reflections")
glutInitWindowPosition(50, 50)
glClearColor(0, 0, 0, 0)  # Black background
glutDisplayFunc(display)
glutMainLoop()
