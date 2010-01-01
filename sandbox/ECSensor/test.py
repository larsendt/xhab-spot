#!/usr/bin/env python

import sys
import time
from ecsensor import *

##Create few strings for I/O equivalence
HIGH = "1"
LOW =  "0"
INPUT = "0"
OUTPUT = "1"

if len(sys.argv) == 4:
    gpio_pin = int(sys.argv[1])
    if not (0 <= gpio_pin <= 23):
        print "GPIO pin must be between 0 and 13"
        sys.exit(1)
    Apin1 = int(sys.argv[2])
    if not (0 <= Apin1 <= 7):
        print "Analog pin1 must be between 0 and 5"
        sys.exit(1)
    Apin2 = int(sys.argv[3])
    if not (0 <= Apin2 <= 7):
        print "Analog pin2 must be between 0 and 5"
        sys.exit(1)
else:
    print "Usage: <GPIO Pin> <Analog pin1> <Analog pin2>"

## Now, let's make all the pins outputs...
set_mode(gpio_pin, OUTPUT)

##Get the readings 
while True:
    time.sleep(0.5)
    set_pin(gpio_pin, 1)
    time.sleep(0.01)
    ECval = read_analog(Apin1)
    Tval = read_analog(Apin2)
    time.sleep(0.49)
    set_pin(gpio_pin, 0)
    print "EC Value: " + str(ECval)
    print "Temperature Value: " + str(Tval)
