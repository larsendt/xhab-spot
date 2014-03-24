#!/usr/bin/env python

# Some of this copied from Nivedita's "ecsensor.py" file.

from time import *

MODE_PATH = "/sys/devices/virtual/misc/gpio/mode/gpio"
PIN_PATH = "/sys/devices/virtual/misc/gpio/pin/gpio"
APIN_PATH = "/proc/adc"

HIGH = "1"
LOW =  "0"
INPUT = "0"
OUTPUT = "1"

# Digital output pin.
GPIO_water = 10

# Analog Input Read Pin
ADC_water = 5


# This function returns a value of 0-4 depending on whether the
# water level is empty (0), up to full (4)
def water_level_read(digitalPinOutput, analogPinInput):
    set_mode(digitalPinOutput, OUTPUT)
    set_pin(digitalPinOutput, 1)
    sleep(.5)
    value = read_analog(analogPinInput)
    set_pin(digitalPinOutput, 0)

    # Full!
    # If value 4096 - 620:
    if value >= 3475:
        return 4

    # Semi-full
    # If value (2.3 volts) 2854 + 620 or 2854 - 496
    elif 2358 <= value <= 3474:
        return 3

    # Half full
    # If value (1.5 volts) 1861 + 496 or 2854 - 496
    elif 1403 <= value <= 2357:
        return 2

    # Semi-empty
    # If value (0.76 volts) 943 + 620 or 2854-496
    elif 472 <= value <= 1402:
        return 1

    # Empty!
    # If value (0 volts) 0 + 471
    elif value <= 471:
        return 0
    # Error?
    else:
        return -1
    

def set_mode(pin, mode):
    if 0 <= pin <= 23:
        fname = MODE_PATH + str(pin)
        with open(fname, "r+") as f:
            f.write(mode)
            f.close()
    else:
        print "Pin must be between 0 and 13 (inclusive)"

def set_pin(pin, on):
    if 0 <= pin <= 23:
        fname = PIN_PATH + str(pin)
        with open(fname, "r+") as f:
            if on:
                #print "Digital High"
                f.write(HIGH)
                f.close()
            else:
                #print "Digital Low"
                f.write(LOW)
                f.close()
    else:
        print "Pin must be between 0 and 13 (inclusive)"

def read_analog(Apin):
    if 0<= Apin <= 6:
        fname = APIN_PATH + str(Apin)
        with open(fname, "r+") as f:
            val = f.read()[5:-1]
            f.close()
            return val
