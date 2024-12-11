#Importing necessary libraries
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random

# Initialize Pygame and OpenGL
pygame.init()
# Define desired viewport size
WINDOW_WIDTH = 1920  # Fixed viewport width
WINDOW_HEIGHT = 1080  # Fixed viewport height


# Load and play background music
pygame.mixer.music.load('main.mp3')  # Replace with your music file path
pygame.mixer.music.play(-1, 0.0)  # Loop the music (-1 means infinite loop)

# Start the program in fullscreen
screen = pygame.display.set_mode((0, 0), FULLSCREEN | DOUBLEBUF | OPENGL)
pygame.display.set_caption("Solar System Simulation")

# OpenGL setup
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_TEXTURE_2D)

# Perspective Projection
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(60, WINDOW_WIDTH / WINDOW_HEIGHT, 0.1, 50000)
glMatrixMode(GL_MODELVIEW)

# Global ambient light
glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1.0])  # Low ambient light for the entire scene

# Sun's light (GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 0.0, 0.0, 1.0])  # Light at the Sun's position
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])  # Diffuse light (white)
glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])  # Specular light (white)

# Enable lighting and materials
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_COLOR_MATERIAL)

# Material settings for planets
glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])  # Specular reflection
glMaterialf(GL_FRONT, GL_SHININESS, 50.0)  # Shininess factor


# Function to load a texture from an image file
def load_texture(filename):
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    try:
        image = pygame.image.load(filename)
        image_data = pygame.image.tostring(image, "RGB", True)
        width, height = image.get_rect().size
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
        glGenerateMipmap(GL_TEXTURE_2D)
    except Exception as e:
        print(f"Failed to load texture {filename}: {e}")
        return None
    return texture

