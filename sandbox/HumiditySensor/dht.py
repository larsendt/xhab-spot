#!/usr/bin/env python
import subprocess
import time

    
class dht:
    def __init__(self,pin):
        self.pin = pin
        self.temp = 0
        self.humidity = 0
        self.error = -999
            
    def getTemp(self):
        return self.temp
    
    def getHumid(self):
        return self.humidity
    
    def getError(self):
        return self.error

    
    def readData(self):
        time.sleep(2) #make sure that read is not called within 2 seconds.
        if(self.pin  < 0 or self.pin > 23):
            self.error = -7
        else:
            cmd = './dht ' + str(self.pin)
            tmp = subprocess.Popen(cmd,shell = True, stdout = subprocess.PIPE)
            tmp.wait()
            out,err=tmp.communicate()
            #print out
            if(len(out.split(','))  > 0):
                if(out.split(',')[0] == '0'):#succes
                    self.temp = (float)(out.split(',')[1])
                    self.humidity = (float)(out.split(',')[2])
                #else:#failure error
                    self.error = (int)(out.split(',')[0])
            else:
                self.error = -6
                        

def getTemperature(pin):
    dhtsensor = dht(pin)
    dhtsensor.readData()
    return (dhtsensor.getTemp(),dhtsensor.getError())

def getHumidity(pin):
    dhtsensor = dht(pin)
    dhtsensor.readData()
    return (dhtsensor.getHumid(),dhtsensor.getError())
        
def getTemperatureInt(pin):
    dhtsensor = dht(pin)
    dhtsensor.readData()
    return ((int)(dhtsensor.getTemp()),dhtsensor.getError())


def getHumidityInt(pin):
    dhtsensor = dht(pin)
    dhtsensor.readData()
    return ((int)(dhtsensor.getHumid()),dhtsensor.getError())
   


def getSensorData(pin):
    dhtsensor = dht(pin)
    dhtsensor.readData()
    return(dhtsensor.getTemp(),dhtsensor.getHumid(),dhtsensor.getError())
                    
def getSensorDataInt(pin):
    dhtsensor = dht(pin)
    dhtsensor.readData()
    return((int)(dhtsensor.getTemp()),(int)(dhtsensor.getHumid()),dhtsensor.getError())
