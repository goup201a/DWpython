from machine import Pin, PWM

led = PWM(Pin(4), freq=200, duty=0)
button = Pin(0, Pin.IN, Pin.PULL_UP)

bright = [0, 256, 512, 767, 1023]

index = 0
previous_btn = 1 # 안눌렀을 때 


while True:
    
    current_btn = button.value() # '1'
    
    if current_btn == 0: #현재 버튼이 눌러지지 않았을 때
        if previous_btn == 1:
            #여긴 생략하고 보자 
            index = index + 1
            if index > 4:
                index = 0
            led.duty(bright[index])
            
        
    previous_btn = current_btn