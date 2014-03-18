 sudo rm /lib/arm-linux-gnueabihf/libgpiodriver.so
 gcc -shared -o libgpiodriver.so -fPIC gpiodriver.c
 sudo cp libgpiodriver.so /lib/arm-linux-gnueabihf/.
 rm -rf build
 python setup.py build
 cp build/lib.linux-armv7l-2.7/dhtsensor.so .