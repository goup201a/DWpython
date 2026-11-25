from machine import Pin
import time

LED_PIN = 4
BUTTON_PIN = 0
ON_VALUE = 1
OFF_VALUE = 0
PRESSED_VALUE = 0
PERIOD = 0.01
levels = [0, 0.1, 0.3, 0.6, 0.9]
index = 0
was_pressed = False

led = Pin(4, Pin.OUT, value=0)
button = Pin(0, Pin.IN, Pin.PULL_UP)


def button_control():
    global index, was_pressed
    if button.value() == PRESSED_VALUE:
        if was_pressed == False:
            index = index + 1
            if index > 4:
                index = 0
                
    if button.value() == PRESSED_VALUE:
        was_pressed = True
    else:
        was_pressed = False
    
    
def ratio_control():
    global ratio, on_time, off_time, PERIOD
    ratio = levels[index]
    on_time = PERIOD * ratio
    off_time = PERIOD - on_time    

        
def led_control():
    if on_time > 0:
        led.value(1)
        time.sleep(on_time)
        
    led.value(0)
    time.sleep(off_time)


while True:
    button_control()
    ratio_control()
    led_control()