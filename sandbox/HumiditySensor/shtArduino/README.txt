Humidity sensor: SHT15

Datasheet: http://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/Humidity/Sensirion_Humidity_SHT1x_Datasheet_V5.pdf

Cost:
$42

link:
https://www.sparkfun.com/products/8257

SHt15 is a digital humidity sensor that outputs a fully calibrated humidity reading.
The humidity reading is actually the relative humidity relative to temperature, SHT 15 has a built-in thermometer and outputs temperature reading as well.
It uses 2-wire connection for communication that could be connected to any two digital output.

SHT15 was chosen over DHT22 sensor. DHT 22 uses a one wire bus protocol and The readings from the DHT22 sensor were unstable. SHT15 readings are stable and the readings are accurate.


Arduino library used: https://github.com/practicalarduino/SHT1x

All the necessary files can be found here.

How to port to pcduino:

1. setup the arduino environment on pcduino. Follow steps given here.

2. copy all the files found here to ~/c_enviroinment/sample folder.

3. run 'make -f Makesht'
