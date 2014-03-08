#!/usr/bin/env python

import pyinotify
import time

FIRST_CALL = True

def callback(stuff):
    global FIRST_CALL
    if FIRST_CALL:
        FIRST_CALL = False
    else:
        print "callback!"


wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm)
wm.add_watch("./interrupt.txt", pyinotify.IN_CLOSE_WRITE)
notifier.loop(callback=callback)
