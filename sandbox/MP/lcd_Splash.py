import lcddriver
import time

# Initialize lcd
lcd = lcddriver.lcd()

# Start Up Screen
lcd.lcd_print_string("       X-HAB!             ", 1)
lcd.lcd_print_string("", 2)
lcd.lcd_print_string("A project funded by", 3)
lcd.lcd_print_string("        NASA       ", 4)




