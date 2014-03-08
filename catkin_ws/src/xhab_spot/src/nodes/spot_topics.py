#!/usr/bin/env python

import rospy
from xhab_spot.msg import *

TASK_MESSAGES = [BatteryTask, CameraTask, CurtainTask, ECTask, FanTask,
                 HumidityTask, LightsTask, PHTask, PumpTask, RotationTask,
                 TemperatureTask, WaterTask]

DATA_MESSAGES = [Data]

TOPICS = ["battery", "camera", "curtain", "ec", "fan", "humidity", "lights",
          "ph", "pump", "rotation", "temperature", "water"]


def make_task_publishers(base_topic):
    tt = zip(TOPICS, TASK_MESSAGES)
    pubs = {}
    for name, msg in tt:
        pubs[name] = rospy.Publisher(base_topic + "/" + name, msg)
    return pubs


def make_task_subscribers(base_topic, callback):
    tt = zip(TOPICS, TASK_MESSAGES)
    subs = {}
    for name, msg in tt:
        subs [name] = rospy.Subscriber(base_topic + "/" + name, msg, callback)
    return subs 


def make_data_subscribers(base_topic, callback):
    tt = map(lambda x: (x, Data), TOPICS)
    subs = {}
    for name, msg in tt:
        subs [name] = rospy.Subscriber(base_topic + "/" + name, msg, callback)
    return subs 
