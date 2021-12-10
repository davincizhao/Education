# Where AM I robot
Localization in Robotics, there is Kalman Filter Localization Algorithms that is using in this projec

## Type of Localization Algorithms
- Extended Kalman Filter
- Markvo Localization
- Grid Localization
- Monte Carlo Localization

## What is Kalman Filter?
**Kalman filtering** is an algorithm that provides estimates of some unknown variables given the measurements observed over time. Kalman filters have been demonstrating its usefulness in various applications. Kalman filters have relatively simple form and require small computational power.
## Snapshot of Kalman Algorithm
![p1]()
![p2]()
### 1D Gaussian
At the basis of the Kalman Filter is the Gaussian distribution, sometimes referred to as a bell curve or normal distribution.
### Mean and Variance
A Gaussian is characterized by two parameters - its mean (μ) and its variance (σ²). The mean is the most probable occurrence and lies at the centre of the function, and the variance relates to the width of the curve. The term unimodal implies a single peak present in the distribution.
Gaussian distributions are frequently abbreviated as N(x: μ, σ²), and will be referred to in this way throughout the coming lessons.

# How to run the project
1. mkdir catkin_ws/src 
2. git clone package "where_am_i_robot" in "catkin_ws/src/"
3. run "catkin_init_workspace" in "catkin_ws/"
4. run "source devel/setup.bash" in "catkin_ws/"
5. run "roslaunch my_robot world.launch"
6. open new ternimal repeat 4 step,
7. run "roslaunch my_robot acml.launch"
8. open new ternimal repeat 4 step
9. run "rosrun teleop_twist_keyboard teleop_twist_keyboard.py" 
