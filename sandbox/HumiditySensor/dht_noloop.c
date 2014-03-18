// Access from ARM Running Linux

#include <stdio.h>

//#define MAXTIMINGS 100
//#define TIMEOUT 10000

extern "C"{
int readValues(int pin,float *temp, float *Humidity);
  int test(int);
}
#include <core.h>

//int dhtpin = -1;

/*
void setup() {

  if (argc != 2) {
    printf("usage: %s GPIOpin#\n", argv[0]);
    printf(
	   "example: %s 2 - Read from an DHT22 connected to GPIO #4\n",
	   argv[0]);
    exit(-1);
  }


  dhtpin = atoi(argv[1]);

  if (dhtpin <= 0) {
    printf("Please select a valid GPIO pin #\n");
    exit(-1);
  }

//printf("Using pin #%d\n", dhtpin);
} // main

void loop() {
  readDHT(type, dhtpin);
  //delay(10000);
  exit(-1);
}

#define DEBUG = true;
*/
//int bits[250], data[100];
//int bitidx = 0;

int readValues(int pin,float *temp, float *humidity) {
  //printf("Reading %d on pin %d", type, pin);
  
    int MAXTIMINGS = 100;
  //int bits[250],data[100];
  //int bitidx = 0;
  int data[100];
  int TIMEOUT = 10000;
  int counter = 0;
  int laststate = LOW;
  int j = 0;
  /*
  // Set GPIO pin to output
  // printf("Setting pin info\n");
  pinMode(pin, OUTPUT);
  //printf("after setting.\n");
 
  digitalWrite(pin, HIGH); 
 
  usleep(500000L);  // 500 ms
  digitalWrite(pin, LOW); 
  usleep(20000);
  pinMode(pin, INPUT);

  data[0] = data[1] = data[2] = data[3] = data[4] = 0;

  while (digitalRead(pin) == HIGH) {
    usleep(1);
  }
  */

  // REQUEST SAMPLE
  pinMode(pin, OUTPUT);
  
  //start the pin in high state
  digitalWrite(pin, HIGH); 
  usleep(50000L);  // 500 ms
  

  digitalWrite(pin, LOW);
  delay(20);
  digitalWrite(pin, HIGH);
  delayMicroseconds(40);
  pinMode(pin, INPUT);


  // GET ACKNOWLEDGE or TIMEOUT
  unsigned int loopCnt = TIMEOUT;
  while(digitalRead(pin) == LOW)
    //if (loopCnt-- == 0) return DHTLIB_ERROR_TIMEOUT;
    if(loopCnt-- == 0)return -1;

  loopCnt = TIMEOUT;
  while(digitalRead(pin) == HIGH)
    //if (loopCnt-- == 0) return DHTLIB_ERROR_TIMEOUT;
    if(loopCnt-- == 0) return -1;

  int i = 0;

  for (i = 0; i < MAXTIMINGS; i++) {
    counter = 0;

    while (digitalRead(pin) == laststate) {
      counter++;
      if (counter == 1000)
	break;
    }
    //printf("8");
    laststate = digitalRead(pin);
    if (counter == 1000)
      break;
    //bits[bitidx++] = counter;

    //if ((i > 3) && (i % 2 == 0)) {
      //printf("9");
    if(i % 2 != 0){
      data[j / 8] <<= 1;
      if (counter > 20)
	data[j / 8] |= 1;
      j++;
    }
  }

  /*
  int count = 0;
  for (count = 0; count < bitidx; count += 2) {
    printf("bit %d: %d\n", count, bits[count]);
    printf("bit %d: %d (%d)\n", count - 2, bits[count + 1],
	   bits[count + 1] > 200);
  
	   }*/

  if ((j >= 39)
      && (data[4] == ((data[0] + data[1] + data[2] + data[3]) & 0xFF))) {
      float f, h;
      h = data[0] * 256 + data[1];
      h /= 10;

      f = (data[2] & 0x7F) * 256 + data[3];
      f /= 10.0;
      if (data[2] & 0x80)
	f *= -1;
      *temp = f;
      *humidity = h;
      printf("Temp =  %.1f *C, Hum = %.1f %%\n", f, h);
      return 0;
    }
  else
    {
      *temp = 0;
      *temp = 0;
      printf("less data or checksum error");
    }
    return 1;

    
}

int test(int num)
{
   // REQUEST SAMPLE
  pinMode(num, OUTPUT);
  
  //start the pin in high state
  digitalWrite(num, HIGH); 
  
  usleep(1000);
  
  // GET ACKNOWLEDGE or TIMEOUT
  //  if(digitalRead(num) == HIGH)
    return num+1;
    //else
    //return num-1;
}
