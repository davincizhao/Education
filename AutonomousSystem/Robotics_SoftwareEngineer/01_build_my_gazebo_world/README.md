# Build My World

create a simulation world for all projects

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
## Steps to build
- Build a single floor wall structure using the **Building Editor** tool in Gazebo. 
- Model any object of  choice using the **Model Editor** tool in Gazebo. The model links should be connected with joints.
- Import structure and two instances of  model inside an empty Gazebo World.
- Import at least one model from the **Gazebo online library** and implement it in  existing **Gazebo world**.
- Write a C++ **World Plugin** to interact with  world. 
- Display “Welcome to ’s World!” message as soon as launch the Gazebo world file.


