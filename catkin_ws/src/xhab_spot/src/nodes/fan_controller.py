#!/usr/bin/env python

import sys
import spot_gpio
import rospy
import time
import pins
from xhab_spot.msg import *
import identity

PUB_DELAY = 15

class FanController(object):
    def __init__(self):
        print "FanController init"
        rospy.init_node("FanController")
        subtopic = "/tasks/" + identity.get_spot_name() + "/fan"
        pubtopic = "/data/" + identity.get_spot_name() + "/fan"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, FanTask, self.callback)
        self.fan_on = False

    def callback(self, msg):
        print "got msg, target =", msg.target

        self.fan_on = msg.on
        spot_gpio.set_pin(pins.GPIO_PLANT_FAN, msg.on)
        spot_gpio.set_pin(pins.GPIO_EPS_FAN, msg.on)

        print "writing status"
        with open("/home/xhab/data/fan_on.txt", "w") as f:
            f.write("1" if self.fan_on else "0")


    def spin(self):
        print "FanController listening"
        while not rospy.is_shutdown():
            msg = Data()
            msg.source = identity.get_spot_name()
            msg.timestamp = rospy.Time().now()
            msg.property = "fan_on"
            msg.value = 1.0 if self.fan_on else 0.0
            self.pub.publish(msg)
            print "Published fan status:", msg.value
            time.sleep(PUB_DELAY)

if __name__ == "__main__":
    try:
        c = FanController()
        c.spin()
    except rospy.ROSInterruptException:
        pass
