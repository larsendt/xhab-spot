#!/usr/bin/env python

import sht
import time

t = sht.getTemperature(2,4)
print 'Reading Temperature data in float'
print 'Temperature: ' + str(t) + '*C' 


t = sht.getTemperatureInt(2,4)
print 'Reading Temperature data in int'
print 'Temperature: ' + str(t) + '*C' 

h = sht.getHumidity(2,4)
print 'Reading Humidity data in float'
print 'Humidity: ' + str(h) + '%' 


h = sht.getHumidityInt(2,4)
print 'Reading Humidity data in Int'
print 'Humidity: ' + str(h) + '%' 
    

