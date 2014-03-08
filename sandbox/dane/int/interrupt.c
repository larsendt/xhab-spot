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
 
#define SWIRQ_START     (0x201)     
#define SWIRQ_STOP        (0x202)        
#define SWIRQ_SETPID    (0x203)        
#define SWIRQ_ENABLE    (0x204)        
#define SWIRQ_DISABLE (0x205)
 
#define SWIRQ_RISING    (0x00)     
#define SWIRQ_FALLING (0x01)        
#define SWIRQ_HIGH        (0x02)        
#define SWIRQ_LOW         (0x03)        
#define SWIRQ_CHANGE    (0x04)
 
#define SWIRQ_PIN1        (0x0)     
#define SWIRQ_PIN2        (0x1)

#define MPIN3 "/sys/devices/virtual/misc/gpio/mode/gpio3"
#define MPIN4 "/sys/devices/virtual/misc/gpio/mode/gpio4"
#define MPIN5 "/sys/devices/virtual/misc/gpio/mode/gpio5"

#define PIN3 "/sys/devices/virtual/misc/gpio/pin/gpio3"
#define PIN4 "/sys/devices/virtual/misc/gpio/pin/gpio4"
#define PIN5 "/sys/devices/virtual/misc/gpio/pin/gpio5"

#define DATA_FNAME "/home/xhab/buttons.txt"

int main(int _argc, char **_argv) {     
    int fd;        
    int ret;        
    swIRQt swIrqCfg;        
    int swIrqNum = 0;
    FILE *datafile;
    FILE *mpin3;
    FILE *mpin4;
    FILE *mpin5;
    FILE *pin3;
    FILE *pin4;
    FILE *pin5;
    char *val3;
    char *val4;
    char *val5;

    /////////////////////////////////////////////////////
    //                    Set Modes
    /////////////////////////////////////////////////////
    mpin3 = fopen(MPIN3, "w");
    if(mpin3 == NULL) {
        printf("Failed to open mode file for gpio3\n");
        return 1;
    }

    fwrite("1", sizeof(char), sizeof("1"), mpin3);
    fclose(mpin3);

    mpin4 = fopen(MPIN4, "w");
    if(mpin4 == NULL) {
        printf("Failed to open mode file for gpio4\n");
        return 1;
    }

    fwrite("1", sizeof(char), sizeof("1"), mpin4);
    fclose(mpin4);

    mpin5 = fopen(MPIN5, "w");
    if(mpin5 == NULL) {
        printf("Failed to open mode file for gpio5\n");
        return 1;
    }

    fwrite("1", sizeof(char), sizeof("1"), mpin5);
    fclose(mpin5);

    /////////////////////////////////////////////////////
    //                Open Pin Files 
    /////////////////////////////////////////////////////
    pin3 = fopen(PIN3, "r");
    if(pin3 == NULL) {
        printf("Failed to open pin file for gpio3\n");
        return 1;
    }

    pin4 = fopen(PIN4, "r");
    if(pin4 == NULL) {
        printf("Failed to open pin file for gpio4\n");
        return 1;
    }
    
    pin5 = fopen(PIN5, "r");
    if(pin5 == NULL) {
        printf("Failed to open pin file for gpio5\n");
        return 1;
    }

    /////////////////////////////////////////////////////
    //             Set the interrupt func
    /////////////////////////////////////////////////////
    
    datafile = fopen(DATA_FNAME, "w");
    if(datafile == NULL) {
        printf("datafile bad\n");
        return 1;
    }
    fprintf(datafile, "asdf\n");
    fclose(datafile);
    
    int irqPin1Func (void) {        
        fread(val3, 1, 1, pin3); 
        fread(val4, 1, 1, pin4); 
        fread(val5, 1, 1, pin5); 

        printf("read values %c %c %c\n", *val3, *val4, *val5);
        
        datafile = fopen(DATA_FNAME, "w");
        if(datafile == NULL) {
            printf("interrupt handler failed to open datafile\n");
            return 1;
        }

        fprintf(datafile, "3: %c\n4: %c\n5: %c\n", *val3, *val4, *val5);
        fclose(datafile);
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
    while (1) {        
    }        
}
