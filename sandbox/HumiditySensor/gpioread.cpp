#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define GPIO_MODE_PATH "/sys/devices/virtual/misc/gpio/mode/" 
#define GPIO_PIN_PATH  "/sys/devices/virtual/misc/gpio/pin/"
#define GPIO_FILENAME "gpio"

// While it seems okay to only *read* the first value from the file, you
//   seemingly must write four bytes to the file to get the I/O setting to
//   work properly. This function does that.
void writeFile(int fileID, int value)
{
  char buffer[4];  // A place to build our four-byte string.
  memset((void *)buffer, 0, sizeof(buffer)); // clear the buffer out.
  sprintf(buffer, "%c", value);
  lseek(fileID, 0, SEEK_SET);   // Make sure we're at the top of the file!
  write(fileID, buffer, sizeof(buffer));
}


// These two 'set' functions are just wrappers to the writeFile() function to
//   make the code prettier.
void setPinMode(int pinID, int mode)
{
  writeFile(pinID, mode);
}

void setPin(int pinID, int state)
{
  writeFile(pinID, state);
}


char HIGH = '1';
char LOW = '0';
int INPUT =  0;
int OUTPUT = 1;


// These arrays will become file descriptors for the 18 IO pin and mode files.
int pinMode[18];
int pinData[18];

int main(void)
{
  int i = 0;       // Loop iterator iterator

char inputBuffer = HIGH; // create and clear a buffer for data from pins

char path[256]; // nice, long buffer to hold the path name for pin access

// This first loop does four things:
//   - initialize the file descriptors for the pin mode files
//   - initialize the file descriptors for the pin data files
//   - make the pins outputs
//   - set all the pins low
for (i = 2; i < 3; i++)
  {
    // Clear the path variable...
    memset(path,0,sizeof(path));
    // ...then assemble the path variable for the current pin mode file...
    sprintf(path, "%s%s%d", GPIO_MODE_PATH, GPIO_FILENAME, i);
    // ...and create a file descriptor...
    pinMode[i] = open(path, O_RDWR);
    // ...then rinse, repeat, for the pin data files.
    memset(path,0,sizeof(path));
    sprintf(path, "%s%s%d", GPIO_PIN_PATH, GPIO_FILENAME, i);
    pinData[i] = open(path, O_RDWR); 
    // Now that we have descriptors, make the pin an output, then set it low.
    setPinMode(pinMode[i], OUTPUT);
    setPin(pinData[i], LOW);
    printf("Pin %d low\n", i);  // Print info to the command line.
  }

// Now, we're going to wait for a button connected to pin 2 to be pressed
//  before moving on with our demo.
setPinMode(pinMode[2], OUTPUT);

for (i = 0; i <= 100; i++)
  {
    if(i %2 ==  0)
       setPin(pinData[2], HIGH);
    //printf("Pin %d HIGH\n", i);
    else
      setPin(pinData[2], LOW);
    usleep(250000);  
  }
}

