
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

#define DHT22_DATA_BIT_COUNT 41

int readDHT(int pin, float *temp, float *hum)
{

  int i = 0;
  int checkSum = 0;
  
  uint8_t bitTimes[DHT22_DATA_BIT_COUNT];
  uint16_t retryCount = 0;
  uint8_t _lastHumidity,currentHumidity = 0;
  uint8_t _lastTemperature,currentTemperature = 0;
  uint8_t csPart1, csPart2, csPart3, csPart4;

  int  modeID = openPinMode(pin);
  int  pinID = openPin(pin);

  
  //set GPIO pin to output

  setPinMode(modeID,OUTPUT);
  setPin(pinID,HIGH);
  //  printf("value %c \n", getPin(pinID));
  // printf(" value written after seting high  %c \n", getPin(pinID));



// Pin needs to start HIGH, wait until it is HIGH with a timeout  
  retryCount = 0;
  do
    {
      if (retryCount > 125)
	{
	  return DHT_BUS_HUNG;
	}
      retryCount++;
      usleep(2);
    }while(getPin(pinID) == LOW);
  //usleep(200000);

  // Send the activate pulse
  
  setPin(pinID,LOW);
  usleep(10000); //1.1 ms

  setPin(pinID,HIGH); //host pulls up high
   usleep(40);// host pulls up high to wait for ack pulse
  
  //printf(" value written after sending activate pulse %c \n", getPin(pinID));
 
   // Switch back to input so pin can float
  setPinMode(modeID, INPUT);

  // Find the start of the ACK Pulse
  retryCount = 0;
  do
    {
      if (retryCount > 25) //(Spec is 20 to 40 us, 25*2 == 50 us)
	{
	  return DHT_ERROR_NOT_PRESENT;
	}
      retryCount++;
      usleep(2);
    } while(getPin(pinID) == HIGH);
  //printf(" host is pulled up for rc: %d\n", retryCount);

  
  //Find the start of sensor pull up that happens in between ack pulse
  retryCount = 0;
  do
    {
      if(retryCount > 50) //(spec says 80 us, 50 * 2  == 100 us)
	{
	  return DHT_ERROR_ACK_TOO_LONG;
	}
      retryCount++;
      usleep(2);
    }while(getPin(pinID) == LOW);
  //printf(" sensor ack pull down for rc: %d\n", retryCount);
	  
  // Find the end of the ACK Pulse
  retryCount = 0;
  do
    {
      if (retryCount > 50) //(Spec is 80 us, 50*2 == 100 us)
	{
	  return DHT_ERROR_ACK_TOO_LONG;
	}
      retryCount++;
      usleep(2);
    } while(getPin(pinID) == HIGH);
  //printf(" sensor pull up low for ack for rc : %d\n", retryCount);

 
  // Read the 40 bit data stream
  for(i = 0; i < DHT22_DATA_BIT_COUNT; i++)
    {
      // Find the start of the sync pulse
      retryCount = 0;
    do
      {
	if (retryCount > 35) //(Spec is 50 us, 35*2 == 70 us)
	  {
	    return DHT_ERROR_SYNC_TIMEOUT;
	  }
	retryCount++;
	usleep(2);
      } while(getPin(pinID) == LOW);
    // Measure the width of the data pulse
    retryCount = 0;
    do
      {
	if (retryCount > 50) //(Spec is 80 us, 50*2 == 100 us)
	  {
	    return DHT_ERROR_DATA_TIMEOUT;
	  }
	retryCount++;
	printf(" i: %d and rc : %d \n", i, retryCount);
	usleep(2);
      } while(getPin(pinID) == HIGH);
    bitTimes[i] = retryCount;
  }

  closePin(pinID);
  closePin(modeID);

  // Now bitTimes have the number of retries (us *2)
  // that were needed to find the end of each data bit
  // Spec: 0 is 26 to 28 us
  // Spec: 1 is 70 us
  // bitTimes[x] <= 11 is a 0
  // bitTimes[x] >  11 is a 1
  // Note: the bits are offset by one from the data sheet, not sure why
  for(i = 0; i < 16; i++)
    {
      if(bitTimes[i + 1] > 11)
	{
	  currentHumidity |= (1 << (15 - i));
	}
    }
  for(i = 0; i < 16; i++)
    {
      if(bitTimes[i + 17] > 11)
	{
	  currentTemperature |= (1 << (15 - i));
	}
    }
  for(i = 0; i < 8; i++)
    {
      if(bitTimes[i + 33] > 11)
	{
	  checkSum |= (1 << (7 - i));
	}
    }


  _lastHumidity = currentHumidity & 0x7FFF;
  
  if(currentTemperature & 0x8000)
    {
      // Below zero, non standard way of encoding negative numbers!
      // Convert to native negative format.
      _lastTemperature = -currentTemperature & 0x7FFF;
    }
  else
    {
      _lastTemperature = currentTemperature;
    }

  csPart1 = currentHumidity >> 8;
  csPart2 = currentHumidity & 0xFF;
  csPart3 = currentTemperature >> 8;
  csPart4 = currentTemperature & 0xFF;
  if(checkSum == ((csPart1 + csPart2 + csPart3 + csPart4) & 0xFF))
    {
      *temp = (float)_lastTemperature/10.0;
      *hum = (float)_lastHumidity/10.0;
      return DHT_ERROR_NONE;
    }
  return DHT_ERROR_CHECKSUM;
}


/*python wrapper support functions*/ 
static PyObject *
dhtsensor_read(PyObject *self, PyObject *args)
{
  int dhtpin;
  if(!PyArg_ParseTuple(args,"i", &dhtpin))
    return NULL;
  float t,h;
  int re = readDHT(dhtpin, &t, &h);
  if(re == DHT_ERROR_NONE){
    return Py_BuildValue("(d,d)",t,h);
  }else if(re == DHT_BUS_HUNG){
    printf("sensor error: bus hung \n");
  }else if(re == DHT_ERROR_NOT_PRESENT){
    printf("sensor error: ACK not present\n");
  }else if(re == DHT_ERROR_ACK_TOO_LONG){
    printf("sensor error: ACk too long\n");
  }else if(re == DHT_ERROR_SYNC_TIMEOUT){
    printf("sensor error: sync timeout\n");
  }else if(re == DHT_ERROR_DATA_TIMEOUT){
    printf("sensor error: Data timeout\n");
  }else if(re == DHT_ERROR_CHECKSUM){
    printf("sensor error: checksum incorrect\n");
  }else{
    printf("sensor error: too quick request\n");
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
