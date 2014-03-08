#!/usr/bin/env python

import json
import sys
import time

pin3 = sys.argv[1]
pin4 = sys.argv[2]
pin5 = sys.argv[3]

obj = {"pin3":pin3, "pin4":pin4, "pin5":pin5, "time":time.time()}

with open("test.json", "w") as f:
    json.dump(obj, f, indent=2)
