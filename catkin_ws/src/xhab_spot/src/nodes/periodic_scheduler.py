#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import String

class Scheduler(object):
    def __init__(self):
        self.pub = rospy.Publisher("scheduled_tasks", String)
        rospy.init_node("PeriodicScheduler")

    def spin(self):
        while not rospy.is_shutdown():
            self.pub.publish(String("lights on"))
            print "scheduled lights on"
            time.sleep(15)
            self.pub.publish(String("lights off"))
            print "scheduled lights off"
            time.sleep(15)


if __name__ == "__main__":
    try:
        s = Scheduler()
        s.spin()
    except rospy.ROSInterruptException:
        pass
            
