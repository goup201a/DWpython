from machine import Pin, PWM
import time

flash = PWM(Pin(4), freq=10)
#freq: 1초에 몇번 반복하냐
#duty: 한 주기당 켜져있는 시간

while True:
    for duty in range(0, 1023, 100):
    flash.duty(duty)
    time.sleep(1)


    