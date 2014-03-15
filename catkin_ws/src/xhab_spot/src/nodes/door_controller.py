#!/usr/bin/env python

import sys
import spot_gpio
import rospy
import time
from xhab_spot.msg import *
import identity

PUB_DELAY = 15

class CurtainController(object):
    def __init__(self):
        print "CurtainController init"
        rospy.init_node("CurtainController")
        subtopic = "/tasks/" + identity.get_spot_name() + "/curtain"
        pubtopic = "/data/" + identity.get_spot_name() + "/curtain"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, CurtainTask, self.callback)
        self.curtain_open = False

    def callback(self, msg):
        print "got msg, target =", msg.target

        if msg.open:
            print "curtain open!"
            self.curtain_open = True
        else:
            print "curtain closed!"
            self.curtain_open = False


    def spin(self):
        print "CurtainController listening"
        while not rospy.is_shutdown():
            msg = Data()
            msg.source = identity.get_spot_name()
            msg.timestamp = rospy.Time().now()
            msg.property = "curtain_open"
            msg.value = 1.0 if self.curtain_open else 0.0
            self.pub.publish(msg)
            print "Published curtain status:", msg.value
            time.sleep(PUB_DELAY)

if __name__ == "__main__":
    try:
        c = CurtainController()
        c.spin()
    except rospy.ROSInterruptException:
        pass
