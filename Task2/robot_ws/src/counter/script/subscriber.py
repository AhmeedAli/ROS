#!/usr/bin/env python3.8

import rospy
from std_msgs.msg import int16

def call (msg):
    rodpy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data)

def listener ():
    rospy,init_node('listener', anonymous=True)
    rospy.Subscriber('counter', int16,call)
    rospy,spin ()

    listener()