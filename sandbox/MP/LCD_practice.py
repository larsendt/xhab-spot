__author__ = 'skynet'


import lcddriver
from time import *
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
GPIO_TRIG = 14
GPIO_ECHO = 15

def measure():
    gpio.setup(GPIO_TRIG, gpio.OUT)
    gpio.setup(GPIO_ECHO, gpio.IN)
    gpio.output(GPIO_TRIG, False)
    time.sleep(0.5)
    gpio.output(GPIO_TRIG, True)
    time.sleep(0.00001)
    gpio.output(GPIO_TRIG, False)
    start = time.time()
    while gpio.input(GPIO_ECHO) == 0:
        start = time.time()
        while gpio.input(GPIO_ECHO) == 1:
            stop = time.time()
            elapsed = stop - start
            distance = (elapsed * 34000) / 2
            return distance

def display_measure(): distance = measure() return distance

lcd = lcddriver.lcd()
lcd.lcd_display_string("i2c/twi/spi serial", 1)
lcd.lcd_display_string("interface2004 20x4", 2)
lcd.lcd_display_string("Character LCD Module", 3)
lcd.lcd_display_string("Display Blue", 4)

sleep(15)
lcd.lcd_clear()

lcd.lcd_display_string("HCSR-04", 1)
lcd.lcd_display_string("Distance Sensor", 2)
lcd.lcd_display_string("Using Python 3.2.3", 3)
lcd.lcd_display_string("Raspi V2 512MB", 4)

sleep(10)
lcd.lcd_clear()

lcd.lcd_display_string("Please visit website", 1)
lcd.lcd_display_string("www.recantha.co.­uk/", 2)
lcd.lcd_display_string("blog/?p=4849",3)

sleep(10)
lcd.lcd_clear()

while True:
    distance = display_measure()
    lcd.lcd_display_string("Distance Measurement", 1)
    lcd.lcd_display_string("Distance : %5.1f cm" % distance, 2)