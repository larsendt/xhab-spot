import i2c_lib
from time import *
import math

PATH = "/home/xhab/data/"

# LCD Address
ADDRESS = 0x27

# commands
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

# flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

# flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

# flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

# flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00

# flags for backlight control
LCD_BACKLIGHT = 0x08
LCD_NOBACKLIGHT = 0x00

MAXCURSORPOS = 20
NUMLINES = 4

MAXHOMESELECT = 3
MAXSPOTSELECT = 9
MAXCTRLSELECT = 8
MAXMSGSELECT = 1

En = 0b00000100 # Enable bit
Rw = 0b00000010 # Read/Write bit
Rs = 0b00000001 # Register select bit

class lcd:
    #initializes objects and lcd
    def __init__(self):
        self.lcd_device = i2c_lib.i2c_device(ADDRESS)
        
        self.lcd_backlight = LCD_BACKLIGHT
        self.lcd_display_status = LCD_DISPLAYON
        self.cursorCol = 0
        self.cursorLine = 1
        self.beingServiced = 0
        self.interruptFlag = 0 # The interrupt calls twice,
                               # so we only want to call it one time.
        self.state = "HOME"
        self.selection = 1

        sleep(0.001)
        self.lcd_write(0x03)
        sleep(0.001)
        self.lcd_write(0x02)

        self.lcd_write(LCD_FUNCTIONSET | LCD_2LINE | LCD_5x8DOTS | LCD_4BITMODE)
        self.lcd_write(LCD_DISPLAYCONTROL | LCD_DISPLAYON | LCD_BLINKON)
        self.lcd_write(LCD_CLEARDISPLAY)

        self.lcd_write(LCD_CURSORSHIFT | LCD_DISPLAYMOVE)
        self.lcd_write(LCD_ENTRYMODESET | LCD_ENTRYLEFT)
        self.lcd_write(LCD_RETURNHOME)

        sleep(0.02)
        
        self.lcd_clear()
        
        sleep(2)

        self.lcd_state("SPLASH")

        sleep(3)
        self.lcd_clear()
        sleep(.5)

        self.lcd_state("HOME")
        self.lcd_cursor_move(2,19)

    # State changing function
    def lcd_state_change(self, buttons):
        
        R = not buttons[0]
        M = not buttons[1]
        L = not buttons[2]
        
        # If the button was pressed while the backlight was off, 
        # start at HOME and assume no buttons were pressed.
        if self.lcd_backlight != LCD_BACKLIGHT:
            
            self.lcd_on()
            
            self.lcd_state("HOME")
            R = 0
            M = 0
            L = 0
            
            count = 20
            okay = False
            while not okay:
                lcdON = PATH + "lcd_status.txt"
            try:
                with open(sensorPath, "w") as f:
                    f.write("1")
                okay = True
            except:
                count = count - 1
            if count < 0:
                okay = True

        
        # ********** HOME *********
        # ********** HOME *********
        # ********** HOME *********
        if state == "HOME":
            if M == 1:
                if self.selection == 1:
                    self.lcd_state("SPOT_1")
                    self.lcd_cursor_move(2,19)
                    self.selection = 1
                elif self.selection == 2:
                    self.lcd_state("CTRL_1")
                    self.lcd_cursor_move(2, 19)
                    self.selection = 1
                elif self.selection == 3:
                    self.lcd_print_string("      MESSAGES      ", 1)
                    self.lcd_print_string("No message service  ", 2)
                    self.lcd_print_string("at this time.       ", 3)
                    self.lcd_print_string("Exiting..           ", 4)
                    self.lcd_countdown_char(3)
                    self.lcd_state("HOME") # Go back
                    self.lcd_cursor_move(4, 19)
                    self.selection = 3

            elif L == 1:
                if self.cursorLine == 2:
                    self.lcd_cursor_move(4, self.cursorCol)
                    self.selection = MAXHOMESELECT
                else:
                    print(self.cursorLine)
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_cursor_move(2, 19)
                    self.selection = 1

        # ********** SPOT INFO  *********
        # ********** SPOT INFO  *********
        # ********** SPOT INFO  *********
        if state == "SPOT_1":
            if M == 1:
                if self.selection == 1:
                    self.lcd_state("WATER_LEVEL") # Water Level (3 seconds)
                    self.lcd_state("SPOT_1")
                    self.lcd_cursor_move(2, 19)
                elif self.selection == 2:
                    self.lcd_state("BATTERY_LEVEL") # Battery Level (3 seconds)
                    self.lcd_state("SPOT_1")
                    self.lcd_cursor_move(3, 19)
                elif self.selection == 3: # Plant Info (Currently Non-existent
                    self.lcd_print_string("     PLANT INFO     ", 1)
                    self.lcd_print_string("No plant info at    ", 2)
                    self.lcd_print_string("this time. Exiting..", 3)
                    self.lcd_countdown(3)
                    self.lcd_state("SPOT_1")
                    self.lcd_cursor_move(4, 19)

            elif L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("SPOT_3")
                    self.lcd_cursor_move(4, 19)
                    self.selection = MAXSPOTSELECT
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("SPOT_2")
                    self.lcd_cursor_move(2, 19)
                    self.selection = self.selection + 1

        if state == "SPOT_2":
            if M == 1:
                if self.selection == 4:
                    self.lcd_state("EC") # EC Reading (3 seconds)
                    self.lcd_state("SPOT_2")
                    self.lcd_cursor_move(2, 19)
                elif self.selection == 5:
                    self.lcd_state("PH") # pH Reading (3 seconds)
                    self.lcd_state("SPOT_2")
                    self.lcd_cursor_move(3, 19)
                elif self.selection == 6:
                    self.lcd_state("HUMIDITY") # Humidity Level (3 seconds)
                    self.lcd_state("SPOT_2")
                    self.lcd_cursor_move(4, 19)

            elif L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("SPOT_1")
                    self.lcd_cursor_move(4, 19)
                    self.selection = self.selection - 1
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("SPOT_3")
                    self.lcd_cursor_move(2, 19)
                    self.selection = self.selection + 1

        if state == "SPOT_3":
            if M == 1:
                if self.selection == 7:
                    self.lcd_state("WATER_TEMP") # Water Temp. (3 seconds)
                    self.lcd_state("SPOT_3")
                    self.lcd_cursor_move(2, 19)
                elif self.selection == 8:
                    self.lcd_state("AIR_TEMP") # Air Temp. (3 seconds)
                    self.lcd_state("SPOT_3")
                    self.lcd_cursor_move(3, 19)
                elif self.selection == 9:
                    self.lcd_state("HOME") # Go Back...
                    self.lcd_cursor_move(2, 19)
                    self.selection = 1

            elif L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("SPOT_2")
                    self.lcd_cursor_move(4, 19)
                    self.selection = self.selection - 1
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("SPOT_1")
                    self.lcd_cursor_move(2, 19)
                    self.selection = 1

        # ********** CONTROLS  *********
        # ********** CONTROLS  *********
        # ********** CONTROLS  *********
        if state == "CTRL_1":
            if M == 1:
                if self.selection == 1:
                    self.lcd_state("ROTATE_PLANT") # Rotate Plant
                    self.lcd_cursor_move(1, 19)
                    self.selection = 1
                elif self.selection == 2:
                    self.lcd_state("DOOR") # Open/Close Door
                    self.lcd_cursor_move(3, 19)
                    self.selection = 1
                elif self.selection == 3:
                    self.lcd_state("LIGHT_SETTINGS") # Light Settings
                    self.lcd_cursor_move(2, 19)
                    self.selection = 1

            elif L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("CTRL_3")
                    self.lcd_cursor_move(3, 19)
                    self.selection = MAXCTRLSELECT
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("CTRL_2")
                    self.lcd_cursor_move(2, 19)
                    self.selection = self.selection + 1

        if state == "CTRL_2":
            if M == 1:
                if self.selection == 4:
                    self.lcd_state("TAKE_PICTURE") # Take Picture
                    self.lcd_cursor_move(3, 19)
                    self.selection = 1
                elif self.selection == 5:
                    self.lcd_state("RESTART") # Restart
                    self.lcd_cursor_move(4, 19)
                    self.selection = 2
                elif self.selection == 6:
                    self.lcd_state("SHUTDOWN") # Shutdown
                    self.lcd_cursor_move(4, 19)
                    self.selection = 2

            elif L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("CTRL_1")
                    self.lcd_cursor_move(4, 19)
                    self.selection = self.selection - 1
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("CTRL_3")
                    self.lcd_cursor_move(2, 19)
                    self.selection = self.selection + 1

        if state == "CTRL_3":
            if M == 1:
                if self.selection == 7:
                    self.lcd_state("CALIBRATE_1") # Calibrate sensors
                    self.lcd_cursor_move(2, 19)
                    self.selection = 1
                elif self.selection == 8:
                    self.lcd_state("HOME") # Go Back
                    self.lcd_cursor_move(3, 19)
                    self.selection = 2

            elif L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("CTRL_2")
                    self.lcd_cursor_move(4, 19)
                    self.selection = self.selection - 1
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 3:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("CTRL_1")
                    self.lcd_cursor_move(2, 19)
                    self.selection = 1

