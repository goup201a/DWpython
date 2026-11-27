from machine import Pin, PWM
import time

PERIOD = 0.01
levels = [0, 0.1, 0.3, 0.6, 0.9]
index = 0
was_pressed = False

led = Pin(4, Pin.OUT, value=0)
button = Pin(0, Pin.IN, Pin.PULL_UP)


def button_control():
    global was_pressed, index
    if button.value() == 0:
        if was_pressed == False:
            index = index + 1
            if index > 4:
                index = 0
            
    if button.value() == 0:
        was_pressed = True
    else:
        was_pressed = False


def get_ratio(index):
    ratio = levels[index]
    return ratio
    

def ratio_control(ratio):
    # global on_time, off_time
    on_time = PERIOD * ratio
    off_time = PERIOD - on_time
    return on_time, off_time
    
    
def led_control(on_time, off_time):
    # global on_time, off_time
    if on_time > 0:
        led.value(1)
        time.sleep(on_time)
    led.value(0)
    time.sleep(off_time)


while True:
    button_control()
    a = get_ratio(index)
    led_control(*ratio_control(a))