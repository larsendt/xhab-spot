#!/usr/bin/env python
import rospy
import time
import datetime
import spot_node
from xhab_spot.msg import *
import identity
import spot_topics


_last_scheduled = {"lights":0}
_frequency = {"lights":15}
def should_schedule(name, curtime):
    if name not in _frequency:
        return False

    if name in _last_scheduled:
        if int(curtime) - _last_scheduled[name] > _frequency[name]:
            _last_scheduled[name] = curtime
            return True
        else:
            return False
    else:
        _last_scheduled[name] = curtime
        return True


class TaskList(spot_node.SPOTNode):
    def __init__(self):
        super(TaskList, self).__init__()
        print "TaskList init"
        pub_topic = "/tasks/" + identity.get_spot_name()
        self.publishers = spot_topics.make_task_publishers(pub_topic)
        rospy.init_node("TaskList")


    def maybe_broadcast_task(self):
        now = int(time.time())
        for topic in spot_topics.TOPICS:
            if should_schedule(topic, now):
                if topic == "lights":
                    pub = self.publishers[topic]
                    msg = LightsTask()
                    msg.spot_id = identity.get_spot_name()
                    msg.timestamp = rospy.Time.now()
                    msg.brightness = 1.0
                    msg.whites_on = True
                    msg.reds_on = True
                    pub.publish(msg)
                    print "published lights"


    def spin(self):
        print "TaskList listening"
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



