#!/usr/bin/env python

import sys
sys.path.append("/home/xhab/xhab-spot/sensor_scripts")
import spot_gpio
import rospy
from xhab_spot.msg import *
import identity
import time
import pyinotify

ROTATE_PUB = rospy.Publisher("/tasks/" + identity.get_spot_name() + "/rotation", RotationTask)
DOOR_PUB = rospy.Publisher("/tasks/" + identity.get_spot_name() + "/door", DoorTask)

def rotate_90_cw():
    print "rotate_90_cw"
    msg = RotationTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    msg.angle = 90
    ROTATE_PUB.publish(msg)

def rotate_90_ccw():
    print "rotate_90_ccw"
    msg = RotationTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    msg.angle = -90
    ROTATE_PUB.publish(msg)

def rotate_180():
    print "rotate_180"
    msg = RotationTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    msg.angle = 180
    ROTATE_PUB.publish(msg)

def door_change_request():
    print "door_change_request"

def lights_time_request():
    print "lights_time_request"

def lights_brightness_request():
    print "lights_brightness_request"

PATH = "/home/xhab/data/"
FILES_TO_MONITOR = {"rotate_90_cw.txt":rotate_90_cw, 
                    "rotate_90_ccw.txt":rotate_90_ccw, 
                    "rotate_180.txt":rotate_180,
                    "door_change_request.txt":door_change_request,
                    "lights_time_request.txt":lights_time_request,
                    "lights_brightness_request.txt":lights_brightness_request}

class EventProcessor(pyinotify.ProcessEvent):
    def __init__(self):
        print "LCDInterface init"
        rospy.init_node("LCDInterface")

    def process_IN_CLOSE_WRITE(self, event):
        if event.name in FILES_TO_MONITOR:
            func = FILES_TO_MONITOR[event.name]
            func()


def setup_notify():
    wm = pyinotify.WatchManager()
    notifier = pyinotify.ThreadedNotifier(wm, EventProcessor())
    notifier.start()
    wm.add_watch(PATH, pyinotify.IN_CLOSE_WRITE)
    return notifier


if __name__ == "__main__":
    try:
        notifier = setup_notify()
    except rospy.ROSInterruptException:
        notifier.stop()
