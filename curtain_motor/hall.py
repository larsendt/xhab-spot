import time, os

## Create a few strings for file I/O equivalence
HIGH = "1"
LOW =  "0"
INPUT = "0"
OUTPUT = "1"

PIN = "2"
DELAY = 0.5

pindata = "/sys/devices/virtual/misc/gpio/pin/gpio" + PIN
pinmode = "/sys/devices/virtual/misc/gpio/mode/gpio" + PIN 

while 1:
    file = open(pinmode, 'r+')  ## open the file in r/w mode
    file.write(INPUT)      ## set the mode of the pin
    file.close()            ## IMPORTANT- must close file to make changes!

    temp = ['']   ## a string to store the value 
    file = open(pindata, 'r') ## open the file
    temp[0] = file.read()       ## fetch the pin state

    print temp[0]

    time.sleep(DELAY)

