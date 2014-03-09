#!/usr/bin/env python

import sys
import rospy
from xhab_spot.msg import *
import identity

import random

class PHSensor(object):
    def __init__(self):
        print "PHSensor init"
        rospy.init_node("PHSensor")
        subtopic = "/tasks/" + identity.get_spot_name() + "/ph"
        pubtopic = "/data/" + identity.get_spot_name() + "/ph"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, PHTask, self.callback)

    def callback(self, msg):
        print "got msg, target =", msg.target
        reading = random.normalvariate(7, 1)
        pubmsg = Data()
        pubmsg.source = identity.get_spot_name()
        pubmsg.property = "ph_reading"
        pubmsg.timestamp = rospy.Time.now()
        pubmsg.value = reading
        self.pub.publish(pubmsg)

    def spin(self):
        print "PHSensor listening"
        rospy.spin()

if __name__ == "__main__":
    try:
        p = PHSensor()
        p.spin()
    except rospy.ROSInterruptException:
        pass
