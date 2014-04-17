#!/usr/bin/env python

"""
This script reads from the analog pins
and outputs a "graph"
"""

import time
import sys

fname = "/proc/adc" + sys.argv[1]
print "Reading from:", fname

while 1:
    with open(fname, "r") as f:
        val = int(f.read()[5:-1])
        frac = "%.1f%%" % (100 * (float(val) / 4095))
        print str(val) + " " + str(frac) + "   " + ("=" * (val / 25))
        time.sleep(0.1)
