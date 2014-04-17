#!/usr/bin/env python

import sys
import rospy
from xhab_spot.msg import *
import identity
import time
import random
import serial
import initializer
import pins
import phsensor
import re

PUB_DELAY = 15

# convert fahrenheight to celsius
def f_to_c(f):
    return (f - 32) * (5/9.0)

class PHSensor(object):
    def __init__(self):
        print "PHSensor init"
        rospy.init_node("PHSensor")
        subtopic = "/tasks/" + identity.get_spot_name() + "/ph"
        pubtopic = "/data/" + identity.get_spot_name() + "/ph"
        self.alert_pub = rospy.Publisher("/alerts/" + identity.get_spot_name(), Alert)
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, PHTask, self.callback)
        self.reading = initializer.get_variable("ph_reading", 7.0)
        self.water_temp = f_to_c(float(initializer.get_variable("water_temp", "20.0")))
        print "PHSensor has water temperature: %.1f C" % self.water_temp

        self.callback(PHTask())
        

    def callback(self, msg):
        print "got msg, target =", msg.target

        self.water_temp = f_to_c(float(initializer.get_variable("water_temp", "20.0")))
        print "PHSensor has water temperature: %.1f C" % self.water_temp

        ph = phsensor.get_ph(self.water_temp)
        if re.match("\d+\.\d+", ph):
            self.reading = float(ph)
            initializer.put_variable("ph_reading", self.reading)
            print "read pH value:", self.reading
        else:
            msg = Alert()
            msg.timestamp = rospy.Time.now()
            msg.spot_id = identity.get_spot_name()
            msg.alert_text = "PHSensor got an error when reading pH:", ph
            self.alert_pub.publish(msg)
            print "PHSensor got an error:", ph


    def spin(self):
        print "PHSensor listening"
        while not rospy.is_shutdown():
            pubmsg = Data()
            pubmsg.source = identity.get_spot_name()
            pubmsg.property = "ph_reading"
            pubmsg.timestamp = rospy.Time.now()
            pubmsg.value = self.reading
            self.pub.publish(pubmsg)
            print "Published pH:", self.reading
            time.sleep(PUB_DELAY)


if __name__ == "__main__":
    try:
        p = PHSensor()
        p.spin()
    except rospy.ROSInterruptException:
        pass
