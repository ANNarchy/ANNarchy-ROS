# ANNarchy - ROS

ANNarchy (Artificial Neural Networks architect, www.github.com/ANNarchy/ANNarchy) is a parallel and hybrid simulator for distributed rate-coded or spiking neural networks. This package implements an interface to the ROS middleware. The ANNarchy-ROS package is released under the [GNU GPL v3 or later](http://www.gnu.org/licenses/gpl.html).

### Authors

* Helge Ülo Dinkelbach (helge-uelo.dinkelbach@informatik.tu-chemnitz.de)

## Installation

### Pre-requisites

If not already installed please install the *rospy* package (https://wiki.ros.org/ROS/Installation, currently we use ROS 1 Noetic).

For conda-users, one can use RoboStack for ROS Noetic - https://robostack.github.io/GettingStarted.html

If not already installed please install the *ANNarchy* package (see https://annarchy.github.io/Installation.html for more details).

### ANNarchy-ROS package

As the ANNarchy-ROS package is not available in PyPi yet (it's planned for the near future), you need to install it from sources via:

pip3 install .

in the source directory.

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
3. *python3 sim_control.py* located in *examples* which runs a simple client that repeatedly sends a *simulate* request to the ANNarchy controller.

This sample demonstrates the direct interaction between ANNarchy and the turtlesim environment. The position of the turtle is send to ANNarchy, being processed, a new action is computed, and then send to the turtlesim environment. Contrary to the above sample, in this setup the new action is only computed being triggered by a command from an external source (i.e., sim_control).







