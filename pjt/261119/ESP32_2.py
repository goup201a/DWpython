from machine import Pin

LED_PIN = 4
ON_VALUE = 0

led = Pin(LED_PIN, Pin.OUT, value=ON_VALUE)
