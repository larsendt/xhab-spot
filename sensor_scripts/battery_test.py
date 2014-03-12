#!/usr/bin/env python

import sys
from battery_sensor import *

print len(sys.argv)

if len(sys.argv) == 4:
    Apin1 = int(sys.argv[1])
    Apin2 = int(sys.argv[2])
    Apin = int(sys.argv[3])
else:
    print "adc1 adc2 adc3"

charge_status = is_charging(Apin1,Apin2)
if charge_status == 1:
    status = "battery is charging"
elif charge_status == 2:
    status = "battery is fully charged"
else:
    status = "battery not detected"

battery_lvl = battery_level(Apin)
print "Battery charging status: %s" % status
print "Battery voltage: " + str(battery_lvl)
