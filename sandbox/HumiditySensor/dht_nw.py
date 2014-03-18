#!/usr/bin/env python

from ctypes import *
import numpy

clib = cdll.LoadLibrary("./dhtsensor.so")

#raw is python object pointing to corresponding c function

readDHT_raw = clib.readValues
test_raw = clib.test

#python function argument types

readDHT_raw.argtypes = [c_int,POINTER(c_float),POINTER(c_float)]
test_raw.argtypes = [c_int]

def readValues(pin):
    print 'here'
    rt = c_int()
    temp = c_float()
    humidity = c_float()
    rt = readDHT_raw(pin,byref(temp),byref(humidity))
    return(rt,temp,humidity)


def test(num):
    rt = c_int()
    rt = test_raw(num)
    return rt



 
