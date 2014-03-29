#!/usr/bin/env python

import subprocess as sp
import time
import os

BASE_PATH = "/home/xhab/camera/"

def snap_frame():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)

    stamp = time.strftime("%Y-%m-%d_%H:%M:%S_UTC", time.gmtime())
    fname = os.path.join(BASE_PATH, "snap_" + stamp + ".jpg")
    cmd = "fswebcam -r 640x480 --no-banner -v " + fname
    retcode = sp.call(cmd.split(" "))
    if retcode == 0:
        return fname
    else:
        return None


if __name__ == "__main__":
    snap_frame()
