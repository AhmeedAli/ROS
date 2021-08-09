#!/usr/bin/env python 3.8

import rospy
from std_msgs.msg import int16

def talker():
    pub= rospy.Publisher('topic', int,queue_size=10)
    rospy.init_node('node1', anonymous=True)
    rate = rospy.Rate(5)
    counter = 0
    while not rospy.is_shutdown():
    
        counter = counter + 1   
        rospy.loginfo (counter)
        pub.publish(counter)
        rate.sleep()

talker()
