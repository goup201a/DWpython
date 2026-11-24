from machine import Pin, PWM
import time

#freq: 1초에 몇번 반복하냐 -> 깜빡이는게 빠를수록 깜빡이지 않고 밝아진 것 처럼 보임
#duty: 한 주기당 켜져있는 시간 (해상도)

flash = PWM(Pin(4), freq=1000)

sleep = 0.01
max = 1023
step = 10

while True:
    for duty in range(0, max+1, step):
        flash.duty(duty)
        time.sleep(sleep)
        # 대기시키기

    for duty in range(max, 0, -step):
        flash.duty(duty)
        time.sleep(sleep)        