# Function to draw a textured sphere
def draw_sphere(radius, texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    quad = gluNewQuadric()
    gluQuadricTexture(quad, GL_TRUE)
    gluSphere(quad, radius, 50, 50)


# # Function to draw an atmosphere (unused in current code) 
# def draw_atmosphere(radius, color):
#     glColor4f(*color, 0.2)  # RGBA with transparency
#     glEnable(GL_BLEND)
#     glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
#     draw_sphere(radius, None)
#     glDisable(GL_BLEND)


# # Function to draw a textured cube (unused in current code)
# def draw_textured_cube(size, texture):
#     glBindTexture(GL_TEXTURE_2D, texture)
#     vertices = [
#         [-size, -size, -size],
#         [size, -size, -size],
#         [size, size, -size],
#         [-size, size, -size],
#         [-size, -size, size],
#         [size, -size, size],
#         [size, size, size],
#         [-size, size, size]
#     ]
#     faces = [
#         [0, 1, 2, 3], [3, 2, 6, 7], [7, 6, 5, 4], [4, 5, 1, 0], [1, 5, 6, 2], [4, 0, 3, 7]
#     ]
#     glBegin(GL_QUADS)
#     for face in faces:
#         for vertex in face:
#             glTexCoord2f((vertices[vertex][0] + size) / (2 * size), (vertices[vertex][1] + size) / (2 * size))
#             glVertex3fv(vertices[vertex])
#     glEnd()

# Camera and time scale variables
camera_position = [0, 0, 15]
camera_speed = 1.5
time_scale = 1.0

# Load textures for celestial objects
textures = {
    "earth": load_texture("earth.jpg"),
    "moon": load_texture("moon.jpg"),
    "mars": load_texture("mars.jpg"),
    "jupiter": load_texture("jupiter.jpg"),
    "saturn": load_texture("saturn.jpg"),
    "uranus": load_texture("uranus.jpg"),
    "neptune": load_texture("neptune.jpg"),
    "mercury": load_texture("mercury.jpg"),
    "venus": load_texture("venus.jpg"),
    "stars": load_texture("stars.jpg"),
    "saturn_ring": load_texture("saturn_ring.png"),
    "sun": load_texture("sun.jpg"),
    "asteroid": load_texture("asteroids.jpg"),
}

# Define planets with their properties
planets = [
    {"name": "Mercury", "size": 0.3, "orbit_radius": 4, "texture": textures["mercury"], "angle": 0, "speed": 0.04, "tilt": 0.0, "vertical_amplitude": 1.0},
    {"name": "Venus", "size": 0.7, "orbit_radius": 6, "texture": textures["venus"], "angle": 0, "speed": 0.03, "tilt": 177.4, "vertical_amplitude": 1.0},
    {"name": "Earth", "size": 1, "orbit_radius": 8, "texture": textures["earth"], "angle": 0, "speed": 0.02, "tilt": 23.5, "vertical_amplitude": 1.5},
    {"name": "Mars", "size": 0.8, "orbit_radius": 10, "texture": textures["mars"], "angle": 0, "speed": 0.015, "tilt": 25.2, "vertical_amplitude": 1.2},
    {"name": "Jupiter", "size": 2.5, "orbit_radius": 14, "texture": textures["jupiter"], "angle": 0, "speed": 0.008, "tilt": 3.1, "vertical_amplitude": 1.0},
    {"name": "Saturn", "size": 2, "orbit_radius": 18, "texture": textures["saturn"], "angle": 0, "speed": 0.006, "tilt": 26.7, "vertical_amplitude": 1.0},
    {"name": "Uranus", "size": 1.7, "orbit_radius": 22, "texture": textures["uranus"], "angle": 0, "speed": 0.004, "tilt": 97.8, "vertical_amplitude": 1.0},
    {"name": "Neptune", "size": 1.6, "orbit_radius": 26, "texture": textures["neptune"], "angle": 0, "speed": 0.003, "tilt": 28.3, "vertical_amplitude": 1.0},
]
# Adding satellites to some planets
planets[2]["satellites"] = [  # Earth satellites
    {"name": "Satellite 1", "size": 0.1, "orbit_radius": 1.8, "speed": 0.07, "angle": 0, "texture": textures["moon"]},
    {"name": "Satellite 2", "size": 0.1, "orbit_radius": 2.1, "speed": 0.05, "angle": 0, "texture": textures["moon"]},
]

planets[4]["satellites"] = [  # Jupiter satellites
    {"name": "Io", "size": 0.2, "orbit_radius": 3, "speed": 0.04, "angle": 0, "texture": textures["moon"]},
    {"name": "Europa", "size": 0.2, "orbit_radius": 3.5, "speed": 0.03, "angle": 0, "texture": textures["moon"]},
    {"name": "Ganymede", "size": 0.25, "orbit_radius": 4, "speed": 0.02, "angle": 0, "texture": textures["moon"]},
    {"name": "Callisto", "size": 0.2, "orbit_radius": 4.5, "speed": 0.01, "angle": 0, "texture": textures["moon"]},
]

# Define Earth's moon properties
moon = {
    "name": "Moon",
    "size": 0.2,
    "orbit_radius": 1.5,
    "texture": textures["moon"],
    "angle": 0,
    "speed": 0.05,
}

# Define asteroid belt properties
asteroids = [
    {"size": 0.1, "orbit_radius": random.uniform(9, 11), "angle": random.uniform(0, 2 * math.pi), "speed": random.uniform(0.035, 0.075)}
    for _ in range(5)
]



# Define comets with elliptical orbits
comets = [
    {
        "name": "Halley",
        "size": 0.3,
        "semi_major_axis": 30,
        "semi_minor_axis": 20,
        "speed": 0.002,
        "angle": random.uniform(0, 2 * math.pi),
        "texture": textures["asteroid"],
    },
    {
        "name": "Encke",
        "size": 0.2,
        "semi_major_axis": 40,
        "semi_minor_axis": 25,
        "speed": 0.001,
        "angle": random.uniform(0, 2 * math.pi),
        "texture": textures["asteroid"],
    },
]
# Draw Saturn's rings
def draw_rings(inner_radius, outer_radius, texture, num_segments=100):
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUAD_STRIP)
    for i in range(num_segments + 1):
        angle = 2 * math.pi * i / num_segments
        x_inner = math.cos(angle) * inner_radius
        z_inner = math.sin(angle) * inner_radius
        x_outer = math.cos(angle) * outer_radius
        z_outer = math.sin(angle) * outer_radius
        glTexCoord2f(0, i / num_segments)
        glVertex3f(x_inner, 0, z_inner)
        glTexCoord2f(1, i / num_segments)
        glVertex3f(x_outer, 0, z_outer)
    glEnd()




