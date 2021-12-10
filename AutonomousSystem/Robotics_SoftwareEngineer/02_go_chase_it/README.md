# Go Chase It


## Repo structure
```
├── ball_chaser
│   ├── CMakeLists.txt
│   ├── launch
│   │   └── ball_chaser.launch
│   ├── package.xml
│   ├── src
│   │   ├── drive_bot.cpp
│   │   └── process_image.cpp
│   └── srv
│       └── DriveToTarget.srv
├── CMakeLists.txt -> /opt/ros/kinetic/share/catkin/cmake/toplevel.cmake
├── my_robot
│   ├── CMakeLists.txt
│   ├── launch
│   │   ├── robot_description.launch
│   │   └── world.launch
│   ├── meshes
│   │   └── hokuyo.dae
│   ├── package.xml
│   ├── urdf
│   │   ├── my_robot.gazebo
│   │   ├── my_robot.xacro
│   │   └── RViz_conf.rviz
│   └── worlds
│       ├── empty.world
│       └── house_with_robot.world
└── README.md

```
## What is ROS?
The **Robot Operating System (ROS)** is a set of software libraries and tools that help you build robot applications. From drivers to state-of-the-art algorithms, and with powerful developer tools, ROS has what you need for your next robotics project. And it's all open source.

## Quick overview of ROS 2 Concepts
- Graph Concepts
- Nodes
- Client Libraries
- Discovery
- Related Content

**ROS 2** is a middleware based on an anonymous publish/subscribe mechanism that allows for message passing between different ROS processes.

At the heart of any ROS 2 system is the ROS graph. The ROS graph refers to the network of nodes in a ROS system and the connections between them by which they communicate.

### Graph Concepts
- Nodes: A node is an entity that uses ROS to communicate with other nodes.
- Messages: ROS data type used when subscribing or publishing to a topic.
- Topics: Nodes can publish messages to a topic as well as subscribe to a topic to receive messages.
- Discovery: The automatic process through which nodes determine how to talk to each other.

### Nodes
A node is a participant in the ROS graph. ROS nodes use a ROS client library to communicate with other nodes. Nodes can publish or subscribe to Topics. Nodes can also provide or use Services and Actions. There are configurable Parameters associated with a node. Connections between nodes are established through a distributed discovery process. Nodes may be located in the same process, in different processes, or on different machines. These concepts will be described in more detail in the sections that follow.

## Client Libraries 
ROS client libraries allow nodes written in different programming languages to communicate. There is a core ROS client library (RCL) that implements common functionality needed for the ROS APIs of different languages. This makes it so that language-specific client libraries are easier to write and that they have more consistent behavior.

The following client libraries are maintained by the ROS 2 team:

- rclcpp = C++ client library

- rclpy = Python client library

Additionally, other client libraries have been developed by the ROS community. 

## Discovery
Discovery of nodes happens automatically through the underlying middleware of ROS 2. It can be summarized as follows:

- When a node is started, it advertises its presence to other nodes on the network with the same ROS domain (set with the ROS_DOMAIN_ID environment variable). Nodes respond to this advertisement with information about themselves so that the appropriate connections can be made and the nodes can communicate.

- Nodes periodically advertise their presence so that connections can be made with new-found entities, even after the initial discovery period.

- Nodes advertise to other nodes when they go offline.

Nodes will only establish connections with other nodes if they have compatible Quality of Service settings.

## How to build ROS package
There are two packages inside your catkin_ws/src: the **my_robot** and the **ball_chaser**

Here are the steps to design the robot, house it inside your world, and program it to chase white-colored balls:

### 1.'''drive_bot''':

- Create a **my_robot** ROS package to hold the robot, the white ball, and the world.
- Design a differential drive robot with the Unified Robot Description Format. Add two sensors to your robot: a lidar and a camera. Add Gazebo plugins for the robot’s differential drive, lidar, and camera. 
- Create a new world 
- Add a white-colored ball to your Gazebo world and save a new copy of this world.
- The world.launch file should launch your world with the white-colored ball and your robot.
- 
### 2.'''ball_chaser''':

Create a **ball_chaser** ROS package to hold your C++ nodes.
Write a **drive_bo**tC++ node that will provide a **ball_chaser/command_robot** service to drive the robot by controlling its linear x and angular z velocities. The service should publish to the wheel joints and return back the requested velocities.
Write a **process_image** C++ node that reads your robot’s camera image, analyzes it to determine the presence and position of a white ball. If a white ball exists in the image, your node should request a service via a client to drive the robot towards it.
The **ball_chaser.launch** should run both the **drive_bot** and the **process_image** nodes.
