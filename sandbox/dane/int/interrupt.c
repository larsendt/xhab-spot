#include <stdio.h> 
#include <signal.h>   
#include <stdlib.h>    
#include <inttypes.h>    
#include <sys/ioctl.h>    
#include <fcntl.h>
// sw_interrupt must be loaded if it isn't load using   
// modprobe sw_interrupt
// Data structure for defining an interrupt on the pcDuino   
typedef struct swIRQ {    
    uint8_t channel;    
    int mode;    
    int pid;    
} swIRQt,*irqSWp;
 
// Pseudo device for controlling interrupts   
static const char *swirq_dev = "/dev/swirq";
 
#define SWIRQ_START   (0x201)   
#define SWIRQ_STOP    (0x202)    
#define SWIRQ_SETPID  (0x203)    
#define SWIRQ_ENABLE  (0x204)    
#define SWIRQ_DISABLE (0x205)
 
#define SWIRQ_RISING  (0x00)   
#define SWIRQ_FALLING (0x01)    
#define SWIRQ_HIGH    (0x02)    
#define SWIRQ_LOW     (0x03)    
#define SWIRQ_CHANGE  (0x04)
 
#define SWIRQ_PIN1    (0x0)   
#define SWIRQ_PIN2    (0x1)
 
int main(int _argc, char **_argv) {   
  int fd;    
  int ret;    
  uint8_t swIrqNum = 0;    
  swIRQt swIrqCfg;    
  
  // Define ISR    
  int irqPin1Cnt = 0;    
  int irqPin1Func (void) {    
     int pid = fork();
     if(pid == 0) {
         execvp("./test.py", NULL);
     }
     else {
         printf("exec'ed ./test.py\n");
     }
  }
 
  // Attach the ISR to the USR1 signal which is triggered by the OS when the interupt is signaled.   
  signal(SIGUSR1, (void (*) (int))irqPin1Func);
 
  // Setup to use pin1 / gpio2 when the signal goes from low to high.   
  swIrqCfg.channel = SWIRQ_PIN1;    
  swIrqCfg.mode = SWIRQ_FALLING;    
  swIrqCfg.pid = getpid();    
  swIrqNum = SWIRQ_PIN1;    
  
  // Connect a file descriptor to the pseudo device used to control interrupts    
  fd = open(swirq_dev, O_RDONLY);    
  if ( fd < 0 ) {    
    printf("open swirq device fail\n");    
    exit(0);    
  }    
  
  // Disable interrupts using pin1 / gpio2    
  ret = ioctl(fd, SWIRQ_STOP, &swIrqNum);    
  if (ret < 0) {    
    printf("can't set SWIRQ_STOP\n");    
    exit(0);    
  }    
  
  // Configure pin1 / gpio2 interrupts    
  ret = ioctl(fd, SWIRQ_SETPID, &swIrqCfg);    
  if (ret < 0) {    
    printf("can't set SWIRQ_SETPID\n");    
    exit(0);    
  }    
  
  // Enable interrupts on pin1 / gpio2    
  ret = ioctl(fd, SWIRQ_START, &swIrqNum);    
  if (ret < 0) {    
    printf("can't set SWIRQ_START\n");    
    exit(0);    
  }    
  
  // Disconnect from the pseudo device    
  if (fd) close(fd);    
 
  // Loop forever. Print out the counter when the ISR has been called.    
  int oldValue = 0;    
  while (2>1) {    
    if (oldValue != irqPin1Cnt) {    
      printf("irqPin1Funct: %d\n", irqPin1Cnt);    
      oldValue = irqPin1Cnt;    
    }    
  }    
}