# Main simulation loop statements
fullscreen = False  # Tracks whether fullscreen is active
running = True
sun_rotation_angle = 0.01
background_rotation_angle = 0.005

# Main simulation loop and event handling
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_w:
                camera_position[2] -= camera_speed
            elif event.key == K_s:
                camera_position[2] += camera_speed
            elif event.key == K_a:
                camera_position[0] -= camera_speed
            elif event.key == K_d:
                camera_position[0] += camera_speed
            elif event.key == K_UP:
                camera_position[1] += camera_speed
            elif event.key == K_DOWN:
                camera_position[1] -= camera_speed
            elif event.key == K_PLUS:
                camera_position[2] -= camera_speed
            elif event.key == K_MINUS:
                camera_position[2] += camera_speed
            elif event.key == K_0:
                time_scale = 0.0
            elif event.key == K_1:
                time_scale = 0.01
            elif event.key == K_2:
                time_scale = 1.0
            elif event.key == K_3:
                time_scale = 5.0
            elif event.key == K_4:
                time_scale = 10.0
            elif event.key == K_r:
                camera_position = [0, 0, 10]
            elif event.key == K_t:
                camera_position = [0, 0, 15]
            elif event.key == K_y:
                camera_position = [0, 0, 20]
            elif event.key == K_u:
                camera_position = [0, 0, 25]

    # Clear buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Set camera position
    gluLookAt(camera_position[0], camera_position[1], camera_position[2], 0, 0, 0, 0, 1, 0)
    camera_position[2] = min(camera_position[2], 30000)


    # Draw starry background
    glPushMatrix()
    glDisable(GL_LIGHTING)
    background_rotation_angle += 0.005 * time_scale
    glRotatef(background_rotation_angle * 50, 0, 1, 0)
    draw_sphere(50, textures["stars"])
    glEnable(GL_LIGHTING)
    glPopMatrix()

    # Set up the sun as a dynamic light source
    sun_position = [0.0, 0.0, 0.0, 1.0]  # Sun's position (w = 1.0 for positional light)
    glLightfv(GL_LIGHT0, GL_POSITION, sun_position)  # Position the light
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])  # Diffuse light color
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])  # Specular light color

    # Render the Sun
    sun_rotation_angle += 0.01 * time_scale
    glPushMatrix()
    glDisable(GL_LIGHTING)  # Disable lighting for the Sun
    glColor3f(1.0, 1.0, 1.0)  # Neutral color since texture will provide brightness
    glRotatef(sun_rotation_angle * 50, 0, 1, 0)
    draw_sphere(3, textures["sun"])  # Sun texture simulates its glowing surface
    glEnable(GL_LIGHTING)  # Re-enable lighting for the rest of the scene
    glPopMatrix()


    # # Draw orbit lines for each planet
    # # glDisable(GL_LIGHTING)  # Disable lighting for orbit lines
    # glLineWidth(1.0)  # Set orbit line thickness
    # # glColor3f(1.0, 1.0, 0.0)  # Set orbit line color to yellow
    # for planet in planets:
    #     glBegin(GL_LINE_LOOP)  # Use LINE_LOOP for a closed circle
    #     for angle in range(0, 360, 2):  # Draw a circle in 2-degree steps
    #         rad = math.radians(angle)
    #         x = math.cos(rad) * planet["orbit_radius"]
    #         z = math.sin(rad) * planet["orbit_radius"]
    #         glVertex3f(x, 0, z)
    #     glEnd()
    # # glEnable(GL_LIGHTING)  # Re-enable lighting

    # Render comets
    for comet in comets:
        glPushMatrix()
        comet["angle"] += comet["speed"] * time_scale
        x = comet["semi_major_axis"] * math.cos(comet["angle"])
        z = comet["semi_minor_axis"] * math.sin(comet["angle"])
        glTranslatef(x, 0, z)
        draw_sphere(comet["size"], comet["texture"])
        glPopMatrix()


    # Render each planet
    for planet in planets:
        glBegin(GL_LINE_LOOP)  # Use LINE_LOOP for a closed circle
        for angle in range(0, 360, 2):  # Draw a circle in 2-degree steps
            rad = math.radians(angle)
            x = math.cos(rad) * planet["orbit_radius"]
            z = math.sin(rad) * planet["orbit_radius"]
            glVertex3f(x, 0, z)
        glEnd()
        glPushMatrix()  # Push the matrix for each planet
        planet["angle"] += planet["speed"] * time_scale
        x = math.cos(planet["angle"]) * planet["orbit_radius"]
        z = math.sin(planet["angle"]) * planet["orbit_radius"]
        y = planet["vertical_amplitude"] * math.sin(planet["angle"] * 0.5)

        glTranslatef(x, y, z)  # Position the planet in its orbit
        glRotatef(planet["tilt"], 1, 0, 0)  # Tilt the planet
        glRotatef(planet["angle"] * 10, 0, 1, 0)  # Simulate rotation
        draw_sphere(planet["size"], planet["texture"])  # Draw the planet

        # Draw satellites, if the planet has any
        if "satellites" in planet:
            for satellite in planet["satellites"]:
                glPushMatrix()  # Push the matrix for the satellite
                satellite["angle"] += satellite["speed"] * time_scale
                sat_x = math.cos(satellite["angle"]) * satellite["orbit_radius"]
                sat_z = math.sin(satellite["angle"]) * satellite["orbit_radius"]
                glTranslatef(sat_x, 0, sat_z)  # Position the satellite relative to the planet
                draw_sphere(satellite["size"], satellite["texture"])  # Draw the satellite
                glPopMatrix()  # Pop the matrix for the satellite

        # If it's Earth, also draw the Moon
        if planet["name"] == "Earth":
            glPushMatrix()  # Push the matrix for the Moon
            moon["angle"] += moon["speed"] * time_scale
            moon_x = math.cos(moon["angle"]) * moon["orbit_radius"]
            moon_z = math.sin(moon["angle"]) * moon["orbit_radius"]
            glTranslatef(moon_x, 0, moon_z)  # Position the Moon relative to Earth
            draw_sphere(moon["size"], moon["texture"])  # Draw the Moon
            glPopMatrix()  # Pop the matrix for the Moon

        if planet["name"] == "Saturn":
            glPushMatrix()  # Push matrix for rings
            glRotatef(90, 1, 0, 0)  # Rotate rings to be horizontal
            draw_rings(2.5, 3.5, textures["saturn_ring"])  # Draw the rings
            glPopMatrix()  # Pop matrix for rings


        glPopMatrix()  # Pop the matrix for the planet

    # Asteroids with random and dynamic movement
    for asteroid in asteroids:
        glPushMatrix()
        # Update angle with some random variation
        asteroid["angle"] += (asteroid["speed"] + random.uniform(-0.002, 0.002)) * time_scale
        
        # Compute x, y, z positions with wobble or randomness
        asteroid_x = math.cos(asteroid["angle"]) * asteroid["orbit_radius"] + random.uniform(-0.1, 0.1)
        asteroid_y = math.sin(asteroid["angle"] * 0.5) * 0.5  # Oscillation in vertical plane
        asteroid_z = math.sin(asteroid["angle"]) * asteroid["orbit_radius"] + random.uniform(-0.1, 0.1)
        
        # Translate and draw the asteroid
        glTranslatef(asteroid_x, asteroid_y, asteroid_z)
        draw_sphere(asteroid["size"], textures["asteroid"])
        glPopMatrix()



        # Update display and wait for the next frame
        pygame.display.flip()
        pygame.time.wait(10)

# Quit Pygame
pygame.quit()
