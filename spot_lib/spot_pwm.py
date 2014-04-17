#!/usr/bin/env python

import subprocess as sp
import time
import sys

PWM_EXE = "/home/xhab/xhab-spot/spot_lib/pwm"
PWM_PROC = None

def kill_proc():
    if PWM_PROC is not None:
        PWM_PROC.kill()
        PWM_PROC.wait()

sys.excepthook = lambda (x, y, z): kill_proc()

def set_pwm_pin(pin, value):
    if pin not in [3, 9, 10, 11]:
        print "Pin must be 3, 9, 10 or 11"
        return

    if not (0 <= value <= 1):
        print "Value must be between 0 and 1"
        return

    pin = str(pin)
    # this is the lowest frequency
    freq = "126"
    # duty can be between 0 and 253
    duty = str(int(value * 253))

    cmd = [PWM_EXE, pin, freq, duty]

    proc = sp.Popen(cmd, close_fds=True)
    global PWM_PROC
    PWM_PROC = proc
    time.sleep(0.5)
    proc.kill()
    proc.wait()



if __name__ == "__main__":
    set_pwm_pin(9, 0.5)
