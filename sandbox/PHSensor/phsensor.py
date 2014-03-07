import serial ##Load the serial library

## Select and configure the port
myPort = serial.Serial('/dev/ttyS1', 38400, bytesize=8, parity='N', stopbits=1, timeout = 10)

ph = ""

while(1):
    ##Wait for data to come in - one byte only
    inputchar = myPort.read()
    ph += inputchar
    if(inputchar == '\r'):
        ##Echo the data to the command prompt
        print "Ph value = " + ph
        ##Clear the string
        inputchar = ""
        ph = ""

##Close the port
myPort.close()

