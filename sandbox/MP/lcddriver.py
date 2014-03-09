import i2c_lib
from time import *
import psutil

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
MAXPLANTSELECT = 7
MAXCTRLSELECT = 5
MAXMSGSELECT = 5

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

        self.lcd_print_string("       X-HAB!       ", 1)
        self.lcd_print_string("                    ", 2)
        self.lcd_print_string("A project funded by ", 3)
        self.lcd_print_string("        NASA       ", 4)
        
        sleep(2)
        self.lcd_clear()
        sleep(.5)

        self.lcd_state(self.state)
        self.lcd_cursor_placement(2,19)

    # State changing function
    def lcd_state_change(self, buttons):
        R = not buttons[0]
        M = not buttons[1]
        L = not buttons[2]
        state = self.state
        
        if state == "HOME":
            if M == 1:
                if self.selection == 1:
                    self.lcd_state("PLANT_1")
                    self.lcd_cursor_placement(2,19)
                    self.selection = 1
                if self.selection == 2:
                    self.lcd_state("CTRL")
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
                if self.selection == 3:
                    self.lcd_state("MSG")
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
            
            if L == 1:
                if self.cursorLine == 2:
                    self.lcd_cursor_placement(4, self.cursorCol)
                    self.selection = MAXHOMESELECT
                else:
                    self.lcd_cursor_placement(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1

            if R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_placement(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
        
        if state == "PLANT_1":
            if M == 1:
                if self.selection == 1:
                    self.lcd_state("HOME") # Water Level
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
                if self.selection == 2:
                    self.lcd_state("HOME") # Battery Level
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
                if self.selection == 3:
                    self.lcd_state("HOME") # EC Reading
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
            
            if L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("PLANT_3")
                    self.lcd_cursor_placement(2, 19)
                    self.selection = MAXPLANTSELECT
                else:
                    self.lcd_cursor_placement(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1
            
            if R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_placement(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("PLANT_2")
                    self.lcd_cursor_placement(2, 19)
                    self.selection = self.selection + 1

        if state == "PLANT_2":
            if M == 1:
                if self.selection == 4:
                    self.lcd_state("HOME") # pH Reading
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
                if self.selection == 5:
                    self.lcd_state("HOME") # Water Temp.
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
                if self.selection == 6:
                    self.lcd_state("HOME") # Plant info.
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
            
            if L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("PLANT_1")
                    self.lcd_cursor_placement(4, 19)
                    self.selection = self.selection - 1
                else:
                    self.lcd_cursor_placement(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1
            
            if R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_placement(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("PLANT_3")
                    self.lcd_cursor_placement(2, 19)
                    self.selection = self.selection + 1
        
        if state == "PLANT_3":
            if M == 1:
                if self.selection == 7:
                    self.lcd_state("HOME") # Go Back
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
                if self.selection == 8:
                    self.lcd_state("HOME") # Water Temp.
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
                if self.selection == 9:
                    self.lcd_state("HOME") # Plant info.
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
            
            if L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("PLANT_2")
                    self.lcd_cursor_placement(4, 19)
                    self.selection = self.selection - 1
                #else:
                #    self.lcd_cursor_placement(self.cursorLine - 1, 19)
                #    self.selection = self.selection - 1
            
            if R == 1:
                if self.cursorLine == 2:
                    self.lcd_state("PLANT_1")
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
                
              #  if self.cursorLine != 4:
              #      self.lcd_cursor_placement(self.cursorLine + 1, 19)
              #      self.selection = self.selection + 1
              #  else:
              #      self.lcd_state("PLANT_1")
              #      self.lcd_cursor_placement(2, 19)
              #      self.selection = self.selection + 1

        if state == "CTRL_1":
            if M == 1:
                if self.selection == 1:
                    self.lcd_state("HOME") # Disable LEDs
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
                if self.selection == 2:
                    self.lcd_state("HOME") # Open Enclosure
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
                if self.selection == 3:
                    self.lcd_state("HOME") # Rotate Plant
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
            
            if L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("CTRL_2")
                    self.lcd_cursor_placement(2, 19)
                    self.selection = MAXCTRLSELECT
                else:
                    self.lcd_cursor_placement(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1
            
            if R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_placement(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("CTRL_2")
                    self.lcd_cursor_placement(2, 19)
                    self.selection = self.selection + 1

        if state == "CTRL_2":
            if M == 1:
                if self.selection == 4: # Restart
                    import subprocess
                    subprocess.call(["shutdown", "-r", "now"])
                if self.selection == 5: # Shutdown
                    import subprocess
                    subprocess.call(["shutdown", "-h", "now"])
                if self.selection == 6:
                    self.lcd_state("HOME") # Go Back
                    self.lcd_cursor_placement(2, 19)
                    self.selection = 1
            
            if L == 1:
                if self.cursorLine == 2:
                    self.lcd_state("PLANT_1")
                    self.lcd_cursor_placement(4, 19)
                    self.selection = self.selection - 1
                else:
                    self.lcd_cursor_placement(self.cursorLine - 1, 19)
                    self.selection = self.selection - 1
            
            if R == 1:
                if self.cursorLine != 4:
                    self.lcd_cursor_placement(self.cursorLine + 1, 19)
                    self.selection = self.selection + 1
                else:
                    self.lcd_state("PLANT_3")
                    self.lcd_cursor_placement(2, 19)
                    self.selection = self.selection + 1
        
    # Set to the new state
    def lcd_state(self, state):
        self.state = state
        if state == "HOME":
            self.lcd_print_string("       HOME         ", 1)
            self.lcd_print_string("1. SPOT Stats      ~", 2)
            self.lcd_print_string("2. Controls        ~", 3)
            self.lcd_print_string("3. Messages        ~", 4)
            self.state = "HOME"
        if state == "PLANT_1":
            self.lcd_print_string("       PLANT        ", 1)
            self.lcd_print_string("1. Water Level     ~", 2)
            self.lcd_print_string("2. Battery Level   ~", 3)
            self.lcd_print_string("3. EC Reading      ~", 4)
            self.state = "PLANT_1"
        if state == "PLANT_2":   
            self.lcd_print_string("4. pH Reading      ~", 2)
            self.lcd_print_string("5. Water Temp.     ~", 3)
            self.lcd_print_string("6. Plant Info.     ~", 4)
            self.state = "PLANT_2"
        if state == "PLANT_3":   
            self.lcd_print_string("7. Go Back         ~", 2)
            self.lcd_print_string("                    ", 3)
            self.lcd_print_string("                    ", 4)
            self.state = "PLANT_3"
        if state == "CTRL_1":
            self.lcd_print_string("      CONTROLS      ", 1)
            self.lcd_print_string("1. Disable LEDs    ~", 2)
            self.lcd_print_string("2. Rotate Enclosure~", 3)
            self.lcd_print_string("3. Rotate Plant    ~", 4)
            self.state = "CTRL"
        if state == "CTRL_2":
            self.lcd_print_string("      CONTROLS      ", 1)
            self.lcd_print_string("4. Restart SPOT    ~", 2)
            self.lcd_print_string("5. SHUTDOWN SPOT   ~", 3)
            self.lcd_print_string("6. Go Back         ~", 4)
            self.state = "CTRL"
        if state == "MSG":
            self.lcd_print_string("      MESSAGES      ", 1)
            self.lcd_print_string("1. Test1           ~", 2)
            self.lcd_print_string("2. Test2           ~", 3)
            self.lcd_print_string("3. Test3           ~", 4)
            self.state = "MSG"

    # clocks EN to latch command
    def lcd_strobe(self, data):
        self.lcd_device.write_cmd(data | En | self.lcd_backlight)
        sleep(.0002)
        self.lcd_device.write_cmd(( (data & ~En) | self.lcd_backlight))
        sleep(.0002)   

    def lcd_write_four_bits(self, data):
        self.lcd_device.write_cmd(data | self.lcd_backlight)
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
        self.lcd_cursor_placement(line, column)
        self.lcd_write
        self.lcd_write(ord(character), Rs)
        self.cursorCol = self.cursorCol + 1
        if (self.cursorCol) % MAXCURSORPOS == 0:
            self.cursorCol = 0
            self.cursorLine = self.cursorLine + 1
            self.lcd_cursor_placement(line + 1, self.cursorCol)


    # This puts the cursor to a desired line and column
    def lcd_cursor_placement(self, line, column):
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
	        elif self.cursorLine == 3:
 		        self.cursorLine = 2
	        elif self.cursorLine == 2:
 		        self.cursorLine = 4
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

#   def lcd_HOME(self, state, button):
#       if self.state == "HOME":
#           if button == "UP":
#               if lcd.cursorLine == 4:
#                   lcd.cursor_move_position(2, 19)
#               else
#                   lcd.cursor_move_position(lcd.cursorLine+1, 19)
#           if button == "ENTER"
#               if lcd











