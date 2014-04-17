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

## First, populate the arrays with file objects that we can use later.
for i in range(0,3):
    pinMode.append(os.path.join(GPIO_MODE_PATH, 'gpio'+str(i)))
    pinData.append(os.path.join(GPIO_PIN_PATH, 'gpio'+str(i)))

## Make pins 0 and 1 as output
for pin in range[0,2]:
    file = open(pinMode[pin], 'r+')  ## open the file in r/w mode
    file.write(OUTPUT)      ## set the mode of the pin as output
    file.close()            ## IMPORTANT- must close file to make changes!

## Make pin 2 as input
file = open(pinMode[2], 'r+')  ##open the file in r/w mode
file.write(INPUT) ## set the mode of the pin as input 
file.close()   ## IMPORTANT- must close file to make changes!

count = 0

## Clockwise rotation function
def clock(dur):   
	file = open(pinData[0], 'r+') ##open the file in r/w mode
        file.write(LOW)        ## set the pin to LOW
        file.close()           ## IMPORTANT - must close file to make changes!

        file = open(pinData[1], 'r+') ##open the file in r/w mode
        file.write(HIGH)        ## set the pin to HIGH
        file.close()           ## IMPORTANT - must close file to make changes!

	time.sleep(dur)


## Counter-clockwise rotation function
def counterclock(dur):
	file = open(pinData[0], 'r+') ##open the file in r/w mode
        file.write(HIGH)        ## set the pin to HIGH
        file.close()           ## IMPORTANT - must close file to make changes!

        file = open(pinData[1], 'r+') ##open the file in r/w mode
        file.write(LOW)        ## set the pin to LOW
        file.close()           ## IMPORTANT - must close file to make changes!
	
	time.sleep(dur)

## Break operation function
def stop():
	file = open(pinData[0], 'r+') ##open the file in r/w mode
        file.write(LOW)        ## set the pin to LOW
        file.close()           ## IMPORTANT - must close file to make changes!

        file = open(pinData[1], 'r+') ##open the file in r/w mode
        file.write(LOW)        ## set the pin to LOW
        file.close()           ## IMPORTANT - must close file to make changes!
	

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
	

