#!/usr/bin/env python

"""
This is the base class for most SPOT ROS nodes. It takes care of creating a PID
file and some other busywork.
"""

import rospy
import psutil
import pidfile

PID_DIR = "/home/xhab/pidfiles"

class SPOTNode(object):
    def __init__(self):
        self.pidfname = pidfile.create_pidfile(self.__class__.__name__)
    
    def cleanup(self):
        pidfile.cleanup_self(self.__class__.__name__)


if __name__ == "__main__":
    import os
    s = SPOTNode()
    print "Pid file:", s.pidfname
    print "Pid info:", pidfile.get_pidinfo("SPOTNode", os.getpid())


