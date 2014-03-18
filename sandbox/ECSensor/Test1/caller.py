#!/usr/bin/env python

import time
import ECSensor

ECVal = ECSensor.EC_read()
print "EC value: " + str(ECVal) + "microS/cm"

TVal = ECSensor.Temp_read()
print "Temperature value: " + str(TVal) + "*F"
