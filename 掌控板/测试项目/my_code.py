from mpython import *
import time

oled.DispChar('Hello! 马婷', 20, 20)
oled.show()
while True:
    oled.invert(0)
    time.sleep(3)
    oled.fill(0)
    oled.DispChar('I love you!', 20, 20)
    oled.show()
    oled.invert(0)
    time.sleep(100)