# TODO...
        # ********** MESSAGES  *********
        # ********** MESSAGES  *********
        # ********** MESSAGES  *********
        if state == "MSG":
            if M == 1:
                if self.selection == 1:
                    self.lcd_state("HOME") # Go Back...
                    self.lcd_cursor_move(4, 19)
                    self.selection = 3

# TODO...
        if state == "PLANT_INFO_1":
            if M == 1:
                if self.selection == 4:
                    self.lcd_state("SPOT_1") # Go Back...
                    self.lcd_cursor_move(4, 19)
                    self.selection = 3

# TODO...
        if state == "PLANT_INFO_2":
            if M == 1:
                if self.selection == 4:
                    self.lcd_state("SPOT_1") # Go Back...
                    self.lcd_cursor_move(4, 19)
                    self.selection = 3
        
        if state == "ROTATE_PLANT":
            if M == 1:
                if self.selection != 4: # Rotate 90 deg. CW
                    self.lcd_clear()
                    if self.selection == 1: # Rotate 90 deg. CW
# Begin 90 deg. CW Rotation Protocol...#
                        count = 20
                        okay = False
                        success = 0
                        while not okay:
                            sensorPath = PATH + "rotate_90_cw.txt"
                            try:
                                with open(sensorPath, "w") as f:
                                    f.write("1")
                                    okay = True
                                    success = 1
                            except:
                                count = count - 1
                                if count < 0:
                                    okay = True

                    elif self.selection == 2: # Rotate 90 deg. CCW
# Begin 90 deg. CCW Rotation Protocol...#
                        count = 20
                        okay = False
                        success = 0
                        while not okay:
                            sensorPath = PATH + "rotate_90_ccw.txt"
                            try:
                                with open(sensorPath, "w") as f:
                                    f.write("1")
                                    okay = True
                                    success = 1
                            except:
                                count = count - 1
                                if count < 0:
                                    okay = True

                    elif self.selection == 3: # Rotate 180 deg.
# Begin 180 deg. CW Rotation Protocol...#
                        count = 20
                        okay = False
                        success = 0
                        while not okay:
                            sensorPath = PATH + "rotate_180.txt"
                            try:
                                with open(sensorPath, "w") as f:
                                    f.write("1")
                                    okay = True
                                    success = 1
                            except:
                                count = count - 1
                                if count < 0:
                                    okay = True

                    if success == 1:
                        self.lcd_print_string("    Rotating...    ", 2)
                    elif success == 0:
                        self.lcd_print_string("Rotation Failure...", 2)
                    self.lcd_countdown(3)
                    self.lcd_state("ROTATE_PLANT")
                    self.lcd_cursor_move(self.selection, 19)
                
                elif self.selection == 4:
                    self.lcd_state("CTRL_1") # Go Back to CTRL_1
                    self.lcd_cursor_move(2, 19)
                    self.selection = 1

            elif L == 1:
                if self.selection == 1:
                    self.lcd_cursor_move(4, 19)
                    self.selection = 4
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_cursor_move(1, 19)
                    self.selection = 1

        if state == "DOOR":
            if M == 1:
                if self.selection == 1:

