#!/usr/bin/env python3.8

import rospy
from std_msgs.msg import Int16

def call (msg):
    rospy.loginfo("I heard %s", msg.data)

def listener ():
    rospy.init_node("node2", anonymous=True)
    rospy.Subscriber('topic', Int16,call)
    rospy.spin()

if __name__ == "__main__":
    listener()