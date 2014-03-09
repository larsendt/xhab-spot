#!/usr/bin/env python

import sys
sys.path.append("/home/xhab/xhab-spot/sensor_scripts")
import spot_gpio
import rospy
from xhab_spot.msg import *
import identity

class LightController(object):
    def __init__(self):
        print "LightController init"
        rospy.init_node("LightController")
        subtopic = "/tasks/" + identity.get_spot_name() + "/lights"
        pubtopic = "/data/" + identity.get_spot_name() + "/lights"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, LightsTask, self.callback)

    def callback(self, msg):
        print "got msg, target =", msg.target

        pubmsg = Data()
        pubmsg.source = identity.get_spot_name()
        pubmsg.property = "lights_brightness"
        pubmsg.timestamp = rospy.Time.now()
        pubmsg.value = msg.brightness
        self.pub.publish(pubmsg)

        pubmsg = Data()
        pubmsg.source = identity.get_spot_name()
        pubmsg.property = "lights_whites_on"
        pubmsg.timestamp = rospy.Time.now()
        pubmsg.value = 1.0 if msg.whites_on else 0.0
        self.pub.publish(pubmsg)

        pubmsg = Data()
        pubmsg.source = identity.get_spot_name()
        pubmsg.property = "lights_reds_on"
        pubmsg.timestamp = rospy.Time.now()
        pubmsg.value = 1.0 if msg.reds_on else 0.0
        self.pub.publish(pubmsg)

        print "published three messages"


    def spin(self):
        print "LightController listening"
        rospy.spin()

if __name__ == "__main__":
    try:
        l = LightController()
        l.spin()
    except rospy.ROSInterruptException:
        pass
