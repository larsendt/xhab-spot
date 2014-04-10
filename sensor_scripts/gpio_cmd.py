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
    elif mode != "read" and mode != "readpullup":
        print "Unknown mode:", mode
        sys.exit(1)
    pin = int(sys.argv[2])
    if not (0 <= pin <= 23):
        print "Pin must be between 0 and 23"
        sys.exit(1)
    #spot_gpio.set_pin_mode(pin, spot_gpio.WRITE)    
    print "Reading from %s" % spot_gpio.pin_path(pin)
    while True:
        if mode == "read":
            print ("1 " + ("="*80)) if spot_gpio.get_pin(pin) == 1 else 0
        elif mode == "readpullup":
            print ("1 " + ("="*80)) if spot_gpio.get_pin_pullup(pin) == 1 else 0
        time.sleep(0.5)

#write
elif len(sys.argv) == 4:
    mode = sys.argv[1]
    pin = int(sys.argv[2])
    value = sys.argv[3]

    if mode == "read" or mode == "readpullup":
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

    print "Writing %s to %s" % (value, spot_gpio.pin_path(pin))
    spot_gpio.set_pin_mode(pin, spot_gpio.READ)
    if value == "1":
        spot_gpio.set_pin(pin, True)
    else:
        spot_gpio.set_pin(pin, False)
        

else:
    print "Usage: %s <read,readpullup,write> <pin> [0,1]"
