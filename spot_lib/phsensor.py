#!/usr/bin/env python

import serial
import time

port = serial.Serial('/dev/ttyS1', 38400, bytesize=8, parity='N', stopbits=1, timeout = 10)

def get_ph(temperature_C=20.0):
    # calibrate the probe to the water temperature
    # ideally received recently from the EC sensor
    port.write(str(temperature_C) + "\r")
    time.sleep(0.5)
    # tell the probe to take one reading
    port.write("r\r")
    time.sleep(0.5)
    val = ""
    for i in range(50):
        inputchar = port.read()
        if inputchar == "\r":
            break
        elif inputchar == "":
            print "pH sensor: no reading!"
            break
        else:
            val += inputchar
    return val


if __name__ == "__main__":
    print get_ph()
