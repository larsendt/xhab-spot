#!/usr/bin/env python

"""
This script reads raw values from the specified GPIO pin
"""

import time
READ_MODE = "0"
PIN = "21"
DELAY = 0.5

pin_file = "/sys/devices/virtual/misc/gpio/pin/gpio" + PIN
mode_file = "/sys/devices/virtual/misc/gpio/mode/gpio" + PIN

with open(mode_file, "w") as f:
	f.write(READ_MODE)

while 1:
	with open(pin_file, "r") as f:
		print f.read()[:-1]
		time.sleep(DELAY)
