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

class PlantFanController(object):
    def __init__(self):
        print "PlantFanController init"
        rospy.init_node("PlantFanController")
        subtopic = "/tasks/" + identity.get_spot_name() + "/plant_fan"
        pubtopic = "/data/" + identity.get_spot_name() + "/plant_fan"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, PlantFanTask, self.callback)
        self.fan_on = initializer.get_variable("plant_fan_on", True)
        self.callback(PlantFanTask())

    def callback(self, msg):
        print "got msg, target =", msg.target

        self.fan_on = msg.on
        spot_gpio.set_pin(pins.GPIO_PLANT_FAN, msg.on)

        print "writing status"
        initializer.put_variable("plant_fan_on", self.fan_on)
        with open("/home/xhab/data/plant_fan_on.txt", "w") as f:
            f.write("1" if self.fan_on else "0")


    def spin(self):
        print "PlantFanController listening"
        while not rospy.is_shutdown():
            msg = Data()
            msg.source = identity.get_spot_name()
            msg.timestamp = rospy.Time().now()
            msg.property = "plant_fan_on"
            msg.value = 1.0 if self.fan_on else 0.0
            self.pub.publish(msg)
            print "Published plant fan status:", msg.value
            time.sleep(PUB_DELAY)

if __name__ == "__main__":
    try:
        c = PlantFanController()
        c.spin()
    except rospy.ROSInterruptException:
        pass
