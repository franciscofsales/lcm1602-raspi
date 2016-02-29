import pylcdlib
import time
import sys

#usage :
#sudo python <String> <row>
#example :
#sudo python hello-world 2

x = sys.argv[1]
y = sys.argv[2]
print type(y)
lcd = pylcdlib.lcd(0x27,1)
time.sleep(.1)
lcd.lcd_write(0x01)
time.sleep(.1)
#lcd.lcd_puts("test\n",1)
lcd.lcd_puts(str(x),int(y))
lcd.lcd_backlight(1)
