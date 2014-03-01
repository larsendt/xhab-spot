#!/usr/bin/env python

import sys
sys.path.append("/home/xhab/xhab-spot/sensor_scripts")
import spot_gpio
import rospy
from std_msgs.msg import String

class LightController(object):
    def __init__(self):
        print "init LightController"
        rospy.init_node("LightController")
        self.pub = rospy.Publisher("sensor_data", String)
        self.sub = rospy.Subscriber("spot_tasks", String, self.callback)

    def callback(self, data):
        if data.data == "task: lights off":
            print "Lights off"
            spot_gpio.set_pin(8, False)
            self.pub.publish(String("lights off"))
        elif data.data == "task: lights on":
            print "Lights on"
            spot_gpio.set_pin(8, True)
            self.pub.publish(String("lights on"))
        else:
            print "Bad data: '%s'" % data.data

    def spin(self):
        print "LightController listening"
        rospy.spin()

if __name__ == "__main__":
    try:
        l = LightController()
        l.spin()
    except rospy.ROSInterruptException:
        pass
