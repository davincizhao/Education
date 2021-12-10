# Build My World

create a simulation world for robotic project.

**repos structure**
```
├── CMakeLists.txt
├── model
│   ├── building
│   │   ├── model.config
│   │   └── model.sdf
│   ├── myrobot
│   │   ├── model.config
│   │   └── model.sdf
│   └── play_car
│       ├── model.config
│       └── model.sdf
├── README.md
├── script
│   └── hello.cpp
└── world
    └── house_with_robot.world
```
## What is Gazebo?
Gazebo is a physics-based, high fidelity 3D simulator for robotics. Gazebo provides the ability to accurately simulate one or more robots in complex indoor and outdoor environments filled with static and dynamic objects, realistic lighting, and programmable interactions.

Gazebo facilitates robotic design, rapid prototyping, testing, and simulation of real-life scenarios. While Gazebo is platform agnostic and runs on Windows, Mac, and Linux, it is mostly used in conjunction with the Robotics Operating System (ROS) running on Linux systems.
## Gazebo Features
Gazebo has eight features that you can take advantage of:

- **Dynamics Simulation:** Model a robot's dynamics with a high-performance physics engine.
- **Advanced 3D Graphics:** Render your environment with high-fidelity graphics, including lighting, shadows, and textures.
- **Sensors:** Add sensors to your robot, generate data, and simulate noise.
- **Plugins:** Write a plugin to interact with your world, robot, or sensor.
- **Model Database:** Download a robot or environment from Gazebo library or build your own through their engine.
- **Socket-Based Communication:** Interact with Gazebo running on a remote server through socket-based communication.
- **Cloud Simulation:** Run Gazebo on a server and interact with it through a browser.
- **Command Line Tools:** Control your simulated environment through the command line tools.

## Gazebo Components
There are six components involved in running an instance of a Gazebo simulation:
- Gazebo Server
- Gazebo Client
- World Files
- Model Files
- Environment Variables
- Plugins

### 1- Gazebo Server
The first main component involved in running an instance of a Gazebo simulation is the Gazebo Server or also known by gzserver.
### 2- Gazebo Client
The second main component involved in running an instance of a Gazebo simulation is the Gazebo Client or also known by gzclient.
### 3- World Files
A world file in Gazebo contains all the elements in the simulated environment. These elements are your robot model, its environment, lighting, sensors, and other objects. 
### 4- Model Files
For simplification, you must create a separate SDF file of your robot with exactly the same format as your world file. This model file should only represent a single model (ex: a robot) and can be imported by your world file. The reason why you need to keep your model in a separate file is to use it in other projects. 
### 5- Environment Variables
There are many environment variables that Gazebo uses, primarily to locate files (world, model, …) and set up communications between gzserver and gzclient. 
### 6- Plugins
To interact with a world, model, or sensor in Gazebo, you can write plugins. These plugins can be either loaded from the command line or added to your SDF world file. 

## Steps to build simulation world
- Build a single floor wall structure using the **Building Editor** tool in Gazebo. 
- Model any object of  choice using the **Model Editor** tool in Gazebo. The model links should be connected with joints.
- Import structure and two instances of  model inside an empty Gazebo World.
- Import at least one model from the **Gazebo online library** and implement it in  existing **Gazebo world**.
- Write a C++ **World Plugin** to interact with  world. 
- Display “Welcome to ’s World!” message as soon as launch the Gazebo world file.


