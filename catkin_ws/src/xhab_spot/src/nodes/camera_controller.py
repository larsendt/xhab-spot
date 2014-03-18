#!/usr/bin/env python

import sys
sys.path.append("/home/xhab/xhab-spot/sensor_scripts")
import spot_gpio
import rospy
from xhab_spot.msg import *
import identity
import time

PUB_DELAY = 15

class CameraController(object):
    def __init__(self):
        print "CameraController init"
        rospy.init_node("CameraController")
        subtopic = "/tasks/" + identity.get_spot_name() + "/camera"
        pubtopic = "/data/" + identity.get_spot_name() + "/camera"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, CameraTask, self.callback)

    def callback(self, msg):
        print "got msg, target =", msg.target
        print "Camera take photo!"  

    def spin(self):
        print "CameraController listening"
        rospy.spin()

if __name__ == "__main__":
    try:
        l = CameraController()
        l.spin()
    except rospy.ROSInterruptException:
        pass