# Read from file that states whether door is open (1) or closed (0). Then request door change.
                    count = 20
                    okay = False
                    success = 0
                    doorStatus = "0"
                    while not okay:
                        sensorPathStatus = PATH + "door_status.txt"
                        sensorPath = PATH + "door_change_request.txt"
                        try:
                            with open(sensorPathStatus, "r") as f:
                                doorStatus = f.read().replace("\n","")
                            with open(sensorPath, "w") as g:
                                g.write("1")
                            okay = True
                            success = 1
                        except:
                            count = count - 1
                            if count < 0:
                                okay = True
                    
                    self.lcd_clear()
                    if success == 1 and doorStatus == "1":
                        self.lcd_print_string("     Closing...     ", 2)

                    elif success == 1 and doorStatus == "0":
                        self.lcd_print_string("     Opening...     ", 2)
                    elif success == 0:
                        self.lcd_print_string("  Door Failure...   ", 2)

                    self.lcd_countdown(3)
                    self.lcd_state("CTRL_1")
                    self.lcd_cursor_move(3, 19)
                    self.selection = 2

                elif self.selection == 2:
                    self.lcd_state("CTRL_1")
                    self.lcd_cursor_move(3, 19)
                    self.selection = 2

            elif L == 1:
                if self.selection == 1:
                    self.lcd_cursor_move(4, 19)
                    self.selection = 2
                elif self.selection == 2:
                    self.lcd_cursor_move(3, 19)
                    self.selection = 1

            elif R == 1:
                if self.selection == 1:
                    self.lcd_cursor_move(4, 19)
                    self.selection = 2
                elif self.selection == 2:
                    self.lcd_cursor_move(3, 19)
                    self.selection = 1

        if state == "LIGHT_SETTINGS":
            if M == 1:
                if self.selection == 1:
                    self.lcd_state("VARY_BRIGHTNESS_1") # Vary Brightness
                    self.lcd_cursor_move(2, 19)
                    self.selection = 1
                elif self.selection == 2:
                    self.lcd_state("LED_ON_OFF_1") # Change LED on/off setting.
                    self.lcd_cursor_move(2, 19)
                    self.selection = 1
                elif self.selection == 3:
                    self.lcd_state("CTRL_1") # GO BACK
                    self.lcd_cursor_move(4, 19)
                    self.selection = 3

            elif L == 1:
                if self.cursorLine == 2:
                    self.lcd_cursor_move(4, 19)
                    self.selection = 3
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_cursor_move(2, 19)
                    self.selection = 1

        if state == "VARY_BRIGHTNESS_1":
            if M == 1:
                if self.selection == 1:
                    self.lcd_state("VARY_BRIGHTNESS") # Vary Brightness
                    self.lcd_state("VARY_BRIGHTNESS_1")
                    self.lcd_cursor_move(2, 19)
                elif self.selection == 2:
                    self.lcd_state("VARY_BRIGHTNESS")
                    self.lcd_state("VARY_BRIGHTNESS_1")
                    self.lcd_cursor_move(3, 19)
                elif self.selection == 3:
                    self.lcd_state("VARY_BRIGHTNESS")
                    self.lcd_state("VARY_BRIGHTNESS_1")
                    self.lcd_cursor_move(4, 19)

            elif L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("VARY_BRIGHTNESS_4")
                    self.lcd_cursor_move(2, 19)
                    self.selection = 10
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("VARY_BRIGHTNESS_2")
                    self.lcd_cursor_move(2, 19)
                    self.selection = self.selection + 1

        if state == "VARY_BRIGHTNESS_2":
            if M == 1:
                if self.selection == 4:
                    self.lcd_state("VARY_BRIGHTNESS") # Vary Brightness
                    self.lcd_state("VARY_BRIGHTNESS_2")
                    self.lcd_cursor_move(2, 19)
                elif self.selection == 5:
                    self.lcd_state("VARY_BRIGHTNESS")
                    self.lcd_state("VARY_BRIGHTNESS_2")
                    self.lcd_cursor_move(3, 19)
                elif self.selection == 6:
                    self.lcd_state("VARY_BRIGHTNESS")
                    self.lcd_state("VARY_BRIGHTNESS_2")
                    self.lcd_cursor_move(4, 19)

            elif L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("VARY_BRIGHTNESS_1")
                    self.lcd_cursor_move(4, 19)
                    self.selection = self.selection - 1
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("VARY_BRIGHTNESS_3")
                    self.lcd_cursor_move(2, 19)
                    self.selection = self.selection + 1

        if state == "VARY_BRIGHTNESS_3":
            if M == 1:
                if self.selection == 7:
                    self.lcd_state("VARY_BRIGHTNESS") # Vary Brightness
                    self.lcd_state("VARY_BRIGHTNESS_3")
                    self.lcd_cursor_move(2, 19)
                elif self.selection == 8:
                    self.lcd_state("VARY_BRIGHTNESS")
                    self.lcd_state("VARY_BRIGHTNESS_3")
                    self.lcd_cursor_move(3, 19)
                elif self.selection == 9:
                    self.lcd_state("VARY_BRIGHTNESS")
                    self.lcd_state("VARY_BRIGHTNESS_3")
                    self.lcd_cursor_move(4, 19)

            elif L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("VARY_BRIGHTNESS_2")
                    self.lcd_cursor_move(4, 19)
                    self.selection = self.selection - 1
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("VARY_BRIGHTNESS_4")
                    self.lcd_cursor_move(2, 19)
                    self.selection = self.selection + 1

        if state == "VARY_BRIGHTNESS_4":
            if M == 1:
                if self.selection == 10:
                    self.lcd_state("LIGHT_SETTINGS") # Go Back
                    self.lcd_cursor_move(2, 19)
                    self.selection = 1

            elif L == 1:
                self.lcd_state("VARY_BRIGHTNESS_3")
                self.lcd_cursor_move(4, 19)
                self.selection = self.selection - 1

            elif R == 1:
                self.lcd_state("VARY_BRIGHTNESS_1")
                self.lcd_cursor_move(2, 19)
                self.selection = 1

        if state == "LED_ON_OFF_1":
            if M == 1:
                if self.selection == 1:
                    self.lcd_state("LED_ON_OFF")
                    self.lcd_state("LIGHT_SETTINGS")
                    self.lcd_cursor_move(3, 19)
                    self.selection = 2
                elif self.selection == 2:
                    self.lcd_state("LED_ON_OFF")
                    self.lcd_state("LIGHT_SETTINGS")
                    self.lcd_cursor_move(3, 19)
                    self.selection = 2
                elif self.selection == 3:
                    self.lcd_state("LED_ON_OFF")
                    self.lcd_state("LIGHT_SETTINGS")
                    self.lcd_cursor_move(3, 19)
                    self.selection = 2

            elif L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("LED_ON_OFF_3")
                    self.lcd_cursor_move(2, 19)
                    self.selection = 7
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("LED_ON_OFF_2")
                    self.lcd_cursor_move(2, 19)
                    self.selection = self.selection + 1


        if state == "LED_ON_OFF_2":
            if M == 1:
                if self.selection == 4:
                    self.lcd_state("LED_ON_OFF")
                    self.lcd_state("LIGHT_SETTINGS")
                    self.lcd_cursor_move(3, 19)
                    self.selection = 2
                elif self.selection == 5:
                    self.lcd_state("LED_ON_OFF")
                    self.lcd_state("LIGHT_SETTINGS")
                    self.lcd_cursor_move(3, 19)
                    self.selection = 2
                elif self.selection == 6:
                    self.lcd_state("LED_ON_OFF")
                    self.lcd_state("LIGHT_SETTINGS")
                    self.lcd_cursor_move(3, 19)
                    self.selection = 2

            elif L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("LED_ON_OFF_1")
                    self.lcd_cursor_move(4, 19)
                    self.selection = self.selection - 1
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("LED_ON_OFF_3")
                    self.lcd_cursor_move(2, 19)
                    self.selection = self.selection + 1

        if state == "LED_ON_OFF_3":
            if M == 1:
                if self.selection == 7:
                    self.lcd_state("LIGHT_SETTINGS") # GO BACK
                    self.lcd_cursor_move(3, 19)
                    self.selection = 2

            elif L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("LED_ON_OFF_2")
                    self.lcd_cursor_move(4, 19)
                    self.selection = self.selection - 1
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 2:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("LED_ON_OFF_1")
                    self.lcd_cursor_move(2, 19)
                    self.selection = 1

        if state == "TAKE_PICTURE":
            if M == 1:
                if self.selection == 1:
                    self.lcd_clear()
