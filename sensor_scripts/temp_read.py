#!/usr/bin/env python

import time

"""
This script is for reading from the temperature
sensor. The analog pins return values from 0 to
4096. This script converts those to a -55 to 180
degree (C) scale and prints them along with a 
"graph"
"""

fname = "/proc/adc2"

counter = 0
while 1:
	with open(fname, "r") as f:
		val = int(f.read()[5:-1])
		temp = ((val / 4096.0) * 180) - 55
		if counter % 4 == 0:
			char = "|"
		elif counter % 4 == 1:
			char = "/"
		elif counter % 4 == 2:
			char = "-"
		elif counter % 4 == 3:
			char = "\\"
		print char + (" %.1f C (%d)" % (temp, val))
		counter += 1
		time.sleep(1)
