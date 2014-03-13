#!/usr/bin/env python

import sys
sys.path.append("/home/xhab/xhab-spot/sensor_scripts")
import spot_gpio
import rospy
from xhab_spot.msg import *
import identity
import time

PUB_DELAY = 15

class LightController(object):
    def __init__(self):
        print "LightController init"
        rospy.init_node("LightController")
        subtopic = "/tasks/" + identity.get_spot_name() + "/lights"
        pubtopic = "/data/" + identity.get_spot_name() + "/lights"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, LightsTask, self.callback)
        self.brightness = 0.75
        self.reds_on = False
        self.whites_on = True

    def callback(self, msg):
        print "got msg, target =", msg.target
        
        self.brightness = msg.brightness
        print "brightness:", self.brightness

        self.whites_on = msg.whites_on
        print "whites on:", self.whites_on
        self.reds_on = msg.reds_on
        print "reds on:", self.reds_on


    def spin(self):
        print "LightController listening"
        while not rospy.is_shutdown():
            msg = Data()
            msg.source = identity.get_spot_name()
            msg.timestamp = rospy.Time().now()
            msg.property = "lights_brightness"
            msg.value = self.brightness
            self.pub.publish(msg)
            print "Published lights brightness:", msg.value

            msg.property = "lights_reds_on"
            msg.value = 1.0 if self.reds_on else 0.0
            self.pub.publish(msg)
            print "Published lights reds on:", msg.value

            msg.property = "lights_whites_on"
            msg.value = 1.0 if self.whites_on else 0.0
            self.pub.publish(msg)
            print "Published lights whites on:", msg.value

            time.sleep(PUB_DELAY)

if __name__ == "__main__":
    try:
        l = LightController()
        l.spin()
    except rospy.ROSInterruptException:
        pass
