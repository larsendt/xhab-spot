#!/usr/bin/env python

import json
import sys
import time
sys.path.append("/home/xhab/xhab-spot/spot_lib/")
import spot_gpio

pval3 = spot_gpio.get_pin_pullup(3)
pval4 = spot_gpio.get_pin_pullup(4)
pval5 = spot_gpio.get_pin_pullup(5)
with open("test.json", "w") as f:
    obj = {"3val":pval3, "4val":pval4, "5val":pval5, "time":time.time()}
    json.dump(obj, f, indent=2)


