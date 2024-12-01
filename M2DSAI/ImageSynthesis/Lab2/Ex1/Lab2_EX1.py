from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# Global variables
center = (0.0, 0.0)  # Center of the circle (x, y)
num_points = 64      # Number of points in the circle

# Display callback function
def display():
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT)

    # Render the circle
    render_scene()

    # Swap buffers
    glutSwapBuffers()

# Scene render function
def render_scene():
    # Draw circle using points
    for i in range(num_points):  # Loop through the number of points
        angle = 2 * math.pi * i / num_points
        x = center[0] + 0.5 * math.cos(angle)  # Calculate x coordinate
        y = center[1] + 0.5 * math.sin(angle)  # Calculate y coordinate

        # Set progressively increasing point size
        point_size = 1.0 + 9.0 * (i / (num_points - 1))
        glPointSize(point_size)

        # Set a random color for each point
        glColor3f(random.random(), random.random(), random.random())

        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)

# Create the window and give it a title
glutCreateWindow("Circle with Points of Random Colors and Sizes")

# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)

# Define the callbacks
glutDisplayFunc(display)

# Begin the event loop
glutMainLoop()
