#!/usr/bin/env python3.8

import rospy
from std_msgs.msg import Int16

def talker():
    pub= rospy.Publisher('topic', Int16,queue_size=10)
    rospy.init_node('node1', anonymous=True)
    rate = rospy.Rate(5)
    counter = 0
    while not rospy.is_shutdown():
    
        counter = counter + 1   
        rospy.loginfo (counter)
        pub.publish(counter)
        rate.sleep()
if __name__ == "__main__":
     try:
        talker()
     except rospy.ROSInterruptException:
        pass