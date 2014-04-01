#!/usr/bin/env python
import rospy
import time
import datetime
import spot_node
from xhab_spot.msg import *
import identity
import spot_topics


def lights_msg(brightness, reds):
    msg = LightsTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    msg.brightness = brightness
    msg.reds_on = reds
    return msg

def camera_msg():
    msg = CameraTask()
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
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

def camera_msg():
    msg = CameraTask()
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

def plant_fan_msg(on):
    msg = PlantFanTask()
    msg.on = on
    msg.spot_id = identity.get_spot_name()
    msg.timestamp = rospy.Time.now()
    return msg

def eps_fan_msg(on):
    msg = EPSFanTask()
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
    

class SPOTCmd(spot_node.SPOTNode):
    def __init__(self):
        super(SPOTCmd, self).__init__()
        print "SPOTCmd init"
        pub_topic = "/tasks/" + identity.get_spot_name()
        self.publishers = spot_topics.make_task_publishers(pub_topic)
        rospy.init_node("SPOTCmd")


    def spin(self):
        while not rospy.is_shutdown():
            cmd = raw_input("cmd> ")
            if cmd.startswith("lights"):
                brightness = float(cmd.split(" ")[1])
                on = True if cmd.split(" ")[2] == "reds_on" else False
                msg = lights_msg(brightness, on)
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
            elif cmd == "eps fan on":
                msg = eps_fan_msg(True)
                topic = "eps_fan"
            elif cmd == "eps fan off":
                msg = eps_fan_msg(False)
                topic = "eps_fan"
            elif cmd == "plant fan on":
                msg = plant_fan_msg(True)
                topic = "plant_fan"
            elif cmd == "plant fan off":
                msg = plant_fan_msg(False)
                topic = "plant_fan"
            elif cmd == "water level":
                msg = water_level_msg()
                topic = "water_level"
            elif cmd.startswith("rotation"):
                angle = float(cmd.split(" ")[1])
                msg = rotation_msg(angle)
                topic = "rotation"
            elif cmd == "camera":
                msg = camera_msg()
                topic = "camera"
            else:
                print "Unknown message!"
                continue
            
            self.publishers[topic].publish(msg)
            print "Published on topic:", topic

        print "rospy shut down!"
                

if __name__ == "__main__":
    t = SPOTCmd()
    try:
        t.spin()
    except rospy.ROSInterruptException:
        pass
    finally:
        print "cleanup!"
        t.cleanup() 



