#!/usr/bin/env python

import sys
import spot_gpio
import rospy
import time
import pins
from xhab_spot.msg import *
import identity
import initializer

PUB_DELAY = 15

class EPSFanController(object):
    def __init__(self):
        print "EPSFanController init"
        rospy.init_node("EPSFanController")
        subtopic = "/tasks/" + identity.get_spot_name() + "/eps_fan"
        pubtopic = "/data/" + identity.get_spot_name() + "/eps_fan"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, EPSFanTask, self.callback)
        self.fan_on = initializer.get_variable("eps_fan_on", True)

        msg = EPSFanTask()
        msg.on = self.fan_on
        self.callback(msg)

    def callback(self, msg):
        print "got msg, target =", msg.target

        self.fan_on = msg.on
        spot_gpio.set_pin(pins.GPIO_EPS_FAN, msg.on)
        initializer.put_variable("eps_fan_on", self.fan_on)

        print "writing status"
        with open("/home/xhab/data/eps_fan_on.txt", "w") as f:
            f.write("1" if self.fan_on else "0")


    def spin(self):
        print "EPSFanController listening"
        while not rospy.is_shutdown():
            msg = Data()
            msg.source = identity.get_spot_name()
            msg.timestamp = rospy.Time().now()
            msg.property = "eps_fan_on"
            msg.value = 1.0 if self.fan_on else 0.0
            self.pub.publish(msg)
            print "Published EPS fan status:", msg.value
            time.sleep(PUB_DELAY)

if __name__ == "__main__":
    try:
        c = EPSFanController()
        c.spin()
    except rospy.ROSInterruptException:
        pass
