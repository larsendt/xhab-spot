#!/usr/bin/env python

import time, os

## For simplicity's sake, we'll create a string for our paths.
GPIO_MODE_PATH= os.path.normpath('/sys/devices/virtual/misc/gpio/mode/')
GPIO_PIN_PATH=os.path.normpath('/sys/devices/virtual/misc/gpio/pin/')
GPIO_FILENAME="gpio"


## Create a few strings for file I/O equivalence
HIGH = "1"
LOW =  "0"
INPUT = "0"
OUTPUT = "1"
INPUT_PU = "8"

## First, populate the arrays with file objects that we can use later.
pinMode = os.path.join(GPIO_MODE_PATH, 'gpio2')
pinData = os.path.join(GPIO_PIN_PATH, 'gpio2')

## Now, let's make all the pins outputs...
file = open(pinMode, 'r+')  ## open the file in r/w mode
file.write(OUTPUT)      ## set the mode of the pin
file.close()            ## IMPORTANT- must close file to make changes!

OUTVALUE = "0"

#initial configuration
file = open(pinData, 'r+')
file.write(HIGH)
file.close()

file = open(pinData, 'r+')
OUTVALUE = file.read(1)
print OUTVALUE + '\n'
  

time.sleep(1)

#initial configuration
file = open(pinData, 'r+')
file.write(LOW)
file.close()

file = open(pinData, 'r+')
OUTVALUE = file.read(1)
print OUTVALUE + '\n'

time.sleep(1)


file = open(pinMode, 'r+')
file.write(INPUT)
file.close();

file = open(pinData,'r+')
while True:
  OUTVALUE = file.read(1)
  print 'inwhile' + OUTVALUE + '\n'
  if OUTVALUE == HIGH:
    time.sleep(0.001)
  else:
    break
file.close()


'''
for i in range(0,10):
  if (OUTVALUE == "1"):
      OUTVALUE = "0";
  else:
      OUTVALUE = "1";
  print OUTVALUE
  file = open(pinData, 'r+')
  file.write(OUTVALUE)
  file.close
  time.sleep(1)  ## sleep for 1/10 of a second.
'''
ONES = 0;
ZEROS = 0;
OTHER = 0;

for i in range(0,20000):
  file = open(pinData, 'r+')
  OUTVALUE = file.read(1)
  if OUTVALUE == HIGH:
    ONES += 1
  elif OUTVALUE == LOW:
    ZEROS += 1
  else:
    OTHER += 1
  time.sleep(0.005)
  file.close()

print 'ones ' + str(ONES) + ' zeros ' + str(ZEROS) + ' others ' + str(OTHER) + '\n'

  
