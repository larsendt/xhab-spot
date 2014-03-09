#!/usr/bin/env python

import sys
import rospy
from xhab_spot.msg import *
import identity

import random

class BatterySensor(object):
    def __init__(self):
        print "BatterySensor init"
        rospy.init_node("BatterySensor")
        subtopic = "/tasks/" + identity.get_spot_name() + "/battery"
        pubtopic = "/data/" + identity.get_spot_name() + "/battery"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, BatteryTask, self.callback)

    def callback(self, msg):
        print "got msg, target =", msg.target
        reading = 0.75
        pubmsg = Data()
        pubmsg.source = identity.get_spot_name()
        pubmsg.property = "battery_level"
        pubmsg.timestamp = rospy.Time.now()
        pubmsg.value = reading
        self.pub.publish(pubmsg)

        pubmsg.property = "battery_charging"
        pubmsg.value = random.choice((1.0, 0.0))
        self.pub.publish(pubmsg)
        print "published 2 messages"

    def spin(self):
        print "BatterySensor listening"
        rospy.spin()

if __name__ == "__main__":
    try:
        p = BatterySensor()
        p.spin()
    except rospy.ROSInterruptException:
        pass
