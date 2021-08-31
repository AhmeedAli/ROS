#!/usr/bin/env python3.8

import rospy
from light_robot.msgs import sensor
import random

pub = rospy.Publisher('sensor_topic', sensor, queue_size=10)
rospy.init_node('publisher_node', anonymous=True)
rate = rospy.Rate(2) 

i = 0
while not rospy.is_shutdown():
    test = sensor()
    test.id = 1
    test.name="parking_01"
    test.temperature = 24.33 + (random.random()*2)
    test.humidity = 33.41+ (random.random()*2)
    rospy.loginfo("I publish:")
    rospy.loginfo(test)
    pub.publish(test)
    rate.sleep()
    i=i+1
