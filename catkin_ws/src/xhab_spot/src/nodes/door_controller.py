#!/usr/bin/env python

import sys
import spot_gpio
import rospy
import time
from xhab_spot.msg import *
import identity

PUB_DELAY = 15

class DoorController(object):
    def __init__(self):
        print "DoorController init"
        rospy.init_node("DoorController")
        subtopic = "/tasks/" + identity.get_spot_name() + "/door"
        pubtopic = "/data/" + identity.get_spot_name() + "/door"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, DoorTask, self.callback)
        self.door_open = False

    def callback(self, msg):
        print "got msg, target =", msg.target

        if msg.open:
            print "door open!"
            self.door_open = True
        else:
            print "door closed!"
            self.door_open = False


    def spin(self):
        print "DoorController listening"
        while not rospy.is_shutdown():
            msg = Data()
            msg.source = identity.get_spot_name()
            msg.timestamp = rospy.Time().now()
            msg.property = "door_open"
            msg.value = 1.0 if self.door_open else 0.0
            self.pub.publish(msg)
            print "Published door status:", msg.value
            time.sleep(PUB_DELAY)

if __name__ == "__main__":
    try:
        c = DoorController()
        c.spin()
    except rospy.ROSInterruptException:
        pass
