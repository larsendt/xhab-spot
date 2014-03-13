#!/usr/bin/env python

import time

DpinData="/sys/devices/virtual/misc/gpio/pin/gpio2" 
DpinMode = "/sys/devices/virtual/misc/gpio/mode/gpio2" 

ECFname = "/proc/adc2"
TempFname = "/proc/adc3"

## Create a few strings for file I/O equivalence
HIGH = "1"
LOW =  "0"
INPUT = "0"
OUTPUT = "1"


## Now, let's make all the pins outputs...

file = open(DpinMode, 'r+')  ## open the file in r/w mode
file.write(OUTPUT)      ## set the mode of the pin
file.close()            ## IMPORTANT- must close file to make changes!


while True:
    time.sleep(0.5)
    Dfile = open(DpinData, 'r+')
    Dfile.write(HIGH)
    Dfile.close()
    time.sleep(0.01)
    ECfile = open(ECFname, 'r+')
    Tfile = open(TempFname, 'r+')
    ECVal = ECfile.read()[5:-1]
    TVal = Tfile.read()[5:-1]
    ECfile.close()
    Tfile.close()
    time.sleep(.49)
    Dfile = open(DpinData, 'r+')
    Dfile.write(LOW)
    Dfile.close()
    print "EC Value :" + str(ECVal)
    ##print "Temperature Value :" + str(TVal) 
    Temp = int(TVal)
    y = (0.0000060954 * pow(Temp,2)) + (0.00690983 * Temp) + 20.9983
    print "Temperature value : " + str(int(y)) + "F"

