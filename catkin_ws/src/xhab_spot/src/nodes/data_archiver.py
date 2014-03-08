#!/usr/bin/env python
import rospy
import time
import sqlite3
from std_msgs.msg import String
import spot_topics
import identity

class DataArchiver(object):
    def __init__(self):
        print "DataArchiver init"
        rospy.init_node("DataArchiver")
        subtopic = "/data/" + identity.get_spot_name() 
        self.subscribers = spot_topics.make_data_subscribers(subtopic, self.data_callback) 
        self.archive = []

    def data_callback(self, message):
        print "archiver got:", message 

    def spin(self):
        print "DataArchiver listening"
        rospy.spin()

if __name__ == "__main__":
    try:
        d = DataArchiver()
        d.spin()
    except rospy.ROSInterruptException:
        pass
            
