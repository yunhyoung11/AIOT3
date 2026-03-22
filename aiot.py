from gpiozero import LED  
from time import sleep

carLedRed = 2  
carLedYellow = 3
carLedGreen = 4
humanLedRed = 20
humanLedGreen = 21

carLedRed = LED(2)           #GPIO 2번에 연결(자동차 빨간불)
carLedYellow = LED(3)        #GPIO 3번에 연결(자동차 노란불)
carLedGreen = LED(4)         #GPIO 4번에 연결(자동차 초록불)
humanLedRed = LED(20)        #GPIO 20번에 연결(보행자 빨간불)
humanLedGreen = LED(21)      #GPIO 21번에 연결(보행자 초록불)

try:
    while 1:                      #무한반복 (신호등이 계속 돌아가게 만들어줌)
        carLedRed.value = 0       #자동차 빨간불 꺼짐 
        carLedYellow.value = 0    #자동차 노란불 꺼짐 
        carLedGreen.value = 1     #자동차 초록불 켜짐 
        humanLedRed.value = 1     #보행자 빨간불 켜짐 
        humanLedGreen.value = 0   #보행자 초록불 꺼짐 
        sleep(3.0)                #3초동안 유지 
        carLedRed.value = 0
        carLedYellow.value = 1
        carLedGreen.value = 0
        humanLedRed.value = 1
        humanLedGreen.value = 0
        sleep(1.0)
        carLedRed.value = 1
        carLedYellow.value = 0
        carLedGreen.value = 0
        humanLedRed.value = 0
        humanLedGreen.value = 1
        sleep(3.0)
    
except KeyboardInterrupt:
    pass                            #프로그램 종료 

carLedRed.value = 0                 #종료 시 LED꺼짐   
carLedYellow.value = 0
carLedGreen.value = 0
humanLedRed.value = 0
humanLedGreen.value = 0
