
/*for usleep*/
#define _BSD_SOURCE
#define DEBUG 
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dirent.h>
#include <fcntl.h>
#include <assert.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/time.h>

#include <Python.h>
#include "gpiodriver.h"

#define MAXTIMINGS 100

int readDHT(int pin, float *temp, float *hum)
{
  int counter = 0;
  unsigned char laststate = HIGH;
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
  gpio_write(pin, LOW);
  usleep(200000);

  gpio_set(pin,INPUT);
  
  data[0] = data[1] = data[2] = data[3] = data[4] = 0;
  
  int pinID = openPin(pin);
  
  //wait for pin to drop
  //while(gpio_read(pin) == 1){
  int k = 0;
  while(getPin(pinID) == HIGH){  
  usleep(1);
  k++;
  printf(" here, %d \n",  k);
  }

  //read data
  for(i = 0; i < MAXTIMINGS; i++){
    counter = 0;
    //while(gpio_read(pin) == laststate){
    while(getPin(pinID) == laststate){
    counter++;
      //nanosleep(1)
    
      if(counter == 1000)
	{
	  printf("i is %d, counter is %d value is %c\n", i, counter,getPin(pinID));
	  break;
	}
    }
    //laststate = gpio_read(pin);
    laststate = getPin(pinID);
    if(counter == 1000)break;
#ifdef DEBUG
    bits[bitidx++] = counter;
#endif

    if((i>3) && (i % 2 == 0)) {
      //shove each bit into the storage bytes
      data[j/8] <<= 1;
      if(counter > 200)
	data[j/8] |=1;
      j++;
    }
  }


#ifdef DEBUG
  for (i=3; i<bitidx; i+=2) {
    printf("bit %d: %d\n", i-3, bits[i]);
    printf("bit %d: %d (%d)\n", i-2, bits[i+1], bits[i+1] > 200);
  }
  printf("Data (%d): 0x%x 0x%x 0x%x 0x%x 0x%x\n", j, data[0], data[1], data[2], data[3], data[4]);
#endif

  closePin(pinID);

  if(j >=39){
    checksum = (data[0] + data[1] + data[2] + data[3]) & 0xFF;
    if(data[4] == checksum){
      //checksum is valid
      *temp = (data[2] & 0x7F) * 256 + data[3];
      *temp /= 10.0;
      if(data[2] & 0x80)
	*temp *= -1;
      *hum = data[0] * 256 + data[1];
      *hum /= 10.0;
      return 0; //correct data
    }
    return -2; //invalid checksum
  }
  return -1; //insufficient data
}
	       
static PyObject *
dhtsensor_read(PyObject *self, PyObject *args)
{
  int dhtpin;
  if(!PyArg_ParseTuple(args,"i", &dhtpin))
    return NULL;
  float t,h;
  int re = readDHT(dhtpin, &t, &h);
  if(re == 0){
    return Py_BuildValue("(d,d)",t,h);
  }else if(re == -1){
    printf("sensor read failed! not enough data received\n");
  }else if(re == -2){
    printf("sensor read failed! checksum failed!\n");
  }
  return Py_BuildValue("");
}

static PyMethodDef DHTSensorMethods[] = {
  {"read",dhtsensor_read,METH_VARARGS,"temperature and humidity from sensor"},{NULL,NULL,0,NULL}
};

PyMODINIT_FUNC
initdhtsensor(void)
{
  PyObject *m;
  m = Py_InitModule("dhtsensor", DHTSensorMethods);
  if(m == NULL)
    return;
}
