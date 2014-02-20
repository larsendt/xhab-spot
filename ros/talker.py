#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher("chatter", String)
	rospy.init_node("talker")
	while not rospy.is_shutdown():
		try:	
			value = raw_input("value (0,1)> ")
			if value != "0" and value != "1":
				print "bad value '%s'" % value
				raise ValueError("Input must be 0 or 1.")
			rospy.loginfo(value)
			pub.publish(String(value))
			rospy.sleep(1.0)
			print "wrote", value
		except ValueError:
			print "input 0 or 1"

if __name__ == "__main__":
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
			
