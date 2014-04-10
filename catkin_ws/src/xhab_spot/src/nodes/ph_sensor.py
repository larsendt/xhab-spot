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

PUB_DELAY = 15

class PHSensor(object):
    def __init__(self):
        print "PHSensor init"
        rospy.init_node("PHSensor")
        subtopic = "/tasks/" + identity.get_spot_name() + "/ph"
        pubtopic = "/data/" + identity.get_spot_name() + "/ph"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, PHTask, self.callback)
        self.reading = initializer.get_variable("ph_reading", 7.0)
        self.port = serial.Serial('/dev/ttyS1', 38400, bytesize=8, parity='N', stopbits=1, timeout = 10)

        self.callback(PHTask())
        

    def callback(self, msg):
        print "got msg, target =", msg.target
        val = ""
        for i in range(50):
            inputchar = self.port.read()
            print "inputchar:", inputchar
            if inputchar == "\r":
                self.reading = float(val)
                break
            elif inputchar == "":
                print "no reading"
                return
            else:
                val += inputchar

        initializer.put_variable("ph_reading", self.reading)
        print "read pH value:", self.reading

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
