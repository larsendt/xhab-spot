#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import String

class DataArchiver(object):
    def __init__(self):
        rospy.init_node("DataArchiver")
        self.sub = rospy.Subscriber("sensor_data", String, self.data_callback)
        self.archive = []

    def data_callback(self, data):
        print "archiver got:", data.data
        self.archive.append((data.data, time.time))
        print "archiver has %d items" % len(self.archive)

    def spin(self):
        rospy.spin()

if __name__ == "__main__":
    try:
        d = DataArchiver()
        d.spin()
    except rospy.ROSInterruptException:
        pass
            
