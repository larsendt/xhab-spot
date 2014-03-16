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
LIGHTS_PUB = rospy.Publisher("/tasks/" + identity.get_spot_name() + "/lights", LightsTask)
VALVE_PUB = rospy.Publisher("/tasks/" + identity.get_spot_name() + "/valve", ValveTask)
CAMERA_PUB = rospy.Publisher("/tasks/" + identity.get_spot_name() + "/camera", CameraTask)


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
    with open("/home/xhab/data/door_status.txt", "r") as f:
        status = f.read()[0]

    if status == "1":
        newstatus = 0.0
        print "closing door"
    else:
        newstatus = 1.0
        print "opening door"

    msg = DoorTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    msg.open = newstatus

def light_time_request():
    print "light_time_request"
    with open("/home/xhab/data/light_time_request.txt", "r") as f:
        time = int(f.read().replace("\n", ""))

    # clamp to (0, 480), so we don't cause problems
    time = max(0, min(480, time))

    if time > 0:
        print "disabling lights for %d minutes" % time
        msg = LightsTask()
        msg.spot_id = identity.get_spot_name()
        msg.timestamp = rospy.Time.now()
        msg.disable_minutes = time
        LIGHTS_PUB.publish(msg)

        with open("/home/xhab/data/light_time_request.txt", "w") as f:
            f.write("0\n")

def light_brightness_request():
    print "light_brightness_request"
    msg = LightsTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()

    with open("/home/xhab/data/light_brightness_request.txt", "r") as f:
        brightness = min(255, int(f.read().replace("\n", "")))
    brightness /= 255.0

    msg.whites_on = True
    msg.reds_on = True

    print "setting brightness to %.2f" % brightness
    msg.brightness = brightness
    LIGHTS_PUB.publish(msg)

def drain_spot_request():
    print "drain_spot_request"
    msg = ValveTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    msg.valve_open = True
    print "opening valve"
    VALVE_PUB.publish(msg)


def take_picture_request():
    print "take_picture_request"
    msg = CameraTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    CAMERA_PUB.publish(msg)


def lcd_status():
    print "lcd_status"
    with open("/home/xhab/data/lcd_status.txt", "r") as f:
        text = f.read()[0]

    if text == "1":
        with open("/home/xhab/data/lcd_status.txt", "w") as f:
            f.write("0\n")
        print "NEED TO DO: sleep for 30 seconds"
        #time.sleep(30)
        print "NEED TO DO: lcd.lcd_off()"


PATH = "/home/xhab/data/"
FILES_TO_MONITOR = {"rotate_90_cw.txt":rotate_90_cw, 
                    "rotate_90_ccw.txt":rotate_90_ccw, 
                    "rotate_180.txt":rotate_180,
                    "door_change_request.txt":door_change_request,
                    "light_time_request.txt":light_time_request,
                    "light_brightness_request.txt":light_brightness_request,
                    "drain_spot_request.txt":drain_spot_request,
                    "take_picture_request.txt":take_picture_request,
                    "lcd_status.txt":lcd_status}

class EventProcessor(pyinotify.ProcessEvent):
    def __init__(self):
        print "LCDInterface init"
        rospy.init_node("LCDInterface")

    def process_IN_CLOSE_WRITE(self, event):
        if event.name in FILES_TO_MONITOR:
            func = FILES_TO_MONITOR[event.name]
            func()
        else:
            print "unknown event name:", event.name


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
