#!/usr/bin/env python

import sys
sys.path.append("/home/xhab/xhab_spot/sensor_scripts")
import spot_gpio
import rospy
from std_msgs.msg import String

def callback(data):
	if data.data == "0":
		print "Lights off"
		spot_gpio.set_pin(8, False)
	elif data.data == "1":
		print "Lights on"
		spot_gpio.set_pin(8, False)
	else:
		print "Bad data: '%s'" % data.data

def listener():
	rospy.init_node("listener", anonymous=True)
	rospy.Subscriber("chatter", String, callback)
	print "listening..."
	rospy.spin()

if __name__ == "__main__":
	listener()
