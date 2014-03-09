#!/usr/bin/env python

import time

MODE_PATH = "/sys/devices/virtual/misc/gpio/mode/gpio"
PIN_PATH = "/sys/devices/virtual/misc/gpio/pin/gpio"
APIN_PATH = "/proc/adc"

HIGH = "1"
LOW =  "0"
INPUT = "0"
OUTPUT = "1"

def set_pin_mode(pin, mode):
    if 0 <= pin <= 23:
        fname = MODE_PATH + str(pin)
        with open(fname, "w") as f:
            f.write(mode)
            f.close()
    else:
        raise ValueError("Pin must be between 0 and 23 (inclusive)")

def set_pin(pin, on):
    if 0 <= pin <= 23:
        fname = PIN_PATH + str(pin)
        with open(fname, "w") as f:
            if on:
                print "Digital High"
                f.write(HIGH)
                f.close()
            else:
                print "Digital Low"
                f.write(LOW)
                f.close()
    else:
        raise ValueError("Pin must be between 0 and 23 (inclusive)")

def read_analog(Apin):
    if 0<= Apin <= 6:
        fname = APIN_PATH + str(Apin)
        with open(fname, "r+") as f:
            val = f.read()[5:-1]
            f.close()
            return val