# Write to file to request picture to be taken.
                    
                    count = 20
                    okay = False
                    success = 0
                    while not okay:
                        sensorPath = PATH + "take_picture_request.txt"
                        try:
                            with open(sensorPath, "w") as f:
                                f.write("1")
                            okay = True
                            success = 1
                        except:
                            count = count - 1
                            if count < 0:
                                okay = True
                    if success == 1:
                        self.lcd_print_string("  Taking Picture... ", 2)
                    elif success == 0:
                        self.lcd_print_string(" Camera Failure...  ", 2)

                    self.lcd_countdown(3)
                    self.lcd_state("CTRL_2")
                    self.lcd_cursor_move(2, 19)
                    self.selection = 4

                elif self.selection == 2:
                    self.lcd_state("CTRL_2")
                    self.lcd_cursor_move(2, 19)
                    self.selection = 4

            elif L == 1:
                if self.selection == 1:
                    self.lcd_cursor_move(4, 19)
                    self.selection = 2
                elif self.selection == 2:
                    self.lcd_cursor_move(3, 19)
                    self.selection = 1

            elif R == 1:
                if self.selection == 1:
                    self.lcd_cursor_move(4, 19)
                    self.selection = 2
                elif self.selection == 2:
                    self.lcd_cursor_move(3, 19)
                    self.selection = 1

        if state == "RESTART":
            if M == 1:
                if self.selection == 1:
                    self.lcd_clear()
                    self.lcd_print_string("    Restarting... ", 2)
                    self.lcd_countdown(3)
                    self.lcd_clear()

                    import subprocess
                    subprocess.call(["shutdown", "-r", "now"])

                elif self.selection == 2:
                    self.lcd_state("CTRL_2")
                    self.lcd_cursor_move(3, 19)
                    self.selection = 5

            elif L == 1:
                if self.selection == 1:
                    self.lcd_cursor_move(4, 19)
                    self.selection = 2
                elif self.selection == 2:
                    self.lcd_cursor_move(3, 19)
                    self.selection = 1

            elif R == 1:
                if self.selection == 1:
                    self.lcd_cursor_move(4, 19)
                    self.selection = 2
                elif self.selection == 2:
                    self.lcd_cursor_move(3, 19)
                    self.selection = 1

        if state == "SHUTDOWN":
            if M == 1:
                if self.selection == 1:
                    self.lcd_clear()
                    self.lcd_print_string("  Shutting Down...  ", 2)
                    self.lcd_countdown(3)
                    self.lcd_print_string("   Wall-E!!!!!!!!!  ", 1)
                    self.lcd_print_string("                    ", 2)
                    self.lcd_print_string("   SPOT created by  ", 3)
                    self.lcd_print_string("  CU Boulder Grads. ", 4)
                    sleep(3)
                    self.lcd_clear()

                    import subprocess
                    subprocess.call(["shutdown", "-h", "now"])

                elif self.selection == 2:
                    self.lcd_state("CTRL_2")
                    self.lcd_cursor_move(4, 19)
                    self.selection = 6

            elif L == 1:
                if self.selection == 1:
                    self.lcd_cursor_move(4, 19)
                    self.selection = 2
                elif self.selection == 2:
                    self.lcd_cursor_move(3, 19)
                    self.selection = 1

            elif R == 1:
                if self.selection == 1:
                    self.lcd_cursor_move(4, 19)
                    self.selection = 2
                elif self.selection == 2:
                    self.lcd_cursor_move(3, 19)
                    self.selection = 1

# TODO...
        if state == "CALIBRATE_1":
            if M == 1:
                if self.selection == 1:
                    self.lcd_state("EC_CALIB") # EC Calib (NOT AVAILABLE)
                    self.lcd_state("CALIBRATE_1")
                    self.lcd_cursor_move(2, 19)
                    self.selection = 1
                elif self.selection == 2:
                    self.lcd_state("PH_CALIB_SPLASH") # PH Calib
                    self.lcd_cursor_move(1, 19)
                    self.selection = 1
                elif self.selection == 3:
                    self.lcd_state("CTRL_3") # GO BACK
                    self.lcd_cursor_move(2, 19)
                    self.selection = 7

            elif L == 1:
                if self.cursorLine == 2:
                    self.lcd_cursor_move(4, 19)
                    self.selection = 3
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            elif R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_cursor_move(2, 19)
                    self.selection = 1

        if state == "EC_CALIB":
            if M == 1:
                self.lcd_state("CALIBRATE_1") # GO BACK
                self.lcd_cursor_move(2, 19)
                self.selection = 1

            elif L == 1:
                self.lcd_state("CALIBRATE_1") # GO BACK
                self.lcd_cursor_move(2, 19)
                self.selection = 1

            elif R == 1:
                self.lcd_clear()
                self.lcd_print_string("   Calibrating...  ", 2)
                self.lcd_countdown(3)

# Set to change EC Calibration Value in file somewhere.
                try:
                    EC_calib_value = 2
                    # Save to file here.
                    pass
                except:
                    pass

                self.lcd_state("CALIBRATE_1")
                self.lcd_cursor_move(2, 19)
                self.selection = 1

        if state == "PH_CALIB":
            if M == 1:
                if self.selection == 1:
                    self.lcd_clear()
                    self.lcd_print_string("   Calibrating...  ", 2)
                    self.lcd_countdown(3)

# Send Byte to pH Probe to calibrate using 4.0 pH soln.
                    
                    self.lcd_state("PH_CALIB")
                    self.lcd_cursor_move(1, 19)
                    self.selection = 1
                elif self.selection == 2:
                    self.lcd_clear()
                    self.lcd_print_string("   Calibrating...  ", 2)
                    self.lcd_countdown(3)

# Send Byte to pH Probe to calibrate using 7.0 pH soln.

                    self.lcd_state("PH_CALIB")
                    self.lcd_cursor_move(2, 19)
                    self.selection = 2
                elif self.selection == 3:
                    self.lcd_clear()
                    self.lcd_print_string("   Calibrating...  ", 2)
                    self.lcd_countdown(3)

