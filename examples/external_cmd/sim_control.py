"""
:copyright: Copyright 2024 - now, see AUTHORS.
:license: GPLv3, see LICENSE for details.
"""

# ROS related
import rospy
from std_msgs.msg import Float64

###############################
# Ramp-up
###############################
if __name__ == '__main__':
    # start the node
    rospy.init_node("sim_control")

    pub = rospy.Publisher('simulate', Float64, queue_size=10)

    # send regularly the command to compute a new action ...
    r = rospy.Rate(20) # 5 Hz
    while not rospy.is_shutdown():
        print('send new simulate')
        pub.publish(1.0)
        r.sleep()