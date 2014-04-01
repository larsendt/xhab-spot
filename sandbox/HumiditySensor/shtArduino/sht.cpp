/**
 * ReadSHT1xValues
 *
 * Read temperature and humidity values from an SHT1x-series (SHT10,
 * SHT11, SHT15) sensor.
 *
 * Copyright 2009 Jonathan Oxer <jon@oxer.com.au>
 * www.practicalarduino.com
 */


#include <core.h>
#include <SHT1x.h>
#include <iostream>

using namespace std;

// Specify data and clock connections and instantiate SHT1x object
#define dataPin  2
#define clockPin 4
SHT1x sht1x(dataPin, clockPin);

int option;

void setup()
{
  /*
  Serial.begin(38400); // Open serial connection to report values to host
  Serial.println("Starting up");
  */

  if (argc != 4) {
    printf("usage: %s DataPin# ClockPin# temp/humidity?\n", argv[0]);
    printf(
	   "example: %s Humidity / Temperture Sensor reading read from DataPin #8 ClockPin #9\n",
	   argv[0]);
    exit(-1);
  }
  //cout << argv[1] << argv[2] << endl;
  int dPin = atoi(argv[1]);
  int cPin = atoi(argv[2]);

  option = atoi(argv[3]);
  //cout << dPin << " " << cPin <<endl;
  sht1x.setDataPin(dPin);
  sht1x.setClockPin(cPin);
  //cout<<  "data pin " << sht1x.getDataPin() << sht1x.getClockPin() <<  endl;
}

void loop()
{
  //float temp_c;
  // float temp_f;
  //float humidity;

  // Read values from the sensor
  //temp_c = sht1x.readTemperatureC();
  //temp_f = sht1x.readTemperatureF();
  //humidity = sht1x.readHumidity();

  /*
  // Print the values to the serial port
  Serial.print("Temperature: ");
  Serial.print(temp_c, DEC);
  Serial.print("C / ");
  Serial.print(temp_f, DEC);
  Serial.print("F. Humidity: ");
  Serial.print(humidity);
  Serial.println("%");
  */

  //cout << "Temperature " << temp_c <<  " C " << endl << "Humidity " << humidity << "%" << endl;
  cout << sht1x.getError();
  if(option  == 0)
    cout << "," <<  sht1x.readTemperatureC() << endl;
  else if(option == 1)
    cout << "," << sht1x.readHumidity() << endl;

  //delay(2000);
 
  exit(-1);
}
