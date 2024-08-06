# ANNarchy - ROS

ANNarchy (Artificial Neural Networks architect, www.github.com/ANNarchy/ANNarchy) is a parallel and hybrid simulator for distributed rate-coded or spiking neural networks. This package implements an interface to the ROS middleware. The ANNarchy-ROS package is released under the [GNU GPL v3 or later](http://www.gnu.org/licenses/gpl.html).

### Authos

* Helge Ülo Dinkelbach (helge-uelo.dinkelbach@informatik.tu-chemnitz.de)

## Installation

### Pre-requisites

If not already installed please install the *rospy* package (https://wiki.ros.org/ROS/Installation, currently we use ROS 1 Noetic).

For conda-users, one can use RoboStack for ROS Noetic - https://robostack.github.io/GettingStarted.html

If not already installed please install the *ANNarchy* package.

### ANNarchy-ROS package

TODO:

### The turtlesim - demo (closed_loop)

As a first working prototype, we use the turtlesim environment already shipped with ROS. You need to run three separate terminal windows. Run the commands in the following order:

1. *roscore* : starts the ROS run-time environment.
2. *rosrun turtlesim turtlesim_node* which starts the turtlesim environment.
3. *python3 simple_demo.py* located in *examples* which runs the ANNarchy script.

This sample demonstrates the direct interaction between ANNarchy and the turtlesim environment. The position of the turtle is send to ANNarchy, being processed, a new action is computed, and then send to the turtlesim environment.

### The turtlesim - demo (external_cmd)

As a first working prototype, we use the turtlesim environment already shipped with ROS. You need to run three separate terminal windows. Run the commands in the following order:

1. *roscore* : starts the ROS run-time environment.
2. *rosrun turtlesim turtlesim_node* which starts the turtlesim environment.
3. *python3 simple_demo.py* located in *examples* which runs the ANNarchy script.
3. *python3 simple_demo.py* located in *examples* which runs the ANNarchy script.







