#!/usr/bin/env python
import rospy
import time
import datetime
import spot_node
from xhab_spot.msg import *
import identity
import spot_topics


def lights_msg(on):
    msg = LightsTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    msg.brightness = 1.0 if on else 0.0
    msg.whites_on = True
    msg.reds_on = True
    return msg

def curtain_msg(curtain_open):
    msg = CurtainTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    msg.open = 1.0 if curtain_open else 0.0
    return msg

def ph_msg():
    msg = PHTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    return msg

def ec_msg():
    msg = ECTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    return msg

def battery_msg():
    msg = BatteryTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    return msg

MESSAGE_MAP = {"lights":lights_msg, "ph":ph_msg, "battery":battery_msg, "ec":ec_msg, "curtain":curtain_msg}

class TaskList(spot_node.SPOTNode):
    def __init__(self):
        super(TaskList, self).__init__()
        print "TaskList init"
        pub_topic = "/tasks/" + identity.get_spot_name()
        self.publishers = spot_topics.make_task_publishers(pub_topic)
        rospy.init_node("TaskList")


    def spin(self):
        print "TaskList listening"
        while not rospy.is_shutdown():
            cmd = raw_input("cmd> ")
            if cmd == "lights on":
                msg = lights_msg(True)
                topic = "lights"
            elif cmd == "lights off":
                msg = lights_msg(False)
                topic = "lights"
            elif cmd == "curtain open":
                msg = curtain_msg(True)
                topic = "curtain"
            elif cmd == "curtain close":
                msg = curtain_msg(False)
                topic = "curtain"
            elif cmd == "battery":
                msg = battery_msg()
                topic = "battery"
            elif cmd == "ec":
                msg = ec_msg()
                topic = "ec"
            elif cmd == "ph":
                msg = ph_msg()
                topic = "ph"
            else:
                print "Unknown message!"
                continue
            
            self.publishers[topic].publish(msg)
            print "Published on topic:", topic

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



