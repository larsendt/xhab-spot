#!/usr/bin/env python

import sys
import rospy
from xhab_spot.msg import *
import identity
import time
import random
import battery_sensor
import pins

PUB_DELAY = 15

class BatterySensor(object):
    def __init__(self):
        print "BatterySensor init"
        rospy.init_node("BatterySensor")
        subtopic = "/tasks/" + identity.get_spot_name() + "/battery"
        pubtopic = "/data/" + identity.get_spot_name() + "/battery"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, BatteryTask, self.callback)
        self.charging = True
        self.level = 0.51
        self.full = False

    def callback(self, msg):
        print "got msg, target =", msg.target
        self.charging = battery_sensor.is_charging(pins.ADC_BATTERY_STATUS_PIN_1, pins.ADC_BATTERY_STATUS_PIN_2)
        self.level = battery_sensor.battery_level(pins.ADC_BATTERY_LEVEL_PIN)
        self.level = min(1.0, self.level)
        self.full = True if self.level >= 1.0 else False

    def spin(self):
        print "BatterySensor listening"
        while not rospy.is_shutdown():
            pubmsg = Data()
            pubmsg.source = identity.get_spot_name()
            pubmsg.property = "battery_level"
            pubmsg.timestamp = rospy.Time.now()
            pubmsg.value = self.level
            self.pub.publish(pubmsg)

            pubmsg.property = "battery_charging"
            pubmsg.value = 1.0 if self.charging else 0.0
            self.pub.publish(pubmsg)

            pubmsg.property = "battery_full"
            pubmsg.value = 1.0 if self.full else 0.0
            self.pub.publish(pubmsg)
            print "published"
            time.sleep(PUB_DELAY)

if __name__ == "__main__":
    try:
        p = BatterySensor()
        p.spin()
    except rospy.ROSInterruptException:
        pass
