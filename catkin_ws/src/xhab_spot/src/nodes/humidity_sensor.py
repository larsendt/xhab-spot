#!/usr/bin/env python

import sys
import rospy
from xhab_spot.msg import *
import identity
import time
import random
import serial
import ecwrapper

PUB_DELAY = 15

class HumiditySensor(object):
    def __init__(self):
        print "HumiditySensor init"
        rospy.init_node("HumiditySensor")
        subtopic = "/tasks/" + identity.get_spot_name() + "/ec"
        humiditypubtopic = "/data/" + identity.get_spot_name() + "/humidity"
        self.humiditypub = rospy.Publisher(humiditypubtopic, Data)
        airpubtopic = "/data/" + identity.get_spot_name() + "/air_temperature"
        self.airpub = rospy.Publisher(airpubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, HumidityTask, self.callback)
        self.humidity_reading = 0.0
        self.air_temp = 0.0
        

    def callback(self, msg):
        print "got msg, target =", msg.target
        gpio_pin = 6
        Apin1 = 2
        Apin2 = 3
        self.ec_reading, self.water_temp = ecwrapper.sensorData_read(gpio_pin, Apin1, Apin2)
        
        print "read EC value:", self.ec_reading
        print "read water temp:", self.water_temp

    def spin(self):
        print "HumiditySensor listening"
        while not rospy.is_shutdown():
            pubmsg = Data()
            pubmsg.source = identity.get_spot_name()
            pubmsg.property = "ec_reading"
            pubmsg.timestamp = rospy.Time.now()
            pubmsg.value = self.ec_reading
            self.ecpub.publish(pubmsg)
            print "Published EC:", self.ec_reading

            pubmsg.property = "water_temperature"
            pubmsg.value = self.water_temp
            self.waterpub.publish(pubmsg)
            print "Published water temp:", self.water_temp
            time.sleep(PUB_DELAY)


if __name__ == "__main__":
    try:
        p = HumiditySensor()
        p.spin()
    except rospy.ROSInterruptException:
        pass
