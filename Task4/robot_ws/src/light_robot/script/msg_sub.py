#!/usr/bin/env python3.8
import rospy
from light_robot.msg import sensor

def sensor_callback(sensor_message):
    rospy.loginfo("new data received: (%d, %s, %.2f ,%.2f)", 
        sensor_message.id,sensor_message.name,
        sensor_message.temperature,sensor_message.humidity)
    
rospy.init_node('subscriber_node', anonymous=True)

rospy.Subscriber("sensor_topic", sensor, sensor_callback)

rospy.spin()
