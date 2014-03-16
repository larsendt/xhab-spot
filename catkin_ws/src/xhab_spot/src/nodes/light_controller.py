#!/usr/bin/env python

import sys
sys.path.append("/home/xhab/xhab-spot/sensor_scripts")
import spot_gpio
import rospy
from xhab_spot.msg import *
import identity
import time

PUB_DELAY = 15

class LightController(object):
    def __init__(self):
        print "LightController init"
        rospy.init_node("LightController")
        subtopic = "/tasks/" + identity.get_spot_name() + "/lights"
        pubtopic = "/data/" + identity.get_spot_name() + "/lights"
        self.pub = rospy.Publisher(pubtopic, Data)
        self.alert_pub = rospy.Publisher("/alerts/" + identity.get_spot_name(), Alert)
        self.sub = rospy.Subscriber(subtopic, LightsTask, self.callback)
        self.brightness = 0.75
        self.reds_on = False
        self.whites_on = True
        self.disabled = False
        self.disable_start = 0
        self.disable_stop = 0

    def callback(self, msg):
        print "got msg, target =", msg.target
        
        self.brightness = msg.brightness
        print "brightness:", self.brightness

        self.whites_on = msg.whites_on
        print "whites on:", self.whites_on
        self.reds_on = msg.reds_on
        print "reds on:", self.reds_on

        if msg.disable_minutes > 0:
            print "disabled for %d minutes" % msg.disable_minutes
            seconds = msg.disable_minutes * 60
            self.disable_start = time.time()
            self.disable_stop = time.time() + seconds
            self.disabled = True

            alertmsg = Alert()
            alertmsg.spot_id = identity.get_spot_name()
            alertmsg.timestamp = rospy.Time.now()
            alertmsg.alert_text = "Lights disabled for %d minutes" % msg.disable_minutes
            self.alert_pub.publish(alertmsg)
        else:
            if self.disabled:
                print "lights no longer disabled!"
            self.disabled = False


    def spin(self):
        print "LightController listening"
        while not rospy.is_shutdown():
            if self.disabled:
                if time.time() > self.disable_stop:
                    print "lights no longer disabled!"
                    self.disabled = False

            msg = Data()
            msg.source = identity.get_spot_name()
            msg.timestamp = rospy.Time().now()
            msg.property = "lights_brightness"
            if self.disabled:
                msg.value = 0.0
            else:
                msg.value = self.brightness
            self.pub.publish(msg)
            print "Published lights brightness:", msg.value

            msg.property = "lights_reds_on"
            msg.value = 1.0 if self.reds_on else 0.0
            self.pub.publish(msg)
            print "Published lights reds on:", msg.value

            msg.property = "lights_whites_on"
            msg.value = 1.0 if self.whites_on else 0.0
            self.pub.publish(msg)
            print "Published lights whites on:", msg.value

            if self.disabled:
                diff = (self.disable_stop - time.time()) / 60.0
                alertmsg = Alert()
                alertmsg.spot_id = identity.get_spot_name()
                alertmsg.timestamp = rospy.Time.now()
                alertmsg.alert_text = "Lights disabled for another %.1f minutes" % diff
                self.alert_pub.publish(alertmsg)

            time.sleep(PUB_DELAY)

if __name__ == "__main__":
    try:
        l = LightController()
        l.spin()
    except rospy.ROSInterruptException:
        pass
