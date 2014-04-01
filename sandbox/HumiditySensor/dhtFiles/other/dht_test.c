// Access from ARM Running Linux

#include <stdio.h>

#define MAXTIMINGS 100

//#define DEBUG

#define DHT11 11
#define DHT22 22
#define AM2302 22

int readDHT(int type, int pin);
#include <core.h>

int dhtpin = -1;
int type = -1;

void setup() {
  // if (!bcm2835_init())
  //return 1;

  if (argc != 3) {
    printf("usage: %s [11|22|2302] GPIOpin#\n", argv[0]);
    printf(
	   "example: %s 2302 4 - Read from an AM2302 connected to GPIO #4\n",
	   argv[0]);
    exit(-1);
  }

  if (strcmp(argv[1], "11") == 0)
    type = DHT11;
  if (strcmp(argv[1], "22") == 0)
    type = DHT22;
  if (strcmp(argv[1], "2302") == 0)
    type = AM2302;
  if (type == 0) {
    printf("Select 11, 22, 2302 as type!\n");
    exit(-1);
  }

  dhtpin = atoi(argv[2]);

  if (dhtpin <= 0) {
    printf("Please select a valid GPIO pin #\n");
    exit(-1);
  }

  printf("Using pin #%d\n", dhtpin);
} // main

void loop() {
  readDHT(type, dhtpin);
  delay(2000);
}
#define DEBUG = true;

int bits[250], data[100];
int bitidx = 0;

int readDHT(int type, int pin) {
  printf("Reading %d on pin %d", type, pin);
  int counter = 0;
  int laststate = HIGH;
  int j = 0;

  // Set GPIO pin to output
  printf("Setting pin info\n");
  pinMode(pin, OUTPUT);
  printf("after setting.\n");
  //bcm2835_gpio_fsel(pin, BCM2835_GPIO_FSEL_OUTP);
  //printf("2\n");
  digitalWrite(pin, HIGH); // turn off LED
  // bcm2835_gpio_write(pin, HIGH);
  usleep(500000L);  // 500 ms
  //printf("3\n");
  digitalWrite(pin, LOW); // turn off LED
  //bcm2835_gpio_write(pin, LOW);
  //printf("4\n");
  usleep(20000);
  pinMode(pin, INPUT);
  //bcm2835_gpio_fsel(pin, BCM2835_GPIO_FSEL_INPT);
  //printf("5\n");
  data[0] = data[1] = data[2] = data[3] = data[4] = 0;

  // wait for pin to drop?
  //printf("6\n");
  while (digitalRead(pin) == HIGH) {
    usleep(1);
  }
  int i = 0;
  //printf("7\n");
  // read data!
  for (i = 0; i < MAXTIMINGS; i++) {
    counter = 0;
    //printf("7a\n");
    while (digitalRead(pin) == laststate) {
      //printf("8");
      counter++;
      //usleep(10);
      //nanosleep(10);// overclocking might change this?
      if (counter == 1000)
	break;
    }
    printf("8");
    laststate = digitalRead(pin);
    if (counter == 1000)
      break;
    bits[bitidx++] = counter;

    if ((i > 3) && (i % 2 == 0)) {
      printf("9");
      // shove each bit into the storage bytes
      data[j / 8] <<= 1;
      if (counter > 20)
	data[j / 8] |= 1;
      j++;
    }
  }

  int count = 3;
  for (count = 3; count < bitidx; count += 2) {
    printf("bit %d: %d\n", count - 3, bits[count]);
    printf("bit %d: %d (%d)\n", count - 2, bits[count + 1],
	   bits[count + 1] > 200);
  }

  printf("Data (%d): 0x%x 0x%x 0x%x 0x%x 0x%x\n", j, data[0], data[1],
	 data[2], data[3], data[4]);

  if ((j >= 39)
      && (data[4] == ((data[0] + data[1] + data[2] + data[3]) & 0xFF))) {
    // yay!
    if (type == DHT11)
      printf("Temp = %d *C, Hum = %d %%\n", data[2], data[0]);
    if (type == DHT22) {
      float f, h;
      h = data[0] * 256 + data[1];
      h /= 10;

      f = (data[2] & 0x7F) * 256 + data[3];
      f /= 10.0;
      if (data[2] & 0x80)
	f *= -1;
      printf("Temp =  %.1f *C, Hum = %.1f %%\n", f, h);
    }
    return 1;
  }

  return 0;
}
