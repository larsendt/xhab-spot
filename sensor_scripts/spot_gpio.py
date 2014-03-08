#!/usr/bin/env python

""" 
This script provides convenient interfaces for writing/reading
the GPIO pins.
"""

import time

MODE_PATH = "/sys/devices/virtual/misc/gpio/mode/"
PIN_PATH = "/sys/devices/virtual/misc/gpio/pin/"

READ = "0"
WRITE = "1"
READ_PULLUP = "8"
OFF = "0"
ON = "1"

def set_pin_mode(pin, mode):
    if 0 <= pin <= 23:
        fname = MODE_PATH + "/gpio" + str(pin)
        with open(fname, "w") as f:
            f.write(mode)
    else:
        raise ValueError("Pin must be between 0 and 23 (inclusive)")

def set_pin(pin, on):
    if 0 <= pin <= 23:
        set_pin_mode(pin, WRITE)
        fname = PIN_PATH + "/gpio" + str(pin)
        with open(fname, "w") as f:
            if on:
                print "wrote ON"
                f.write(ON)
            else:
                print "wrote OFF"
                f.write(OFF)
    else:
        raise ValueError("Pin must be between 0 and 23 (inclusive)")

def get_pin(pin):
    if 0 <= pin <= 23:
        set_pin_mode(pin, READ)
        fname = PIN_PATH + "/gpio" + str(pin)
        with open(fname, "r") as f:
            return int(f.read())

    else:
        raise ValueError("Pin must be between 0 and 23 (inclusive)")

def get_pin_pullup(pin):
    if 0 <= pin <= 23:
        set_pin_mode(pin, READ_PULLUP)
        fname = PIN_PATH + "/gpio" + str(pin)
        with open(fname, "r") as f:
            return int(f.read())

def pin_path(pin):
    if 0 <= pin <= 23:
        return PIN_PATH + "/gpio" + str(pin)
    else:
        raise ValueError("Pin must be between 0 and 23 (inclusive)")
            

