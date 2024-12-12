# Solar System Simulation

![](https://github.com/haJye/DSAI/blob/main/M2DSAI/ImageSynthesis/Project/Gif.gif)

## How to Run This Project??
This project requires several libraries to run properly. Follow the steps below to install and set up the required dependencies.

### Step 1: Install Required Libraries

Before running the project, ensure that you have the following libraries installed:

- **Pygame**: A set of Python modules designed for writing video games, which is used here for window management and input handling.
- **PyOpenGL**: A Python binding for OpenGL, used for rendering 3D graphics.

You can install these libraries using the following commands in your terminal:

```bash
pip install pygame == 2.6.1
pip install PyOpenGL = 3.1.7
```

Python version 3.11.10

## Introduction
This report provides an overview of a solar system simulation built using **Pygame** and **OpenGL**. The simulation showcases various celestial objects, their orbital mechanics, and visual effects, implemented using 3D rendering techniques.

## Features of the Simulation
### 1. **Celestial Bodies**
- **Planets**: Simulates all eight planets with realistic sizes, textures, orbital radii, and tilts.
- **Satellites**: Implements moons for Earth (e.g., two artificial satellites and the Moon) and prominent satellites for Jupiter (e.g., Io, Europa, Ganymede, Callisto).
- **Asteroids**: Models a small asteroid belt with random movement and elliptical orbits.
- **Comets**: Includes comets with elliptical orbits, such as Halley and Encke.

### 2. **Visual Effects**
- **Lighting**: Dynamic lighting simulates the Sun as a light source with diffuse and specular components.
- **Textures**: High-resolution textures are applied to celestial objects, including planets, satellites, and the Sun.
- **Starry Background**: A rotating textured sphere simulates a starry sky, providing a visually rich environment.
- **Saturn's Rings**: Rendered with textured quad strips, accurately depicting their appearance.

### 3. **Interactive Features**
- **Camera Controls**: The user can navigate the simulation using keyboard inputs.
  - **W/A/S/D**: Move the camera forward/backward and sideways.
  - **Arrow Keys**: Adjust vertical camera position.
  - **Plus/Minus Keys**: Zoom in and out.
  - **Preset Views**: Reset or move to preset camera distances (e.g., `R`, `T`, `Y`, `U`).
- **Time Control**: Adjust the simulation's speed using keys:
  - `0`: Pause the simulation.
  - `1-4`: Different time scales.

## Technical Implementation
### 1. **Programming Environment**
- **Python Libraries**:
  - **Pygame**: Handles windowing and user input.
  - **OpenGL**: Manages 3D rendering and lighting.
  - **Math**: Provides trigonometric functions for orbit calculations.

### 2. **3D Rendering**
- **OpenGL Primitives**:
  - `gluSphere`: Used for rendering planets and celestial bodies.
  - `glBegin` and `glEnd`: Used to draw orbits and other simple shapes.
- **Lighting Setup**:
  - Global ambient light.
  - Positional light source for the Sun.
- **Texture Mapping**:
  - `glGenTextures` and `glBindTexture`: Load and bind textures to OpenGL objects.

### 3. **Orbital Mechanics**
- Planets and satellites have attributes for:
  - **Orbit Radius**: Determines distance from the Sun or planet.
  - **Speed**: Governs angular velocity.
  - **Angle**: Tracks the current position in orbit.
  - **Tilt**: Adds realistic axial tilt.

### 4. **Special Features**
- **Elliptical Orbits**:
  - Comets are rendered with semi-major and semi-minor axes for their paths.
- **Dynamic Asteroids**:
  - Incorporates randomness in movement and positions to simulate real-world asteroid dynamics.

## Challenges Faced
1. **Texture Loading**: Ensuring textures mapped accurately without distortion.
2. **Lighting Artifacts**: Balancing brightness and maintaining realism for the Sun and planetary surfaces.
3. **Performance Optimization**:
   - Managing frame rates for smooth rendering.
   - Efficient memory usage for high-resolution textures.

## Future Enhancements
1. **Advanced Physics**:
   - Implement gravitational interactions between celestial bodies.
   - Simulate orbital decay and resonance.
2. **More Celestial Features**:
   - Add dwarf planets like Pluto.
   - Enhance asteroid belt with more particles.
3. **Real-Time Shadows**: 
    - Incorporate shadow mapping to enhance depth perception.
4. **User Interface**:
   - On-screen controls for camera and time adjustments.
   - Informational overlays about celestial objects.
5. **Aircraft and other ships**

## Conclusion
The solar system simulation effectively demonstrates the application of Pygame and OpenGL to create an interactive, visually engaging representation of celestial mechanics. With further enhancements, it can serve as an educational tool for astronomy enthusiasts.

