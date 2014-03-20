#!/usr/bin/env python

import sys
import time
from ecsensor import *

##Create few strings for I/O equivalence
HIGH = "1"
LOW =  "0"
INPUT = "0"
OUTPUT = "1"

## Now, let's make all the pins outputs...

class EC:
    def __init__(self,pin1,pin2,pin3):
        self.gpio_pin = pin1
        self.Apin1 = pin2
        self.Apin2 = pin3
        self.ECval = 0
        self.Tval = 0

    def get_readings(self):
        set_mode(self.gpio_pin, OUTPUT)
        ##Get the readings
        for x in range(0,10):
            time.sleep(0.5)
            set_pin(self.gpio_pin, 1)
            time.sleep(0.01)
            ECVal = read_analog(self.Apin1)
            TVal = read_analog(self.Apin2)
            time.sleep(0.49)
            set_pin(self.gpio_pin, 0)
            ##print "EC Value: " + str(ECval)
            ##print "Temperature Value: " + str(Tval)
            Temp = int(TVal)
            self.Tval = (0.0000060954 * pow(Temp,2)) + (0.00690983 * Temp) + 20.9983
            ##print "Temperature value : " + str(int(y)) + "F"
            Temp1 = long(ECVal)
            self.ECval = (0.0023 * pow(Temp1,2)) - (12.6 * Temp1) + 17520.1
            ##print "EC value : " + str(int(y1)) + "microS/cm"


def EC_read(gpio_pin, Apin1, Apin2):
    ecsensor = EC(gpio_pin, Apin1, Apin2)
    ecsensor.get_readings()
    return ecsensor.ECval

def Temp_read(gpio_pin, Apin1, Apin2):
    ecsensor = EC(gpio_pin, Apin1, Apin2)
    ecsensor.get_readings()
    return ecsensor.Tval

def sensorData_read(gpio_pin, Apin1, Apin2):
    ecsensor = EC(gpio_pin, Apin1, Apin2)
    ecsensor.get_readings()
    return (ecsensor.ECval, ecsensor.Tval)
