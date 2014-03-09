#!/usr/bin/env python

import sys
import rospy
from xhab_spot.msg import *
import identity

import random

class ECSensor(object):
    def __init__(self):
        print "ECSensor init"
        rospy.init_node("ECSensor")
        subtopic = "/tasks/" + identity.get_spot_name() + "/ec"
        pubtopic = "/data/" + identity.get_spot_name() + "/ec"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, ECTask, self.callback)

    def callback(self, msg):
        print "got msg, target =", msg.target
        reading = random.normalvariate(7, 1)
        pubmsg = Data()
        pubmsg.source = identity.get_spot_name()
        pubmsg.property = "ec_reading"
        pubmsg.timestamp = rospy.Time.now()
        pubmsg.value = reading
        self.pub.publish(pubmsg)

    def spin(self):
        print "ECSensor listening"
        rospy.spin()

if __name__ == "__main__":
    try:
        p = ECSensor()
        p.spin()
    except rospy.ROSInterruptException:
        pass
