#!/usr/bin/env python

import sys
import spot_gpio
import rospy
import time
import pins
from xhab_spot.msg import *
import identity

PUB_DELAY = 15

class PumpController(object):
    def __init__(self):
        print "PumpController init"
        rospy.init_node("PumpController")
        subtopic = "/tasks/" + identity.get_spot_name() + "/pump"
        pubtopic = "/data/" + identity.get_spot_name() + "/pump"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, PumpTask, self.callback)
        self.pump_on = False

    def callback(self, msg):
        print "got msg, target =", msg.target

        if msg.on: 
            self.pump_on = True
            spot_gpio.set_pin(pins.GPIO_PUMP_PIN, True)
        else:
            self.pump_on = False
            spot_gpio.set_pin(pins.GPIO_PUMP_PIN, False)

        if msg.temporary_disable:
            print "Temporary disabling of the pump is not implemented yet!"

        print "writing status"
        with open("/home/xhab/data/pump_on.txt", "w") as f:
            f.write("1" if self.pump_on else "0")


    def spin(self):
        print "PumpController listening"
        while not rospy.is_shutdown():
            msg = Data()
            msg.source = identity.get_spot_name()
            msg.timestamp = rospy.Time().now()
            msg.property = "pump_on"
            msg.value = 1.0 if self.pump_on else 0.0
            self.pub.publish(msg)
            print "Published pump status:", msg.value
            time.sleep(PUB_DELAY)

if __name__ == "__main__":
    try:
        c = PumpController()
        c.spin()
    except rospy.ROSInterruptException:
        pass
