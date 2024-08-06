"""
A simple demo using ANNarchy and the turtlesim environment shipped with ROS.

:copyright: Copyright 2024 - now, see AUTHORS.
:license: GPLv3, see LICENSE for details.
"""

# User-defined implementations
from ann_network import create_network
from ann_turtle_controller import TurtleController

# ROS related
import rospy
from std_srvs.srv import Empty

###############################
# Ramp-up
###############################
if __name__ == '__main__':
    # Create controller
    controller = TurtleController(True, True)

    # Create the neural network
    ann_net = create_network()

    # Init ROS and link the ANNarchy network
    controller.startup_ros(net = ann_net)
 
    # reset turtlesim to initial state
    reset = rospy.ServiceProxy('/reset', Empty)
    reset()

    # HD (26th Jun. 24): I'm not sure yet, if this should be done
    #                    automatically after calling *startup_ros()*.
    controller.run()