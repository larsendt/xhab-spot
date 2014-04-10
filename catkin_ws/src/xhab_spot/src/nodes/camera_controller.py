#!/usr/bin/env python

import sys
sys.path.append("/home/xhab/xhab-spot/sensor_scripts")
import spot_gpio
import rospy
from xhab_spot.msg import *
import identity
import time
import camera
import os
import initializer

PUB_DELAY = 15

class CameraController(object):
    def __init__(self):
        print "CameraController init"
        rospy.init_node("CameraController")
        subtopic = "/tasks/" + identity.get_spot_name() + "/camera"
        pubtopic = "/data/" + identity.get_spot_name() + "/camera"
        self.pub = rospy.Publisher(pubtopic, CameraData)
        self.sub = rospy.Subscriber(subtopic, CameraTask, self.callback)
        self.last_fname = initializer.get_variable("camera_last_fname", "")

    def callback(self, msg):
        print "got msg, target =", msg.target
        img = camera.snap_frame()
        if img is None:
            print "Failed to capture image!"
            return

        print "Captured image:", img

        pubmsg = CameraData()
        pubmsg.source = identity.get_spot_name()
        pubmsg.timestamp = rospy.Time.now()
        pubmsg.filename = img
        pubmsg.encoding = "JPG"
        pubmsg.property = os.path.basename(img)

        initializer.put_variable("camera_last_fname", img)
       
        with open(img, "rb") as f:
            pubmsg.photo_data = f.read()

        print "Photo is %d bytes" % len(pubmsg.photo_data)

        self.pub.publish(pubmsg)
        print "published msg"

    def spin(self):
        print "CameraController listening"
        rospy.spin()

if __name__ == "__main__":
    try:
        l = CameraController()
        l.spin()
    except rospy.ROSInterruptException:
        pass
