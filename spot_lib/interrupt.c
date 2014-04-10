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

#define INTERRUPT_FILE "./interrupt.txt"
#define BUTTONS_FILE "./buttons.txt"

#define MPIN12 "/sys/devices/virtual/misc/gpio/mode/gpio12"
#define MPIN4 "/sys/devices/virtual/misc/gpio/mode/gpio4"
#define MPIN13 "/sys/devices/virtual/misc/gpio/mode/gpio13"

#define PIN12 "/sys/devices/virtual/misc/gpio/pin/gpio12"
#define PIN4 "/sys/devices/virtual/misc/gpio/pin/gpio4"
#define PIN13 "/sys/devices/virtual/misc/gpio/pin/gpio13"

int main(int _argc, char **_argv) {     
    int fd;        
    int ret;        
    swIRQt swIrqCfg;        
    int swIrqNum = 0;
    FILE *interrupt_file;
    FILE *buttons_file;
    FILE *mpin12;
    FILE *mpin4;
    FILE *mpin13;
    FILE *pin12;
    FILE *pin4;
    FILE *pin13;
    char val12[2];
    char val4[2];
    char val13[2];
    int read_counter = 0;

    val12[1] = 0;
    val4[1] = 0;
    val13[1] = 0;


    /////////////////////////////////////////////////////
    //                    Set Modes
    /////////////////////////////////////////////////////
    mpin12 = fopen(MPIN12, "w");
    if(mpin12 == NULL) {
        printf("Failed to open mode file for gpio3\n");
        return 1;
    }

    fwrite("8", sizeof(char), sizeof("1"), mpin12);
    fclose(mpin12);

    mpin4 = fopen(MPIN4, "w");
    if(mpin4 == NULL) {
        printf("Failed to open mode file for gpio4\n");
        return 1;
    }

    fwrite("8", sizeof(char), sizeof("1"), mpin4);
    fclose(mpin4);

    mpin13 = fopen(MPIN13, "w");
    if(mpin13 == NULL) {
        printf("Failed to open mode file for gpio5\n");
        return 1;
    }

    fwrite("8", sizeof(char), sizeof("1"), mpin13);
    fclose(mpin13);

    /////////////////////////////////////////////////////
    //             Set the interrupt func
    /////////////////////////////////////////////////////
    
    int irqPin1Func (void) {        
        pin12 = fopen(PIN12, "r");
        if(pin12 == NULL) {
            printf("Failed to open pin file for gpio3\n");
            return 1;
        }

        pin4 = fopen(PIN4, "r");
        if(pin4 == NULL) {
            printf("Failed to open pin file for gpio4\n");
            return 1;
        }
        
        pin13 = fopen(PIN13, "r");
        if(pin13 == NULL) {
            printf("Failed to open pin file for gpio5\n");
            return 1;
        }

        fread(val12, 1, 1, pin12); 
        fread(val4, 1, 1, pin4); 
        fread(val13, 1, 1, pin13); 

        fclose(pin12);
        fclose(pin4);
        fclose(pin13);

        read_counter += 1;

        printf("(%d) read values '%c' '%c' '%c'\n", read_counter, *val12, *val4, *val13);

        interrupt_file = fopen(INTERRUPT_FILE, "w");
        if(interrupt_file == NULL) {
            printf("interrupt file is bad\n");
            return 1;
        }

        buttons_file = fopen(BUTTONS_FILE, "w");
        if(buttons_file == NULL) {
            printf("buttons file is bad\n");
            return 1;
        }

        fprintf(interrupt_file, "1");
        fprintf(buttons_file, "%c\n%c\n%c\n", *val12, *val4, *val13);

        fclose(interrupt_file);
        fclose(buttons_file);
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
    printf("interrupt listening for values\n");
    while (1) {        
    }        
}
