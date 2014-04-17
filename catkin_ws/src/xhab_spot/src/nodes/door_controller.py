#!/usr/bin/env python

import sys
import spot_gpio
import rospy
import time
from xhab_spot.msg import *
import identity
import door_motor
import os
import initializer

PUB_DELAY = 15

class DoorController(object):
    def __init__(self):
        print "DoorController init"
        print os.getenv("ROS_MASTER_URI")
        rospy.init_node("DoorController")
        subtopic = "/tasks/" + identity.get_spot_name() + "/door"
        pubtopic = "/data/" + identity.get_spot_name() + "/door"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.error_pub = rospy.Publisher("/alerts", Alert)
        self.sub = rospy.Subscriber(subtopic, DoorTask, self.callback)
        self.door_open = initializer.get_variable("door_open")

    def callback(self, msg):
        print "got msg, target =", msg.target

        if msg.open:
            print "door open!"
            self.door_open = True
            ok = door_motor.clock(5)
        else:
            print "door closed!"
            self.door_open = False
            ok = door_motor.counterclock(5)

        if not ok:
            msg = Alert()
            msg.spot_id = identity.get_spot_name()
            msg.timestamp = rospy.Time.now()
            msg.alert_text = "Door may be stuck!"
            self.error_pub.publish(msg)
            print "ERROR"
        
        print "writing status"
        initializer.put_variable("door_open", self.door_open)
        with open("/home/xhab/data/door_status.txt", "w") as f:
            f.write("1" if self.door_open else "0")
        sys.stdout.flush()


    def spin(self):
        print "DoorController listening"
        while not rospy.is_shutdown():
            msg = Data()
            msg.source = identity.get_spot_name()
            msg.timestamp = rospy.Time().now()
            msg.property = "door_open"
            msg.value = 1.0 if self.door_open else 0.0
            self.pub.publish(msg)
            print "Published door status:", msg.value
            sys.stdout.flush()
            time.sleep(PUB_DELAY)

if __name__ == "__main__":
    try:
        c = DoorController()
        c.spin()
    except rospy.ROSInterruptException:
        pass
