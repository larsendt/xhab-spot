#!/usr/bin/env python

import spot_gpio
import sys
import time

# read
if len(sys.argv) == 3:
	mode = sys.argv[1]
	if mode == "write":
		print "Must provide write value"
		sys.exit(1)
	elif mode != "read":
		print "Unknown mode:", mode
		sys.exit(1)
	pin = int(sys.argv[2])
	if not (0 <= pin <= 23):
		print "Pin must be between 0 and 23"
		sys.exit(1)
	spot_gpio.set_pin_mode(pin, spot_gpio.WRITE)	
	while True:
		print spot_gpio.get_pin(pin)
		time.sleep(0.5)
#write
elif len(sys.argv) == 4:
	mode = sys.argv[1]
	pin = int(sys.argv[2])
	value = sys.argv[3]

	if mode == "read":
		print "Read only takes 2 arguments"
		sys.exit(1)
	elif mode != "write":
		print "Unknown mode:", mode
		sys.exit(1)

	if not (0 <= pin <= 23):
		print "Pin must be between 0 and 23"
		sys.exit(1)

	if not (value == "0" or value == "1"):
		print "Value must be 0 or 1"
		sys.exit(1)

	spot_gpio.set_pin_mode(pin, spot_gpio.READ)
	spot_gpio.set_pin(pin, value)

else:
	print "Usage: %s <read,write> <pin> [0,1]"
