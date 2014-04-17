import time, os
import pins
import spot_gpio
 
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
pinMode.append(os.path.join(GPIO_MODE_PATH, 'gpio'+str(pins.GPIO_DOOR_MOTOR_OPEN)))
pinData.append(os.path.join(GPIO_PIN_PATH, 'gpio'+str(pins.GPIO_DOOR_MOTOR_OPEN)))
pinMode.append(os.path.join(GPIO_MODE_PATH, 'gpio'+str(pins.GPIO_DOOR_MOTOR_CLOSE)))
pinData.append(os.path.join(GPIO_PIN_PATH, 'gpio'+str(pins.GPIO_DOOR_MOTOR_CLOSE)))

## Make all the pins outputs
for pin in pinMode:
    file = open(pin, 'r+')  ## open the file in r/w mode
    file.write(OUTPUT)      ## set the mode of the pin
    file.close()            ## IMPORTANT- must close file to make changes!

def _rotate(_open, _close, max_duration):
    start_time = time.time()

    spot_gpio.set_pin(pins.GPIO_DOOR_MOTOR_OPEN, _open)
    spot_gpio.set_pin(pins.GPIO_DOOR_MOTOR_CLOSE, _close)

    # wait for the hall effect sensor to go to zero
    time.sleep(1)

    while True:
        done = spot_gpio.get_pin(pins.GPIO_HALL_EFFECT_PIN)
        if done:
            print "hall effect sensor triggered"
            stop()
            return True
        else:
            now = time.time()
            if now - start_time > (max_duration - 1):
                print "hall effect sensor didn't trigger in %d seconds!" % max_duration
                stop()
                return False


def clock(max_duration):
    print "door clockwise (%d seconds)" % max_duration
    return _rotate(True, False, max_duration)

def counterclock(max_duration):
    print "door ccw (%d seconds)" % max_duration
    return _rotate(False, True, max_duration)

def stop():
    spot_gpio.set_pin(pins.GPIO_DOOR_MOTOR_OPEN, False)
    spot_gpio.set_pin(pins.GPIO_DOOR_MOTOR_CLOSE, False)


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
        

