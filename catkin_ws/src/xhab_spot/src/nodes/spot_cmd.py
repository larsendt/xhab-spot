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

def door_msg(door_open):
    msg = DoorTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    msg.open = 1.0 if door_open else 0.0
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

def water_level_msg():
    msg = WaterLevelTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    return msg

def battery_msg():
    msg = BatteryTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    return msg

def pump_msg(on):
    msg = PumpTask()
    msg.on = on
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    return msg

def fan_msg(on):
    msg = FanTask()
    msg.on = on
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    return msg

def rotation_msg(angle):
    msg = RotationTask()
    msg.angle = angle
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    return msg
    

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
            elif cmd == "door open":
                msg = door_msg(True)
                topic = "door"
            elif cmd == "door close":
                msg = door_msg(False)
                topic = "door"
            elif cmd == "battery":
                msg = battery_msg()
                topic = "battery"
            elif cmd == "ec":
                msg = ec_msg()
                topic = "ec"
            elif cmd == "ph":
                msg = ph_msg()
                topic = "ph"
            elif cmd == "pump on":
                msg = pump_msg(True)
                topic = "pump"
            elif cmd == "pump off":
                msg = pump_msg(False)
                topic = "pump"
            elif cmd == "fan on":
                msg = fan_msg(True)
                topic = "fan"
            elif cmd == "fan off":
                msg = fan_msg(False)
                topic = "fan"
            elif cmd == "water level":
                msg = water_level_msg()
                topic = "water_level"
            elif cmd.startswith("rotation"):
                angle = float(cmd.split(" ")[1])
                msg = rotation_msg(angle)
                topic = "rotation"
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



