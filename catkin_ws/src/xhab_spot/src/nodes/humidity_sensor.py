#!/usr/bin/env python

import sys
import rospy
from xhab_spot.msg import *
import identity
import time
import random
import serial
import ecwrapper
import initializer
import pins

PUB_DELAY = 15

class HumiditySensor(object):
    def __init__(self):
        print "HumiditySensor init"
        rospy.init_node("HumiditySensor")
        subtopic = "/tasks/" + identity.get_spot_name() + "/humidity"
        humiditypubtopic = "/data/" + identity.get_spot_name() + "/humidity"
        self.humiditypub = rospy.Publisher(humiditypubtopic, Data)
        airpubtopic = "/data/" + identity.get_spot_name() + "/air_temperature"
        self.airpub = rospy.Publisher(airpubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, HumidityTask, self.callback)
        self.humidity_reading = initializer.get_variable("humidity_reading", 0.0)
        self.air_temp = initializer.get_variable("air_temp", 0.0)
        self.callback(HumidityTask())        

    def callback(self, msg):
        print "got msg, target =", msg.target
        initializer.put_variable("humidity_reading", self.humidity_reading)
        initializer.put_variable("air_temp", self.air_temp)
        

    def spin(self):
        print "HumiditySensor listening"
        while not rospy.is_shutdown():
            pubmsg = Data()
            pubmsg.source = identity.get_spot_name()
            pubmsg.property = "humidity_reading"
            pubmsg.timestamp = rospy.Time.now()
            pubmsg.value = self.humidity_reading
            self.humiditypub.publish(pubmsg)
            print "Published humidity:", self.humidity_reading

            pubmsg.property = "air_temperature"
            pubmsg.value = self.air_temp
            self.airpub.publish(pubmsg)
            print "Published air temp:", self.air_temp
            time.sleep(PUB_DELAY)



if __name__ == "__main__":
    try:
        p = HumiditySensor()
        p.spin()
    except rospy.ROSInterruptException:
        pass
