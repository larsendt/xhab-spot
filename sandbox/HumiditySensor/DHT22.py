#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import dhtsensor

if len(sys.argv) != 2:
    print("usage: {0}  GPIOpin#".format(sys.argv[0]))
    print("example: {0} 2302 Read from an DHT22 connected to GPIO #4".format(sys.argv[0]))
    sys.exit(2)

dhtpin = int(sys.argv[1])
if dhtpin <= 0: #check what the boundary condition for gpio pin number should be"
    print("invalid GPIO pin#")
    sys.exit(3)

print("using pin #{0}".format(dhtpin))
t, h = dhtsensor.read(dhtpin)
if t and h:
    print("Temp = {0} *C, Hum = {1} %".format(t, h))
else:
    print("Failed to read from sensor, maybe try again?")
