from machine import Pin, PWM
import time

ON_DUTY = 100

button = Pin(0, Pin.IN, Pin.PULL_UP)
flash = PWM(4, freq=200, duty=0)

count = 0

while True:
    if button.value() == 0:
        count += 1
        count = count % 2
        if count == 0:
            flash.duty(ON_DUTY)
        else:
            flash.duty(0)
        