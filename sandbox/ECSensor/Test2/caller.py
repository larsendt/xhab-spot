#!/usr/bin/env python

import sys
import time
from test import*

if len(sys.argv) == 4:
    gpio_pin = int(sys.argv[1])
    if not (0 <= gpio_pin <= 23):
        print "GPIO pin must be between 0 and 13"
        sys.exit(1)
    Apin1 = int(sys.argv[2])
    if not (0 <= Apin1 <= 5):
        print "Analog pin1 must be between 0 and 5"
        sys.exit(1)
    Apin2 = int(sys.argv[3])
    if not (0 <= Apin2 <= 5):
        print "Analog pin2 must be between 0 and 5"
        sys.exit(1)
else:
    gpio_pin = 6
    Apin1 = 2
    Apin2 = 3

'''
ECVal = EC_read(gpio_pin,Apin1,Apin2)
print "EC value: " + str(ECVal) + "microS/cm"

TVal = Temp_read(gpio_pin, Apin1, Apin2)
print "Temperature value: " + str(TVal) + "*F"
'''

ECVal, TVal = sensorData_read(gpio_pin, Apin1, Apin2)
print "EC value: " + str(ECVal) + "microS/cm"
print "Temperature value: " + str(TVal) + "*F"

