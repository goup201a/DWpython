from machine import Pin
import time

PERIOD = 0.01
levels = [0, 0.1, 0.3, 0.6, 0.9]
index = 0

flash = Pin(4, Pin.OUT, value=0)
button = Pin(0, Pin.IN, Pin.PULL_UP)

pressed = False

while True:
    if button.value() == 0:
        if not pressed:
            index = index + 1
            if index > 4:
                index = 0
                
    pressed = button.value() == 0
    RATIO = levels[index]
    on_time = PERIOD * RATIO # 켜지는 시간
    off_time = PERIOD - on_time # 전체 주기 - 켜지는 시간 = 꺼져있는 시간
    
    if on_time > 0:
        flash.value(1)
        time.sleep(on_time)
        
    flash.value(0)
    time.sleep(off_time)