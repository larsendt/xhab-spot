#!/usr/bin/env python

import rospy
from xhab_spot.msg import *

TASK_MESSAGES = [BatteryTask, CameraTask, CurtainTask, ECTask, FanTask,
         HumidityTask, LightsTask, PHTask, PumpTask, RotationTask,
         TemperatureTask, WaterTask]

TOPICS = ["battery", "camera", "curtain", "ec", "fan", "humidity", "lights",
          "ph", "pump", "rotation", "temperature", "water"]


def make_all_publishers(base_topic):
    tt = zip(TOPICS, TASK_MESSAGES)
    pubs = {}
    for name, msg in tt:
        pubs[name] = rospy.Publisher(base_topic + "/" + name, msg)
    return pubs


def make_all_subscribers(base_topic, callback):
    tt = zip(TOPICS, TASK_MESSAGES)
    subs = {}
    for name, msg in tt:
        subs [name] = rospy.Publisher(base_topic + "/" + name, msg, callback)
    return subs 
