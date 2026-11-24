from machine import Pin, PWM
import time

flash = PWM(Pin(4), freq=1000)
#freq: 1초에 몇번 반복하냐
#duty: 한 주기당 켜져있는 시간

while True:
    for duty in range(0, 1024, 10):
        flash.duty(duty)
        time.sleep(0.01)

    for duty in range(1023, -1, -10):
        flash.duty(duty)
        time.sleep 0.01
        