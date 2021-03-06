import serial ## Load the serial library

## Select and configure the port
myPort = serial.Serial('/dev/ttyS1', 115200, timeout = 10)

## Dump some data out of the port
myPort.write("1")

## Wait for data to come in- one byte, only
x = myPort.read(10)

## Echo the data to the command prompt
print "You entered " + x
## Close the port so other applications can use it.
myPort.close()

