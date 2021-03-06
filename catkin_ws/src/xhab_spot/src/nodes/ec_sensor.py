#!/usr/bin/env python

import sys
import rospy
from xhab_spot.msg import *
import identity
import time
import random
import serial
import ecwrapper
import pins
import initializer

PUB_DELAY = 15

class ECSensor(object):
    def __init__(self):
        print "ECSensor init"
        rospy.init_node("ECSensor")
        subtopic = "/tasks/" + identity.get_spot_name() + "/ec"
        ecpubtopic = "/data/" + identity.get_spot_name() + "/ec"
        self.ecpub = rospy.Publisher(ecpubtopic, Data)
        waterpubtopic = "/data/" + identity.get_spot_name() + "/water_temperature"
        self.waterpub = rospy.Publisher(waterpubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, ECTask, self.callback)
        self.ec_reading = initializer.get_variable("ec_reading", 0)
        self.water_temp = initializer.get_variable("water_temp", 0)
        self.callback(ECTask())
        
    def callback(self, msg):
        print "got msg, target =", msg.target
        gpio_pin = pins.GPIO_EC_PIN
        Apin1 = pins.ADC_EC_PIN
        Apin2 = pins.ADC_WATER_TEMP_PIN
        self.ec_reading, self.water_temp = ecwrapper.sensorData_read(gpio_pin, Apin1, Apin2)
        
        print "read EC value:", self.ec_reading
        print "read water temp:", self.water_temp
        initializer.put_variable("ec_reading", self.ec_reading)
        initializer.put_variable("water_temp", self.water_temp)

    def spin(self):
        print "ECSensor listening"
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
        p = ECSensor()
        p.spin()
    except rospy.ROSInterruptException:
        pass
