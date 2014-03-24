import lcddriver
import time

lcd=lcddriver.lcd()

lcd.lcd_print_char('X',2, 7)
lcd.lcd_print_char('-',2, 8)
lcd.lcd_print_char('H',2, 9)
lcd.lcd_print_char('A',2, 10)
lcd.lcd_print_char('B',2, 11)

lcd.lcd_print_char('2',3, 7)
lcd.lcd_print_char('0',3, 8)
lcd.lcd_print_char('1',3, 9)
lcd.lcd_print_char('4',3, 10)
lcd.lcd_print_char('!',3, 11)

lcd.lcd_cursor_placement(4,19)

