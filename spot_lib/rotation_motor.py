import time, os
import pins
 
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

## First, populate the arrays with file objects that we can use later.
pinMode.append(os.path.join(GPIO_MODE_PATH, 'gpio'+str(pins.GPIO_ROTATION_LEFT)))
pinData.append(os.path.join(GPIO_PIN_PATH, 'gpio'+str(pins.GPIO_ROTATION_LEFT)))
pinMode.append(os.path.join(GPIO_MODE_PATH, 'gpio'+str(pins.GPIO_ROTATION_RIGHT)))
pinData.append(os.path.join(GPIO_PIN_PATH, 'gpio'+str(pins.GPIO_ROTATION_RIGHT)))

## Make all the pins outputs
for pin in pinMode:
    file = open(pin, 'r+')  ## open the file in r/w mode
    file.write(OUTPUT)      ## set the mode of the pin
    file.close()            ## IMPORTANT- must close file to make changes!

## Clockwise rotation function
def clock(dur):   
    print "clock:", dur
    file = open(pinData[0], 'r+') ##open the file in r/w mode
    file.write(LOW)        ## set the pin to LOW
    file.close()           ## IMPORTANT - must close file to make changes!

    file = open(pinData[1], 'r+') ##open the file in r/w mode
    file.write(HIGH)        ## set the pin to HIGH
    file.close()           ## IMPORTANT - must close file to make changes!

    time.sleep(dur)


## Counter-clockwise rotation function
def counterclock(dur):
    print "counterclock:", dur
    file = open(pinData[0], 'r+') ##open the file in r/w mode
    file.write(HIGH)        ## set the pin to HIGH
    file.close()           ## IMPORTANT - must close file to make changes!

    file = open(pinData[1], 'r+') ##open the file in r/w mode
    file.write(LOW)        ## set the pin to LOW
    file.close()           ## IMPORTANT - must close file to make changes!
    
    time.sleep(dur)

## Break operation function
def stop():
    print "stop"
    file = open(pinData[0], 'r+') ##open the file in r/w mode
    file.write(LOW)        ## set the pin to LOW
    file.close()           ## IMPORTANT - must close file to make changes!

    file = open(pinData[1], 'r+') ##open the file in r/w mode
    file.write(LOW)        ## set the pin to LOW
    file.close()           ## IMPORTANT - must close file to make changes!
    

if __name__ == "__main__":
    print "1. Counter-Clockwise rotation" 
    print "2. Clockwise rotation"
    option = raw_input('Choose an option:' )
    input_time = raw_input('Enter the duration of rotation in seconds: ')
    dur = float(input_time)

    if option=='1':
        counterclock(dur)
        stop()

    if option=='2':
        clock(dur)
        stop()
        

