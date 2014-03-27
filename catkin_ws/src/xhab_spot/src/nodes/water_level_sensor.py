#!/usr/bin/env python

import sys
import rospy
from xhab_spot.msg import *
import identity
import time
import random
import serial
import ecwrapper
import waterLevelDetector as wld

PUB_DELAY = 15

class WaterLevelSensor(object):
    def __init__(self):
        print "WaterLevelSensor init"
        rospy.init_node("WaterLevelSensor")
        subtopic = "/tasks/" + identity.get_spot_name() + "/water_level"
        pubtopic = "/data/" + identity.get_spot_name() + "/water_level"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, WaterLevelTask, self.callback)
        self.water_level = 0

    def callback(self, msg):
        print "got msg, target =", msg.target
        self.water_level = wld.water_level_read(pins.GPIO_WATER_LEVEL, pins.ADC_WATER_LEVEL_PIN)
        
        print "read water level", self.water_level

    def spin(self):
        print "WaterLevelSensor listening"
        while not rospy.is_shutdown():
            pubmsg = Data()
            pubmsg.source = identity.get_spot_name()
            pubmsg.property = "water_level"
            pubmsg.timestamp = rospy.Time.now()
            pubmsg.value = self.water_level
            self.pub.publish(pubmsg)
            print "Published water_level:", self.water_level

            time.sleep(PUB_DELAY)


if __name__ == "__main__":
    try:
        p = WaterLevelSensor()
        p.spin()
    except rospy.ROSInterruptException:
        pass
