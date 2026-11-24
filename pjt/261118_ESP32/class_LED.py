from machine import Pin
import time

#LED Port define
RED_LED = 33
FLASH_LED = 4

# LED Time Control
ON_LED = 1
OFF_LED = 2

led = Pin(FLASH_LED, Pin.OUT, value=1)

for led_cnt in range(10):
    led.value(0)
    time.sleep(ON_LED)
    led.value(1)
    time.sleep(OFF_LED)
    