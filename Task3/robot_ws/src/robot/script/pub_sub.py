#!/usr/bin/env python3.8

from typing import Counter
import rospy
from std_msgs.msg import Int16

    Counter = 0
    pub= rospy.Publisher('topic', Int16,queue_size=10)
def call (msg):
    rospy.loginfo("I heard %s", msg.data)

    while not rospy.is_shutdown():
    
        counter = counter + 1   
        rospy.loginfo (counter)
        pub.publish(counter)
        rate.sleep()

def listener():
    rospy.init_node("node2", anonymous=True)
    rospy.Subscriber('topic', Int16,call)
    rospy.spin()

if __name__ == "__main__":
     try:
        listener()
     except rospy.ROSInterruptException:
        pass    