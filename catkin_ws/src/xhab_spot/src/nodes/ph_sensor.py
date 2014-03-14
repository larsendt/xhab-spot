#!/usr/bin/env python

import sys
import rospy
from xhab_spot.msg import *
import identity
import time
import random

PUB_DELAY = 15

class PHSensor(object):
    def __init__(self):
        print "PHSensor init"
        rospy.init_node("PHSensor")
        subtopic = "/tasks/" + identity.get_spot_name() + "/ph"
        pubtopic = "/data/" + identity.get_spot_name() + "/ph"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, PHTask, self.callback)
        self.reading = 7.0

    def callback(self, msg):
        print "got msg, target =", msg.target
        self.reading = random.normalvariate(7, 1)
        print "read pH value:", self.reading

    def spin(self):
        print "PHSensor listening"
        while not rospy.is_shutdown():
            pubmsg = Data()
            pubmsg.source = identity.get_spot_name()
            pubmsg.property = "ph_reading"
            pubmsg.timestamp = rospy.Time.now()
            pubmsg.value = self.reading
            self.pub.publish(pubmsg)
            print "Published pH:", self.reading
            time.sleep(PUB_DELAY)


if __name__ == "__main__":
    try:
        p = PHSensor()
        p.spin()
    except rospy.ROSInterruptException:
        pass
