#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#include "gpiodriver.h"


// These arrays will become file descriptors for the 18 IO pin and mode files.
//int pinMode[18];
//int pinData[18];

int main(void)
{
  int i = 0;       // Loop iterator iterator

  //char inputBuffer = HIGH; // create and clear a buffer for data from pins

  char path[256]; // nice, long buffer to hold the path name for pin access

// This first loop does four things:
//   - initialize the file descriptors for the pin mode files
//   - initialize the file descriptors for the pin data files
//   - make the pins outputs
//   - set all the pins low

  int pinid,modeid;
for (i = 3; i < 4; i++)
  {
    // Clear the path variable...
    memset(path,0,sizeof(path));
    // ...then assemble the path variable for the current pin mode file...
    sprintf(path, "%s%s%d", GPIO_MODE_PATH, GPIO_FILENAME, i);
    // ...and create a file descriptor...
    modeid = open(path, O_RDWR);
    // ...then rinse, repeat, for the pin data files.
    memset(path,0,sizeof(path));
    sprintf(path, "%s%s%d", GPIO_PIN_PATH, GPIO_FILENAME, i);
    pinid = open(path, O_RDWR); 
    // Now that we have descriptors, make the pin an output, then set it low.
    setPinMode(modeid, OUTPUT);
    setPin(pinid, LOW);
    printf("Pin %d low\n", i);  // Print info to the command line.
    }

  int pin = 5;
  //gpio_set(pin,OUTPUT);

// Now, we're going to wait for a button connected to pin 2 to be pressed
//  before moving on with our demo.
setPinMode(modeid, OUTPUT);

  //gpio_set(2,OUTPUT);

//int modeid = openPinMode(2);
//int pinid = openPin(2);
 
//gpio_write(pin,LOW);
 setPin(pinid,1);
//printf(" value %c \n", getPin(pinid));
for (i = 0; i <= 100; i++)
  {
    //if(gpio_read(2) ==  LOW)
      //setPin(pinData[2], HIGH);
      //gpio_write(2,1);
    //printf("Pin %d HIGH\n", i);
    //else
      //setPin(pinData[2], LOW);
      //gpio_write(2,0);

    printf(" value %c \n", getPin(pinid));
    // printf("value %c \n", gpio_read(2));
    //if(gpio_read(pin) == LOW)
      if(getPin(pinid) == LOW)
	setPin(pinid,HIGH);
      //gpio_write(pin,HIGH);
    else
      setPin(pinid,LOW);
      //gpio_write(pin,LOW);
    
    usleep(250000);  
  }


closePin(pinid);
closePin(modeid);
}
