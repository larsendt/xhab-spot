__author__ = 'skynet'

"""
This script sets all GPIO pins to write mode,
and then blinks them on and off.
"""

import time

mode_path = "/sys/devices/virtual/misc/gpio/mode/"
pin_path = "/sys/devices/virtual/misc/gpio/pin/"

mode_files = map(lambda x: mode_path + "gpio" + str(x), [4])
pin_files = map(lambda x: pin_path + "gpio" + str(x), [4])

for fname in mode_files:
    with open(fname, "w") as f:
        f.write("1")

while 1:
    for fname in mode_files:
        with open(fname, "w") as f:
            f.write("1")
            print "on"
            time.sleep(1)
            for fname in mode_files:
                with open(fname, "w") as f:
                    f.write("0")
                    print "off"
                    time.sleep(1)