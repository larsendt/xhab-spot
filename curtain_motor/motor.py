import time, os

## For simplicity's sake, we'll create a string for our paths.
GPIO_MODE_PATH= os.path.normpath('/sys/devices/virtual/misc/gpio/mode/')
GPIO_PIN_PATH=os.path.normpath('/sys/devices/virtual/misc/gpio/pin/')
GPIO_FILENAME="gpio"

## create a couple of empty arrays to store the pointers for our files
pinMode = []
pinData = []

## Create a few strings for file I/O equivalence
HIGH = "1"
LOW =  "0"
INPUT = "0"
OUTPUT = "1"

#while True:
## First, populate the arrays with file objects that we can use later.
for i in range(0,5):
    pinMode.append(os.path.join(GPIO_MODE_PATH, 'gpio'+str(i)))
    pinData.append(os.path.join(GPIO_PIN_PATH, 'gpio'+str(i)))

## Make all the pins outputs
for pin in pinMode:
    file = open(pin, 'r+')  ## open the file in r/w mode
    file.write(OUTPUT)      ## set the mode of the pin
    file.close()            ## IMPORTANT- must close file to make changes!

## Make all the pins low
#for pin in pinData:
file = open(pinData[0], 'r+') ##open the file in r/w mode
file.write(LOW)        ## set the pin to LOW
file.close()           ## IMPORTANT - must close file to make changes!

file = open(pinData[1], 'r+') ##open the file in r/w mode
file.write(HIGH)        ## set the pin to LOW
file.close()           ## IMPORTANT - must close file to make changes!

file = open(pinData[2], 'r+') ##open the file in r/w mode
file.write(LOW)        ## set the pin to LOW
file.close() 

file = open(pinData[3], 'r+') ##open the file in r/w mode
file.write(HIGH)        ## set the pin to LOW
file.close()           ## IMPORTANT - must close file to make changes!

file = open(pinData[4], 'r+') ##open the file in r/w mode
file.write(LOW)        ## set the pin to LOW
file.close()           ## IMPORTANT - must close file to make changes!

from array import *
temp = ['','','','','']
file = open(pinData[0], 'r')
temp[0] = file.read()

file = open(pinData[1], 'r')
temp[1] = file.read()

file = open(pinData[2], 'r')
temp[2] = file.read()

file = open(pinData[3], 'r')
temp[3] = file.read()

file = open(pinData[4], 'r')
temp[4] = file.read()

print"" + temp[0] + temp[1] + temp[2] + temp[3] + temp[4]

    ##Rotate the left motor in Clockwise direction
    #file = open(pinData[3], 'r+') ## accessing pin 2 data file 
    #file.write(HIGH)      ## set the mode of the pin
    #file.close()          ## IMPORTANT- must close file to make changes!

    #file = open(pinData[4], 'r+') ## accessing pin 2 data file 
    #file.write(LOW)       ## set the mode of the pin
    #file.close()          ## IMPORTANT- must close file to make changes!

    #time.sleep(0.25)  

    ##Brake the rotation
    #file = open(pinData[3], 'r+') ## accessing pin 2 data file 
    #file.write(LOW)       ## set the mode of the pin
    #file.close()          ## IMPORTANT- must close file to make changes!

    #time.sleep(0.1)

    ##Rotate the left motor in Anti-Clockwise direction
    #file = open(pinData[3], 'r+') ## accessing pin 2 data file 
    #file.write(LOW)       ## set the mode of the pin
    #file.close()          ## IMPORTANT- must close file to make changes!

    #file = open(pinData[4], 'r+') ## accessing pin 2 data file 
    #file.write(HIGH)      ## set the mode of the pin
    #file.close()          ## IMPORTANT- must close file to make changes!

    #time.sleep(0.25)
    
    ##Brake the rotation
    #file = open(pinData[4], 'r+') ## accessing pin 2 data file 
    #file.write(LOW)       ## set the mode of the pin
    #file.close()          ## IMPORTANT- must close file to make changes!

    #time.sleep(0.5)


