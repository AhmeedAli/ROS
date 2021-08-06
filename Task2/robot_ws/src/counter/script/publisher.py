#!/usr/bin/env python3.8

import rospy
from std_msgs.msg import int16

def talker():
    pub= rospy.Publisher('topic', int,queue_size=10)
    rospy.init_node('node1')
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
    
     counter = counter + 1   
        rospy.loginfo (counter)
        pub.publish(counter)
        rate.sleep()

      talker()
