#!/usr/bin/env python

import rospy
from xhab_spot.msg import *

TASK_MESSAGES = [BatteryTask, CameraTask, DoorTask, ECTask, FanTask,
                 HumidityTask, LightsTask, PHTask, PumpTask, RotationTask,
                 AirTemperatureTask, WaterTemperatureTask, WaterLevelTask, ValveTask]

DATA_MESSAGES = [Data]

TOPICS = ["battery", "camera", "door", "ec", "fan", "humidity", "lights",
          "ph", "pump", "rotation", "air_temperature", "water_temperature", 
          "water_level", "valve"]

PROPERTIES = ["battery_charging", "battery_level", "battery_full", "door_status", 
              "ec_reading", "fan_on", "humidity_reading", "lights_brightness", 
              "lights_whites_on", "lights_reds_on", "ph_reading", "pump_on", 
              "rotation_angle", "air_temperature", "water_temperature", "water_level"
              "valve_status"]


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