# Send Byte to pH Probe to calibrate using 10.0 pH soln.

                    self.lcd_state("PH_CALIB")
                    self.lcd_cursor_move(3, 19)
                    self.selection = 3
                elif self.selection == 4:
                    self.lcd_state("CALIBRATE_1") # GO BACK
                    self.lcd_cursor_move(3, 19)
                    self.selection = 2

            if L == 1:
                if self.cursorLine == 1:
                    self.lcd_cursor_move(4, 19)
                    self.selection = 4
                else:
                    self.lcd_cursor_move(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            if R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_move(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_cursor_move(1, 19)
                    self.selection = 1

    # Set to the new state
    def lcd_state(self, state):
        self.state = state
        self.lcd_clear()
        if state == "SPLASH":
            self.lcd_print_string("       X-HAB!       ", 1)
            self.lcd_print_string("A project funded by ", 3)
            self.lcd_print_string("        NASA       ", 4)

        if state == "HOME":
            self.lcd_print_string("        HOME       ", 1)
            self.lcd_print_string("1. SPOT Info       ~", 2)
            self.lcd_print_string("2. Controls        ~", 3)
            self.lcd_print_string("3. Messages        ~", 4)

        if state == "SPOT_1":
            self.lcd_print_string("     SPOT INFO      ", 1)
            self.lcd_print_string("1. Water Level     ~", 2)
            self.lcd_print_string("2. Battery Level   ~", 3)
            self.lcd_print_string("3. Plant Info      ~", 4)

        if state == "SPOT_2":
            self.lcd_print_string("     SPOT INFO      ", 1)
            self.lcd_print_string("4. EC Reading      ~", 2)
            self.lcd_print_string("5. PH Reading      ~", 3)
            self.lcd_print_string("6. Humidity Level  ~", 4)

        if state == "SPOT_3":
            self.lcd_print_string("     SPOT INFO      ", 1)
            self.lcd_print_string("7. Water Temp.     ~", 2)
            self.lcd_print_string("8. Air Temp.       ~", 3)
            self.lcd_print_string("9. Go Back         ~", 4)

        if state == "CTRL_1":
            self.lcd_print_string("      CONTROLS      ", 1)
            self.lcd_print_string("1. Rotate Plant    ~", 2)
            self.lcd_print_string("2. Open/Close Door ~", 3)
            self.lcd_print_string("3. Light Settings  ~", 4)

        if state == "CTRL_2":
            self.lcd_print_string("      CONTROLS      ", 1)
            self.lcd_print_string("4. Take Picture    ~", 2)
            self.lcd_print_string("5. Restart SPOT    ~", 3)
            self.lcd_print_string("6. SHUTDOWN SPOT   ~", 4)

        if state == "CTRL_3":
            self.lcd_print_string("      CONTROLS      ", 1)
            self.lcd_print_string("7. Calib. Sensors  ~", 2)
            self.lcd_print_string("8. Go Back         ~", 3)

        if state == "MSG":
            self.lcd_print_string("      MESSAGES      ", 1)
            self.lcd_print_string("1. Go Back         ~", 2)

        if state == "WATER_LEVEL":
# Get water level reading form file. For now, assume int 0 to 4
           
            count = 20
            okay = False
            success = 0
            waterLevel = "-1"
            while not okay:
                sensorPath = PATH + "water_level.txt"
                try:
                    with open(sensorPath, "r") as f:
                        waterLevel = f.read().replace("\n","")
                        okay = True
                        success = 1
                except:
                    count = count - 1
                    if count < 0:
                        okay = True
            
            if success == 1:
                self.lcd_print_string("     WATER LEVEL    ", 1)
            if success == 1 and waterLevel == "0":
                self.lcd_print_string("||                  ", 3)
                self.lcd_print_string("      EMPTY!!!      ", 4)
            elif success == 1 and waterLevel == "1":
                self.lcd_print_string("|||||               ", 3)
                self.lcd_print_string("        LOW         ", 4)
            elif success == 1 and waterLevel == "2":
                self.lcd_print_string("||||||||||          ", 3)
                self.lcd_print_string("     HALF FULL      ", 4)
            elif success == 1 and waterLevel == "3":
                self.lcd_print_string("|||||||||||||||     ", 3)
                self.lcd_print_string("    ALMOST FULL     ", 4)
            elif success == 1 and waterLevel == "4":
                self.lcd_print_string("||||||||||||||||||| ", 3)
                self.lcd_print_string("       FULL!        ", 4)
            elif success == 0:
                self.lcd_print_string("    Water Level     ", 2)
                self.lcd_print_string("   Read Failure...  ", 3)

            self.lcd_countdown_char(3)

        if state == "BATTERY_LEVEL":
# Get battery level reading from file. Assume 0 to 100.

            count = 20
            okay = False
            success = 0
            batteryLevel = "-1"
            while not okay:
                sensorPath = PATH + "battery_level.txt"
                try:
                    with open(sensorPath, "r") as f:
                        batteryLevel = f.read().replace("\n","")
                        okay = True
                        success = 1
                except:
                    count = count - 1
                    if count < 0:
                        okay = True

            if success == 1 and int(batteryLevel) >= 0 and int(batteryLevel) <= 100: 
                self.lcd_print_string("   BATTERY LEVEL    ", 1)
                barLen = math.trunc((int(batteryLevel)*20.0)/100.0)
                print barLen
                barStr = "|"*barLen
                print barStr
                self.lcd_print_string(barStr, 3)
                self.lcd_print_string("      " + batteryLevel + "% Full      ", 4)
            else:
                self.lcd_print_string("    Battery Read    ", 2)
                self.lcd_print_string("     Failure...     ", 3)
            self.lcd_countdown_char(3)

        if state == "PLANT_INFO_1":
            self.lcd_print_string("     PLANT INFO     ", 1)
            self.lcd_print_string("1. Plant ID        ~", 2)
            self.lcd_print_string("2. Plant Type      ~", 3)
            self.lcd_print_string("3. Plant Age       ~", 4)

        if state == "PLANT_INFO_2":
            self.lcd_print_string("     PLANT INFO     ", 1)
            self.lcd_print_string("4. Go Back         ~", 2)

        if state == "EC":
# Get EC reading from file. For now, assume int 10 to 9999.
         
            count = 20
            okay = False
            success = 0
            ecReading = "-1"
            while not okay:
                sensorPath = PATH + "ec_reading.txt"
                try:
                    with open(sensorPath, "r") as f:
                        ecReading = f.read().replace("\n","") # in mS/cm
                        okay = True
                        dispStr = "     " + str(ecReading) + " uS/cm     "
                        success = 1
                except:
                    count = count - 1
                    if count < 0:
                        okay = True
            
            if success == 1 and int(ecReading) >= 0 and int(ecReading) < 1000000:
                self.lcd_print_string("     EC READING     ", 1)
                self.lcd_print_string("                    ", 2)
                self.lcd_print_string(dispStr, 3)
            else:
                self.lcd_print_string(" EC Read Failure... ", 2)

            self.lcd_countdown(3)

        if state == "PH":
# Get PH reading from file. For now, assume float with 2 point precision.
           
            count = 20
            okay = False
            success = 0
            phReading = "-1.00"
            while not okay:
                sensorPath = PATH + "ph_reading.txt"
                try:
                    with open(sensorPath, "r") as f:
                        phReading = f.read().replace("\n","")
                        okay = True
                        dispStr = "      " + phReading  + " pH     "
                        success = 1
                except:
                    count = count - 1
                    if count < 0:
                        okay = True
           
            if success == 1 and float(phReading) >= 0.0 and float(phReading) <= 14.0:
                self.lcd_print_string("     PH READING     ", 1)
                self.lcd_print_string("                    ", 2)
                self.lcd_print_string(dispStr, 3)
            else:
                self.lcd_print_string(" PH Read Failure... ", 2)
            
            self.lcd_countdown(3)

        if state == "HUMIDITY":
# Get humidity reading from file. For now, assume int value.
            
            count = 20
            okay = False
            success = 0
            while not okay:
                sensorPath = PATH + "humidity_reading.txt"
                try:
                    with open(sensorPath, "r") as f:
                        humidityReading = f.read().replace("\n","")
                        okay = True
                        dispStr = "        " + humidityReading + "%      "
                        success = 1
                except:
                    count = count - 1
                    if count < 0:
                        okay = True
            
            if success == 1 and int(humidityReading) >= 0 and int(humidityReading) <= 100:
                self.lcd_print_string("   HUMIDITY LEVEL   ", 1)
                self.lcd_print_string(dispStr, 3)
            else:
                self.lcd_print_string("    Humidity Read    ", 2)
                self.lcd_print_string("     Failure...     ", 3)

            self.lcd_countdown(3)

        if state == "WATER_TEMP":
# Get water temp. reading from file. For now, assume int in celcius.
            
            count = 20
            okay = False
            success = 0
            waterTempReadingC = "-21"
            while not okay:
                sensorPath = PATH + "water_temp_reading.txt"
                try:
                    with open(sensorPath, "r") as f:
                        waterTempReadingC = f.read().replace("\n","")
                        waterTempReadingF = str(math.trunc(9.0/5.0*int(waterTempReadingC)+32))
                        dispStrC = "     " + waterTempReadingC + " deg. C      "
                        dispStrF = "     " + waterTempReadingF + " deg. F      "
                        okay = True
                        success = 1
                except:
                    count = count - 1
                    if count < 0:
                        okay = True
            
            if success == 1 and int(waterTempReadingC) >= -20 and int(waterTempReadingC) <= 90:
                self.lcd_print_string(" WATER TEMPERATURE  ", 1)
                self.lcd_print_string(dispStrC, 3)
                self.lcd_print_string(dispStrF, 4)
            else:
                self.lcd_print_string("  Water Temperature  ", 2)
                self.lcd_print_string("   Read Failure...   ", 3)
            self.lcd_countdown_char(3)

        if state == "AIR_TEMP":
# Get air temp. reading from file. For now, assume int in celcius.
             
            count = 20
            okay = False
            success = 0
            airTempReadingC = "-21"
            while not okay:
                sensorPath = PATH + "air_temp_reading.txt"
                try:
                    with open(sensorPath, "r") as f:
                        airTempReadingC = f.read().replace("\n","")
                        airTempReadingF = str(math.trunc(9.0/5.0*int(airTempReadingC)+32))
                        dispStrC = "     " + airTempReadingC + " deg. C      "
                        dispStrF = "     " + airTempReadingF + " deg. F      "
                        okay = True
                        success = 1
                except:
                    count = count - 1
                    if count < 0:
                        okay = True
            
            if success == 1 and int(airTempReadingC) >= -20 and int(airTempReadingC) <= 90:
                self.lcd_print_string("  AIR TEMPERATURE   ", 1)
                self.lcd_print_string(dispStrC, 3)
                self.lcd_print_string(dispStrF, 4)
            else:
                self.lcd_print_string("  Air Temperature      ", 2)
                self.lcd_print_string("  Read Failure...  ", 3)
            self.lcd_countdown_char(3)

        if state == "ROTATE_PLANT":
            self.lcd_print_string("Rotate 90 deg. CW  ~", 1)
            self.lcd_print_string("Rotate 90 deg. CCW ~", 2)
            self.lcd_print_string("Rotate 180 deg.    ~", 3)
            self.lcd_print_string("Go Back            ~", 4)

        if state == "DOOR":
# Read from file that states whether door is open (1) or closed (0). Binary/Int.

            count = 20
            okay = False
            success = 0
            doorStatus = "0"
            while not okay:
                sensorPathStatus = PATH + "door_status.txt"
                try:
                    with open(sensorPathStatus, "r") as f:
                        # 1 = currently opened. 0 == currently closed.
                        doorStatus = f.read().replace("\n","")
                    okay = True
                    success = 1
                except:
                    count = count - 1
                    if count < 0:
                        okay = True

            if success == 1 and doorStatus == "0": # i.e. currently closed
                self.lcd_print_string("     Open Door?     ", 1)
                self.lcd_print_string("1. Yes             ~", 3)
                self.lcd_print_string("2. No, Go Back     ~", 4)
            elif success == 1 and doorStatus == "1": # i.e. currently open
                self.lcd_print_string("     Close Door?    ", 1)
                self.lcd_print_string("1. Yes             ~", 3)
                self.lcd_print_string("2. No, Go Back     ~", 4)
            elif success == 0: # i.e. read fail...
                self.lcd_print_string("  Open/Close Door?  ", 1)
                self.lcd_print_string("1. Yes             ~", 3)
                self.lcd_print_string("2. No, Go Back     ~", 4)

        if state == "LIGHT_SETTINGS":
            self.lcd_print_string("   LIGHT SETTINGS   ", 1)
            self.lcd_print_string("1. Vary Brightness ~", 2)
            self.lcd_print_string("2. Turn LED ON/OFF ~", 3)
            self.lcd_print_string("3. Go Back         ~", 4)

        if state == "VARY_BRIGHTNESS":
# WRITE to file that states brightness level (int 0-255) and time for that brightness level.
            
            brightnessVector = ("62", "128", "255")
            brightnessTimeVector = ("30", "120", "480")
            
            brightnessLevel = "255"
            if self.selection <= 3:
                brightnessLevel = (brightnessVector[0])
            elif self.selection >= 4 and self.selection <= 6:
                brightnessLevel = (brightnessVector[1])
            elif self.selection >= 7 and self.selection <= 9:
                brightnessLevel = (brightnessVector[2])
            
            brightnessTimeLimit = "30"
            if self.selection % 3 == 1:
                brightnessTimeLimit = (brightnessTimeVector[0])
            elif self.selection % 3 == 2:
                brightnessTimeLimit = (brightnessTimeVector[1])
            elif self.selection % 3 == 0:
                brightnessTimeLimit = (brightnessTimeVector[2])

            count = 20
            okay = False
            success = 0
            while not okay:
                sensorTimePath = PATH + "light_time_request.txt"
                sensorBrightnessPath = PATH + "light_brightness_request.txt"
                try:
                    with open(sensorTimePath, "w") as f:
                        f.write(brightnessTimeLimit)
                    with open(sensorBrightnessPath, "w") as g:
                        g.write(brightnessLevel)
                    okay = True
                    success = 1
                except:
                    count = count - 1
                    if count < 0:
                        okay = True

            if success == 1:
                self.lcd_print_string(" Brightness set to  ", 1)
                if self.selection == 1:
                    self.lcd_print_string("        LOW         ", 2)
                    self.lcd_print_string("   for 30 minutes   ", 3)
                if self.selection == 2:
                    self.lcd_print_string("        LOW         ", 2)
                    self.lcd_print_string("    for 2 hours     ", 3)
                if self.selection == 3:
                    self.lcd_print_string("        LOW         ", 2)
                    self.lcd_print_string("    for 8 hours     ", 3)

                if self.selection == 4:
                    self.lcd_print_string("       MEDIUM       ", 2)
                    self.lcd_print_string("   for 30 minutes   ", 3)
                if self.selection == 5:
                    self.lcd_print_string("       MEDIUM       ", 2)
                    self.lcd_print_string("    for 2 hours     ", 3)
                if self.selection == 6:
                    self.lcd_print_string("       MEDIUM       ", 2)
                    self.lcd_print_string("    for 8 hours     ", 3)

                if self.selection == 7:
                    self.lcd_print_string("        HIGH        ", 2)
                    self.lcd_print_string("   for 30 minutes   ", 3)
                if self.selection == 8:
                    self.lcd_print_string("        HIGH        ", 2)
                    self.lcd_print_string("    for 2 hours     ", 3)
                if self.selection == 9:
                    self.lcd_print_string("        HIGH        ", 2)
                    self.lcd_print_string("    for 8 hours     ", 3)
            
            elif success == 0:
                self.lcd_print_string("   LED Brightness   ", 2)
                self.lcd_print_string("     Failure...     ", 3)
            
            self.lcd_countdown(3)

        if state == "VARY_BRIGHTNESS_1":
            self.lcd_print_string("  BRIGHTNESS LEVEL  ", 1)
            self.lcd_print_string("1. Low (30 min.)   ~", 2)
            self.lcd_print_string("2. Low (2 hours)   ~", 3)
            self.lcd_print_string("3. Low (8 hours)   ~", 4)

        if state == "VARY_BRIGHTNESS_2":
            self.lcd_print_string("  BRIGHTNESS LEVEL  ", 1)
            self.lcd_print_string("4. Medium (30 min.)~", 2)
            self.lcd_print_string("5. Medium (2 hours)~", 3)
            self.lcd_print_string("6. Medium (8 hours)~", 4)

        if state == "VARY_BRIGHTNESS_3":
            self.lcd_print_string("  BRIGHTNESS LEVEL  ", 1)
            self.lcd_print_string("7. High (30 min.)  ~", 2)
            self.lcd_print_string("8. High (2 hours)  ~", 3)
            self.lcd_print_string("9. High (8 hours)  ~", 4)

        if state == "VARY_BRIGHTNESS_4":
            self.lcd_clear()
            self.lcd_print_string("  BRIGHTNESS LEVEL  ", 1)
            self.lcd_print_string("10. Go Back        ~", 2)

        if state == "LED_ON_OFF":
            
            brightnessTimeVector = ("30", "120", "480")
            
            brightnessLevel = "255"
            if self.selection <= 3:
                brightnessLevel = "0"
            elif self.selection >= 3 and self.selection <= 6:
                ledOffOn = "255"

            brightnessTimeLimit = "30"
            if self.selection % 3 == 1:
                brightnessTimeLimit = (brightnessTimeVector[0])
            elif self.selection % 3 == 2:
                brightnessTimeLimit = (brightnessTimeVector[1])
            elif self.selection % 3 == 0:
                brightnessTimeLimit = (brightnessTimeVector[2])

            count = 20
            okay = False
            success = 0
            while not okay:
                sensorTimePath = PATH + "light_time_request.txt"
                sensorBrightnessPath = PATH + "light_brightness_request.txt"
                try:
                    with open(sensorTimePath, "w") as f:
                        f.write(brightnessTimeLimit)
                    with open(sensorBrightnessPath, "w") as g:
                        g.write(brightnessLevel)
                    okay = True
                    success = 1
                except:
                    count = count - 1
                    if count < 0:
                        okay = True

            if success == 1:
                self.lcd_print_string("    LEDs set to     ", 1)
                if self.selection == 1:
                    self.lcd_print_string("        OFF         ", 2)
                    self.lcd_print_string("   for 30 minutes   ", 3)
                if self.selection == 2:
                    self.lcd_print_string("        OFF         ", 2)
                    self.lcd_print_string("    for 2 hours     ", 3)
                if self.selection == 3:
                    self.lcd_print_string("        OFF         ", 2)
                    self.lcd_print_string("    for 8 hours     ", 3)

                if self.selection == 4:
                    self.lcd_print_string("         ON         ", 2)
                    self.lcd_print_string("   for 30 minutes   ", 3)
                if self.selection == 5:
                    self.lcd_print_string("         ON         ", 2)
                    self.lcd_print_string("    for 2 hours     ", 3)
                if self.selection == 6:
                    self.lcd_print_string("         ON         ", 2)
                    self.lcd_print_string("    for 8 hours     ", 3)
            
            if success == 0:
                self.lcd_print_string("     LED ON/OFF     ", 2)
                self.lcd_print_string("     Failure...     ", 3)
            
            self.lcd_countdown(3)

        if state == "LED_ON_OFF_1":
            self.lcd_print_string("     LEDs ON/OFF    ", 1)
            self.lcd_print_string("1. OFF (30 min.)   ~", 2)
            self.lcd_print_string("2. OFF (2 hours)   ~", 3)
            self.lcd_print_string("3. OFF (8 hours)   ~", 4)

        if state == "LED_ON_OFF_2":
            self.lcd_print_string("     LEDs ON/OFF    ", 1)
            self.lcd_print_string("4. ON (30 min.)    ~", 2)
            self.lcd_print_string("5. ON (2 hours)    ~", 3)
            self.lcd_print_string("6. ON (8 hours)    ~", 4)

        if state == "LED_ON_OFF_3":
            self.lcd_print_string("     LEDs ON/OFF    ", 1)
            self.lcd_print_string("7. Go Back         ~", 2)

        if state == "TAKE_PICTURE":
            self.lcd_print_string("   Take Picture?    ", 1)
            self.lcd_print_string("1. Yes             ~", 3)
            self.lcd_print_string("2. No, Go Back     ~", 4)

        if state == "RESTART":
            self.lcd_print_string("  Restart System?   ", 1)
            self.lcd_print_string("1. Yes             ~", 3)
            self.lcd_print_string("2. No, Go Back     ~", 4)

        if state == "SHUTDOWN":
            self.lcd_print_string("  Shutdown System?  ", 1)
            self.lcd_print_string("1. Yes             ~", 3)
            self.lcd_print_string("2. No, Go Back     ~", 4)

# TODO...
        if state == "CALIBRATE_1":
            self.lcd_print_string(" CALIBRATE SENSORS  ", 1)
            self.lcd_print_string("1. EC Sensor       ~", 2)
            self.lcd_print_string("2. PH Sensor       ~", 3)
            self.lcd_print_string("3. Go Back         ~", 4)

        if state == "EC_CALIB":
            self.lcd_print_string("EC calibrating does ", 1)
            self.lcd_print_string("not work at this    ", 2)
            self.lcd_print_string("time. Exiting...    ", 3)
            self.lcd_countdown(3)

            #self.lcd_print_string("Place EC sensor in  ", 1)
            #self.lcd_print_string("62mS/cm soln. RIGHT ", 2)
            #self.lcd_print_string("button = calib; LEFT", 3)
            #self.lcd_print_string("button = cancel.    ", 4)

        if state == "PH_CALIB_SPLASH":
            self.lcd_print_string("Place PH sensor in  ", 1)
            self.lcd_print_string("7, 4, then 10 PH    ", 2)
            self.lcd_print_string("calibration soln... ", 3)

            self.lcd_countdown(3)

            self.lcd_print_string("See User Manual for ", 1)
            self.lcd_print_string("additional calib.   ", 2)
            self.lcd_print_string("calibration         ", 3)
            self.lcd_print_string("instructions.       ", 4)
            
            self.lcd_countdown(3)
            self.lcd_state("PH_CALIB")
        
        if state == "PH_CALIB":
            self.lcd_print_string("1. 4 PH Solution   ~", 1)
            self.lcd_print_string("2. 7 PH Solution   ~", 2)
            self.lcd_print_string("3. 10 PH Solution  ~", 3)
            self.lcd_print_string("4. Go Back         ~", 4)

    # Clears line 4 and counts down using line 4
    def lcd_countdown(self, val):
        self.lcd_print_string("                    ", 4)
        while val > 0:
            self.lcd_print_char( str(val), 4, 18)
            sleep(1)
            val = val - 1

    # Clears line 4 and counts down using line 4
    def lcd_countdown_char(self, val):
        while val > 0:
            self.lcd_print_char( str(val), 4, 18)
            sleep(1)
            val = val - 1

    # clocks EN to latch command
    def lcd_strobe(self, data):
        self.lcd_device.write_cmd(data | En | self.lcd_backlight)
        sleep(.0005)
        self.lcd_device.write_cmd(( (data & ~En) | self.lcd_backlight))
        sleep(.0003)

    def lcd_write_four_bits(self, data):
        self.lcd_device.write_cmd(data | self.lcd_backlight)
        sleep(.0002)
        self.lcd_strobe(data)

    # write a command to lcd
    def lcd_write(self, cmd, mode=0):
        self.lcd_write_four_bits(mode | (cmd & 0xF0))
        self.lcd_write_four_bits(mode | ((cmd << 4) & 0xF0))

    # put block of text function (i.e. it breaks up
    # the text for you, and cuts the text to the max text length)
    def lcd_print_long_string(self, string):
        self.lcd_clear()

        s = len(string)

        if s > MAXCURSORPOS * NUMLINES:
            string = string[0:MAXCURSORPOS * NUMLINES]
        s = MAXCURSORPOS * NUMLINES

        linesNeeded = 1
        for i in range(1, NUMLINES):
            if s > MAXCURSORPOS * linesNeeded:
                linesNeeded = linesNeeded+1

        for i in range(1, linesNeeded+1):
            if i == linesNeeded:
                self.lcd_print_string(string[MAXCURSORPOS * (i-1):s], i)
            else:
                self.lcd_print_string(string[MAXCURSORPOS * (i-1):MAXCURSORPOS * i], i)

    # This clears a specific line.
    def lcd_line_clear(self, line):
        self.cursorLine = line
        self.cursorCol = 0
        string = MAXCURSORPOS * ' '
        if line == 1:
            self.lcd_write(0x80)
            nextLineCode = 0x80
        if line == 2:
            self.lcd_write(0xC0)
            nextLineCode = 0xC0
        if line == 3:
            self.lcd_write(0x94)
            nextLineCode = 0x94
        if line == 4:
            self.lcd_write(0xD4)
            nextLineCode = 0xD4

        for char in string:
            self.lcd_write(ord(char), Rs)

        self.lcd_write(nextLineCode)

    # print char on specific line and column
    def lcd_print_char(self, character, line, column):
        self.lcd_cursor_move(line, column)
        self.lcd_write
        self.lcd_write(ord(character), Rs)
        self.cursorCol = self.cursorCol + 1
        if (self.cursorCol) % MAXCURSORPOS == 0:
            self.cursorCol = 0
            self.cursorLine = self.cursorLine + 1
            self.lcd_cursor_move(line + 1, self.cursorCol)


    # This puts the cursor to a desired line and column
    def lcd_cursor_move(self, line, column):
        # if ((self.cursorLine)-1)*20+(self.cursorCol)>(line-1)*20+column:
        self.lcd_write(LCD_RETURNHOME)
        self.cursorCol = 0
        self.cursorLine = 1
        if column > MAXCURSORPOS-1:
            column = MAXCURSORPOS-1
        if line > NUMLINES:
            line = NUMLINES

        while (((self.cursorLine) != line) or ((self.cursorCol) != column)):
            self.lcd_write(LCD_CURSORSHIFT | LCD_MOVERIGHT)
            self.cursorCol = self.cursorCol + 1
            if (self.cursorCol) % MAXCURSORPOS == 0:
                self.cursorCol = 0
                if self.cursorLine == 1:
                    self.cursorLine = 3
                elif self.cursorLine == 2:
                    self.cursorLine = 4
                elif self.cursorLine == 3:
                    self.cursorLine = 2
                elif self.cursorLine == 4:
                    self.cursorLine = 1

    # put string function
    def lcd_print_string(self, string, line):
        self.lcd_line_clear(line)
        s = len(string)

        if s > MAXCURSORPOS:
            string = string[0:MAXCURSORPOS]
            s=len(string)
        if line == 1:
            self.lcd_write(0x80)
            nextLineCode = 0xC0
        if line == 2:
            self.lcd_write(0xC0)
            nextLineCode = 0x94
        if line == 3:
            self.lcd_write(0x94)
            nextLineCode = 0xD4
        if line == 4:
            self.lcd_write(0xD4)
            nextLineCode = 0x80

        self.cursorLine = line

        for char in string:
            self.lcd_write(ord(char), Rs)
            self.cursorCol = self.cursorCol + 1

            if (self.cursorCol) % MAXCURSORPOS == 0:
                self.lcd_write(nextLineCode)
                self.cursorCol = 0
            self.cursorLine = self.cursorLine + 1

            if (self.cursorLine) % (NUMLINES + 1) == 0:
                self.cursorLine = 1

    # Turn the LCD screen.
    def lcd_off(self):
        self.lcd_backlight = LCD_NOBACKLIGHT
        self.lcd_write(LCD_DISPLAYCONTROL | LCD_DISPLAYOFF | LCD_BLINKOFF)

    # Turn the LCD screen.
    def lcd_on(self):
        self.lcd_backlight = LCD_BACKLIGHT
        self.lcd_write(LCD_DISPLAYCONTROL | LCD_DISPLAYON | LCD_BLINKON)

    # clear lcd and set to home
    def lcd_clear(self):
        self.lcd_write(LCD_CLEARDISPLAY)
        self.lcd_write(LCD_RETURNHOME)
        self.cursorCol = 0
        self.cursorLine = 1
