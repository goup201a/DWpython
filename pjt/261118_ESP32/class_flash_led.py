from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
led = Pin(33, Pin.OUT, value=1)

# PWM 코드 짜보기
while True:
    flash.value(1)
    time.sleep(0.001)
    flash.value(0)
    time.sleep(0.009)