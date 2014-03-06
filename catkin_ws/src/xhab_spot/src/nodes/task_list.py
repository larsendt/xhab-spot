#!/usr/bin/env python
import rospy
import time
import datetime
import spot_node
from xhab_spot.msg import *
import identity


TASKS = ["lights"]
_last_scheduled = {"lights":0}
_frequency = {"lights":15}
def should_schedule(name, curtime):
    if int(curtime) - _last_scheduled[name] > _frequency[name]:
        _last_scheduled[name] = curtime
        return True
    else:
        return False


class TaskList(spot_node.SPOTNode):
    def __init__(self):
        super(TaskList, self).__init__()
        pub_topic = "/tasks/" + identity.get_spot_name()
        self.pub = rospy.Publisher(pub_topic, Task)
        rospy.init_node("TaskList")

    def maybe_broadcast_task(self):
        now = int(time.time())
        for task in TASKS:
            if should_schedule(task, now):
                if task == "lights":
                    msg = LightsTask()
                    msg.spot_id = identity.get_spot_name()
                    msg.timestamp = rospy.Time.now()
                    msg.brightness = 1.0
                    msg.whites_on = True
                    msg.reds_on = True
                    self.pub.publish(msg)


    def spin(self):
        while not rospy.is_shutdown():
            self.maybe_broadcast_task()
            time.sleep(1)

        print "rospy shut down!"
                

if __name__ == "__main__":
    t = TaskList()
    try:
        t.spin()
    except rospy.ROSInterruptException:
        pass
    finally:
        print "cleanup!"
        t.cleanup() 



