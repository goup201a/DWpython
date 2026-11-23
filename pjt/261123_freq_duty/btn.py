from machine import Pin
import time

BUTTON_PIN = 0
FLASH_PIN = 4
OFF_VALUE = 0
ON_VALUE = 1
PRESSED_VALUE =0

button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

flash = Pin(FLASH_PIN, Pin.OUT, value=OFF_VALUE)

while True:
    if button.value() == PRESSED_VALUE:
        flash.value(ON_VALUE)
    else:
        flash.value(OFF_VALUE)
    time.sleep(0.05)