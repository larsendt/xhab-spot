#!/usr/bin/env python

import sys
import spot_gpio
import rospy
import time
from xhab_spot.msg import *
import identity
import rotation_motor
import initializer

PUB_DELAY = 15

class RotationController(object):
    def __init__(self):
        print "RotationController init"
        rospy.init_node("RotationController")
        subtopic = "/tasks/" + identity.get_spot_name() + "/rotation"
        pubtopic = "/data/" + identity.get_spot_name() + "/rotation"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.sub = rospy.Subscriber(subtopic, RotationTask, self.callback)
        self.rotation_angle = initializer.get_variable("rotation_angle", 0)

    def callback(self, msg):
        print "got msg, target =", msg.target

        if msg.angle > 0:
            print "rotation left!"
            self.rotation_angle = msg.angle
            rotation_motor.clock(5)
            rotation_motor.stop()
        else:
            print "rotation right!"
            self.rotation_angle = msg.angle
            rotation_motor.counterclock(5)
            rotation_motor.stop()

        initializer.put_variable("rotation_angle", self.rotation_angle)
        
        print "writing status"
        with open("/home/xhab/data/rotation_angle.txt", "w") as f:
            f.write("1" if self.rotation_angle else "0")


    def spin(self):
        print "RotationController listening"
        while not rospy.is_shutdown():
            msg = Data()
            msg.source = identity.get_spot_name()
            msg.timestamp = rospy.Time().now()
            msg.property = "rotation_angle"
            msg.value = self.rotation_angle
            self.pub.publish(msg)
            print "Published rotation angle:", msg.value
            time.sleep(PUB_DELAY)

if __name__ == "__main__":
    try:
        c = RotationController()
        c.spin()
    except rospy.ROSInterruptException:
        pass
