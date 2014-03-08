Build dependencies for dhtreader python library
 1. python-dev

Run the following to build the library
python setup.py build

After that you should be able to find a dhtsensor.so file inside build directory. Put that library file in the same directory with your python script, then you are good to go.

Usage example:
==============
import dhtsensor
pin = 5
print dhtsensor.read(pin)

