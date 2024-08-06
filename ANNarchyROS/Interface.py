"""
:copyright: Copyright 2024 - now, see AUTHORS.
:license: GPLv3, see LICENSE for details.
"""

from .Mapping import ANNarchyROSMapping

from typing import List
import rospy

class ANNarchyROSInterface:

    def __init__(self, delayed_startup: bool = True, verbose_msg: bool = False):
        """
        Store the configuration and if not suppressed start the publisher/subscriber.
        """
        self._verbose_msg = verbose_msg
        self._channels = {}

        if not delayed_startup:
            self._ros_inited = self.startup_ros()
        else:
            self._ros_inited = False

    def startup_ros(self, node_name: str = "annarchy_simulation", topic_mapping: List[ANNarchyROSMapping] = []) -> bool :
        """
        Initialize
        """
        if self._ros_inited:
            print("ROS has been initialized already!")
            return True

        # should be done by user?
        rospy.init_node(node_name)

        # build-up communication channels
        for mapping in topic_mapping:
            self._channels[mapping.name] = self._init_topic(mapping)

        if self._verbose_msg:
            print("Initialized", len(self._channels), "ROS publisher(s)/subsriber(s).")
        
        return True

    def get_topic_by_name(self, name : str):
        """
        Get a topic channel by the user-defined *name*.
        """
        try:
            return self._channels[name]
        except KeyError:
            print("The topic", name, "probably not initialized ...")
            exit(-1)

    def run(self):
        """
        """
        rospy.spin()

    def _init_topic(self, mapping: ANNarchyROSMapping) -> rospy.Publisher | rospy.Subscriber:
        """
        """
        if mapping.topic_direction not in ['publisher', 'subscriber']:
            raise AttributeError("ANNarchyROSMapping.topic_direction must be  either 'publisher' or 'subscriber'")

        if mapping.topic_direction == 'publisher':
            instance = rospy.Publisher(mapping.topic_name, mapping.topic_msg_type, queue_size=mapping.queue_size)
        else:
            instance = rospy.Subscriber(mapping.topic_name, mapping.topic_msg_type, mapping.callback_func)

        return instance