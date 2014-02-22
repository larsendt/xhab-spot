#!/usr/bin/env python

import sys
sys.path.append("/home/xhab/xhab-spot/sensor_scripts")
import spot_gpio
import rospy
from std_msgs.msg import String

def callback(data):
    if data.data == "task: lights off":
        print "Lights off"
        spot_gpio.set_pin(8, False)
    elif data.data == "task: lights on":
        print "Lights on"
        spot_gpio.set_pin(8, True)
    else:
        print "Bad data: '%s'" % data.data

def listener():
    rospy.init_node("rosblinker", anonymous=True)
    rospy.Subscriber("spot_tasks", String, callback)
    print "listening..."
    rospy.spin()

if __name__ == "__main__":
    listener()
