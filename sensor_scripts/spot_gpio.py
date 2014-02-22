#!/usr/bin/env python

""" 
This script provides convenient interfaces for writing/reading
the GPIO pins.
"""

import time

mode_path = "/sys/devices/virtual/misc/gpio/mode/"
pin_path = "/sys/devices/virtual/misc/gpio/pin/"

READ = "0"
WRITE = "1"
OFF = "0"
ON = "1"

def set_pin_mode(pin, mode):
	if 0 <= pin <= 23:
		fname = mode_path + "/gpio" + str(pin)
		with open(fname, "w") as f:
			f.write(mode)
	else:
		raise ValueError("Pin must be between 0 and 23 (inclusive)")

def set_pin(pin, on):
	if 0 <= pin <= 23:
		set_pin_mode(pin, WRITE)
		fname = pin_path + "/gpio" + str(pin)
		with open(fname, "w") as f:
			if on:
				f.write(ON)
			else:
				f.write(OFF)
	else:
		raise ValueError("Pin must be between 0 and 23 (inclusive)")

def get_pin(pin):
	if 0 <= pin <= 23:
		set_pin_mode(pin, READ)
		fname = pin_path + "/gpio" + str(pin)
		with open(fname, "r") as f:
			return int(f.read())

	else:
		raise ValueError("Pin must be between 0 and 23 (inclusive)")

def pin_path(pin):
	if 0 <= pin <= 23:
		return pin_path + "/gpio" + str(pin)
	else:
		raise ValueError("Pin must be between 0 and 23 (inclusive)")
			

