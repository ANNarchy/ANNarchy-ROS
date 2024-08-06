"""
:copyright: Copyright 2024 - now, see AUTHORS.
:license: GPLv3, see LICENSE for details.
"""

# Communication types these definitions come with the rospy packages
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from turtlesim.msg import Pose

# ANNarchy
from ANNarchyROS import *

class TurtleController(ANNarchyROSInterface):
    """
    This turtle controller implementation implements a closed loop interaction between the
    turtle and the environement. In the sense that, we get a position information and directly
    compute a new action, which is send to the environment.
    """
    def __init__(self, delayed_startup: bool = True, verbose_msg: bool = False):
        super().__init__(delayed_startup, verbose_msg)

    def startup_ros(self, node_name: str = "annarchy1", net : "Network" = None):
        # Communication in ROS is done by topics which need to be configured.
        topics = [
            # Incoming signal being processed by _pose_callback
            ANNarchyROSMapping(
                name="turtle_pose",
                topic_direction='subscriber',
                topic_name="/turtle1/pose",
                topic_msg_type=Pose,
                callback_func=self._pose_callback
            ),
            # Incoming signal being processed by _sim_callback
            ANNarchyROSMapping(
                name="turtle_pose",
                topic_direction='subscriber',
                topic_name="simulate",
                topic_msg_type=Float64,   # sim_time in ms, mapped to float in Python
                callback_func=self._sim_callback
            ),
            # Outgoing signal send at the end of _pose_callback
            ANNarchyROSMapping(
                name="turtle_vel",
                topic_direction='publisher',
                topic_name="/turtle1/cmd_vel",
                topic_msg_type=Twist,
                queue_size=10
            )
        ]

        # store the link to ANNarchy network
        self._net = net

        return super().startup_ros(node_name, topics)

    def _pose_callback(self, msg):
        """
        Automatically called when a *Pose* message has been received.
        """
        # get the neuron population by it's name
        pop = self._net.get_population("turtle_control")

        # update neural state
        pop.x = msg.x
        pop.y = msg.y
        
        print("Updated position:", pop.x, pop.y)
    
    def _sim_callback(self, msg):
        """
        """
        # do one simulation step
        self._net.step()

        # get the neuron population by it's name
        pop = self._net.get_population("turtle_control")

        # read-out the neural state and generate action message
        new_action = Twist()
        new_action.linear.x = pop.resp_1
        new_action.angular.z = pop.resp_2

        # send the new action
        self.get_topic_by_name("turtle_vel").publish(new_action)
