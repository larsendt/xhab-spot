#include <fcntl.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <gpiodriver.h>

int openPinMode(int pin_no)
{
  if(pin_no < 2 || pin_no > 17)
    return -2;
  else
    {
      char path[256] = {0};
      //memset(path,0,sizeof(path));
      sprintf(path,"%s%s%d",GPIO_MODE_PATH,GPIO_FILENAME,pin_no);
      return open(path,O_RDWR);
    }
}

int openPin(int pin_no)
{
  if(pin_no < 2 || pin_no > 17)
    return -2;
  else
    {
      char path[256]  = {0};
      sprintf(path,"%s%s%d",GPIO_PIN_PATH,GPIO_FILENAME,pin_no);
      return open(path,O_RDWR);
    }
}

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


int getPin(int pinID)
{
  int value = -1;
  lseek(pinID,0,SEEK_SET);
  read(pinID,&value,1);
  return value;
}
  
//set and write functions for gpio pin

void gpio_set(int pin_no,int mode)
{
  int fileid  = openPinMode(pin_no);
  if (fileid <= 0)
    printf("wrong pin");
  if(fileid > 0)
    {
      setPinMode(fileid,mode);
      close(fileid);
    }
}

void gpio_write(int pin_no,int state)
{
  int fileid = openPin(pin_no);
  if(fileid < 0)
    printf("wrong pin");
  if(fileid > 0)
    {
      setPin(fileid,state);
      close(fileid);
    }
}

int gpio_read(int pin_no)
{
  int fileid = openPin(pin_no);
  int state = -1;
  if(fileid > 0)
    {
      state =  getPin(fileid);
      close(fileid);
    }
  return state;
}
