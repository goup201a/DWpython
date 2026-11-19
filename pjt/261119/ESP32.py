from machine import Pin
import time

LED_PIN = 4
PERIOD = 1
RATIO = 0.5
ON = PERIOD * RATIO
OFF = PERIOD - ON

flash = Pin(LED_PIN, Pin.OUT, value=0)

while True:
    flash.value(1)
    time.sleep(ON)
    flash.value(0)
    time.sleep(OFF)