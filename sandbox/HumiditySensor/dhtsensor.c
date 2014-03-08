#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#inclde <sys/time.h>

#include <Python.h>
#include "gpiodriver.h"

int readDHT(int pin, float *temp, float *hum)
{
  int counter = 0;
  int lastsate = HIGH;
  int i = 0;
  int j = 0;
  int checksum = 0;
  int bitidx = 0;
  int bits[250];
  int data[100];

  //set GPIO pin to output
  gpio_set(pin,OUTPUT);
  
  gpio_write(pin, HIGH);
  usleep(500000); //500 ms
  gpio_write(pin,LOW);
  usleep(200000);

  gpio_set(pin,INPUT);
  
  data[0] = data[1] = data[2] = data[3] = data[4] = 0;
  
  //wait for pin to drop
  

  
