#!/usr/bin/env python

# The contents of this file will have to go in the main start up file.

PATH = "/home/xhab/data/"

import lcddriver
import time
import json
import sys
import time
import pyinotify
import os

BASE_PATH = "/home/xhab/xhab-spot/spot_lib/"

pid = os.fork()
if pid == 0:
    os.execvp(BASE_PATH + "interrupt", [BASE_PATH + "interrupt"])

lcd = lcddriver.lcd()

# Need to incorporate this file.
# interruptFile = PATH + "interrupt.txt"

with open("interrupt.txt", "w") as f:
    f.write("0")

def callback(stuff):

    # If the interrupt is already being taken care of, don't change anything.
    if lcd.beingServiced == 1:
        return
   
    # The interrupt happens twice, so I ignore it the second time.
    if lcd.interruptFlag == 0:
        lcd.interruptFlag = 1
        return
    
    # Otherwise, do stuff...
    lcd.beingServiced = 1
    lcd.interruptFlag = 0
    
    count = 20
    okay = False
    while not okay:
        with open("interrupt.txt", "r") as f:
            text = f.read()
        try:
            if text[0] == "0":
                return
            okay = True
        except:
            count = count - 1
            if count < 0:
                print "ERROR in interrupt callback handler."
                okay = True

    time.sleep(.01)
    
    okay = False
    while not okay:
        with open("buttons.txt", "r") as f:
            text = f.read()
        try:
            buttons = (int(text[0]), int(text[2]), int(text[4]))
            if  (buttons[0] + buttons[1] + buttons[2]) != 2:
                lcd.beingServiced = 0
                return
            else:
                lcd.lcd_state_change(buttons)
                lcd.beingServiced = 0
                time.sleep(0.1)
                with open("interrupt.txt", "w") as f:
                    f.write("0")
            okay = True
        except IndexError:
            pass

wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm)
wm.add_watch("./interrupt.txt", pyinotify.IN_CLOSE_WRITE)
notifier.loop(callback=callback)


