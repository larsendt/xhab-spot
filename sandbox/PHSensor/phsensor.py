import serial ##Load the serial library

## Select and configure the port
myPort = serial.Serial('/dev/ttyS1', 115200, bytesize=8, parity='N', stopbits=1, timeout = 10)

##Wait for data to come in - one byte only
ph_volt = myPort.read()

##Echo the data to the command prompt
print "Ph voltage = " + ph_volt

##Close the port
myPort.close()

