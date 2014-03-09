import lcddriver
import time

# Functions:
# 
# lcd_clear() ...This clears the screen and moves the cursor to line 1, col 0
#
# lcd_on()    ... turns it on
#
# lcd_off()   ... turns it off
#
# lcd_print_char(char, line, column)
# ...This prints a single char, and moves the cursor to the right of the char
#
# lcd_print_string(str, line)
# ...This ERASES the current line, and replaces it with a specified line.
# Overflow is deleted.
#
# lcd_print_long_string(str)
# ...This clears all, and prints a block of text. Overflow is deleted.
#
# lcd_cursor_placement(line, column)
# ...This moves the cursor to the desired line and column.
#
# Notes:
# -LCD display is 20 column x 4 line. 
#  Denoted as Lines 1-4, and Columns 0-19
# -LCD current line and col position can be found using:
#  self.cursorLine
#  self.cursorCol
# -initialize a new object using 
#  self.lcddriver.lcd()
#
# Talk to MP fmi.

# initialize an lcd
lcd = lcddriver.lcd()

# Make a test string, for demonstration...
lcd.lcd_print_string("Test Str", 2)

# To turn the lcd off, do this:
# (Note that lcd_off() and lcd_on() don't clear.)
time.sleep(4)

lcd.lcd_off()
time.sleep(4)

# To turn the lcd on, do this: 
# (Note that lcd_off() and lcd_on() don't clear.)
lcd.lcd_on()
time.sleep(4)

# To display a LONG string (i.e. of ANY length), do this:
lcd.lcd_print_long_string("01234567890123456789012345678901234567890123456789012345678901234567890123456789_THIS IS CUT OFF BECAUSE IT IS MORE THAN 80 CHARACTERS")
time.sleep(4)

# To change a single line, do this:
lcd.lcd_print_string("This_will_be_cropped_at_the_end", 3)
time.sleep(4)
lcd.lcd_print_string("This is 20 in length", 4) 
# Note that the cursor goes to the next line for len(string)%20 character strings.
time.sleep(4)
lcd.lcd_print_string("This is NOT 20", 2)
time.sleep(4)

# This is how you clear the lcd screen:
lcd.lcd_clear()
time.sleep(4) 

# This is how you move the cursor to line 2 and col 6:
lcd.lcd_cursor_placement(2, 5)
time.sleep(4)

# This is how you write a character to line 2 and col 8: 
# (Note: Cursor goes to line 2 and col 8+1)
lcd.lcd_print_char('F', 2, 8)
time.sleep(4)

lcd.lcd_clear()

