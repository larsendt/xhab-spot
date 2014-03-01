#!/usr/bin/env python
import rospy
import time
import psutil
from std_msgs.msg import String

class LivenessMonitor(object):
    def __init__(self):
        print "LivenessMonitor init"
        rospy.init_node("LivenessMonitor")
        self.data_sub = rospy.Subscriber("sensor_data", String, self.data_callback)
        self.alert_pub = rospy.Publisher("alerts", String)

    def data_callback(self, data):
        print "liveness monitor got:", data.data

    def spin(self):
        print "LivenessMonitor listen"
        while not rospy.is_shutdown():
            found = False
            for proc in psutil.process_iter():
                if len(proc.cmdline) > 1 and "task_list.py" in proc.cmdline[1]:
                    found = True

            if not found:
                print "no task list!!!"
                self.alert_pub.publish("task_list.py appears to have died!")
            else:
                print "task list is okay"

            time.sleep(1)

if __name__ == "__main__":
    try:
        l = LivenessMonitor()
        l.spin()
    except rospy.ROSInterruptException:
        pass
            
