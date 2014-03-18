#!/usr/bin/env python

import dht

'''
t,h,e = dummy.getSensorDataInt(2)
print 'Reading sensor data in int'
if(e == 0):
    print 'Temperature: ' + str(t) + '*C' 
    print 'Humidity: ' + str(h) + '%'
    #print 'I am awesome!!!!'
else:
    print 'Error:' + str(e)
    #print 'I am yet to be awesome'



t,h,e = dummy.getSensorData(2)
print 'Reading sensor data in float'
if(e == 0):
    print 'Temperature: ' + str(t) + '*C' 
    print 'Humidity: ' + str(h) + '%'
    #print 'I am awesome!!!!'
else:
    print 'Error:' + str(e)
    #print 'I am yet to be awesome'

t,e = dht.getTemperature(2)
print 'Reading Temperature data in float'
if(e == 0):
    print 'Temperature: ' + str(t) + '*C' 
else:
    print 'Error:' + str(e)
'''

t,e = dht.getTemperatureInt(2)
print 'Reading Temperature data in int'
if(e == 0):
    print 'Temperature: ' + str(t) + '*C' 
else:
    print 'Error:' + str(e)


h,e = dht.getHumidity(2)
print 'Reading Humidity data in float'
if(e == 0):
    print 'Humidity: ' + str(h) + '%' 
else:
    print 'Error:' + str(e)

'''
h,e = dht.getHumidityInt(2)
print 'Reading Humidity data in Int'
if(e == 0):
    print 'Humidity: ' + str(h) + '%' 
else:
    print 'Error:' + str(e)

'''    

