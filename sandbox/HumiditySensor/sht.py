#!/usr/bin/env python
import subprocess
import time

    
class sht:
    def __init__(self,dpin,cpin):
        self.dpin = dpin
        self.cpin = cpin
        self.temp = 0
        self.humidity = 0
        self.error = -104
            
    def getTemp(self):
        return self.temp
    
    def getHumid(self):
        return self.humidity
    
    def getError(self):
        return self.error
    
    def readData(self, option):
        time.sleep(2) #make sure that read is not called within 2 seconds.
        if(self.dpin  < 0 or self.dpin > 23):
            self.error = -103
        elif(self.cpin < 0 or self.cpin > 23):
            self.error =  -103
        elif(self.dpin == self.cpin):
            self.error = -103
        else:
            cmd = './sht ' + str(self.dpin) + " " + str(self.cpin) +  " " + str(option)
            tmp = subprocess.Popen(cmd,shell = True, stdout = subprocess.PIPE)
            tmp.wait()
            out,err=tmp.communicate()
            #print out
            if(len(out.split(','))  > 0):
                if(out.split(',')[0] == '0'):#success
                    if(option == 0): #temp
                        self.temp = (float)(out.split(',')[1])
                    elif(option == 1): #humidity
                        self.humidity = (float)(out.split(',')[1])
                #else:#failure error
                if(out.split(',')[0] == ''):
                    self.error = -104
                else:
                    self.error = (int)(out.split(',')[0])
            else:
                self.error = -104
    '''            
    def readData(self):
        cont = True
        maxIteration = 10
        while(cont == True and maxIteration > 0):
            self._readData()
            if(self.error == 0):
                cont == False
            maxIteration = maxIteration - 1
    '''
           

def getTemperature(dpin,cpin):
    shtsensor = sht(dpin,cpin)
    shtsensor.readData(0)
    error = shtsensor.getError()
    if(error == 0):
        return (shtsensor.getTemp())
    else:
        return error

def getHumidity(dpin,cpin):
    shtsensor = sht(dpin,cpin)
    shtsensor.readData(1)
    error = shtsensor.getError()
    if(error == 0):
        return (shtsensor.getHumid())
    else:
        return error
   
        
def getTemperatureInt(dpin,cpin):
    shtsensor = sht(dpin,cpin)
    shtsensor.readData(0)
    error = shtsensor.getError()
    if(error == 0):
        return ((int)(round(shtsensor.getTemp())))
    else:
        return error


def getHumidityInt(dpin,cpin):
    shtsensor = sht(dpin,cpin)
    shtsensor.readData(1)
    error = shtsensor.getError()
    if(error == 0):
        return ((int)(round(shtsensor.getHumid())))
    else:
        return error
    
   
