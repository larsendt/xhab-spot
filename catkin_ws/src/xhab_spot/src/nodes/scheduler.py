#!/usr/bin/env python
import rospy
import time
from xhab_spot.msg import Scheduler
from std_msgs.msg import String
import identity

class Scheduler(object):
    def __init__(self):
        pub_topic = "/tasks/" + identity.get_spot_name() + "/scheduled"
        self.pub = rospy.Publisher(pub_topic, String)
        rospy.init_node("Scheduler")

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
            
