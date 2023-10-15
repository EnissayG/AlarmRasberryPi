#!/usr/bin/env python3
import RPi.GPIO as GPIO
from gpiozero import Button

import LCD1602
import time
import sqlite3

conn = sqlite3.connect('intrusion.db')
cursor = conn.cursor()
BtnPin = 18
ObstaclePin = 17
Buzzer = 26
Rpin= 5
Gpin= 6
buttonState=0

def setup(pin):
    
    LCD1602.init(0x27, 1)   # init(slave address, background light)
    LCD1602.write(0, 0, 'Bienvenu :) !')
    LCD1602.write(1, 1, 'SECU MOYA 1.0')
    time.sleep(3)
    LCD1602.write(0, 0, 'Vert = Passive')
    LCD1602.write(1, 1, 'Rouge = Active')
    time.sleep(3)
    LCD1602.clear()
    LCD1602.write(0, 0, 'Cliquez pour ')
    LCD1602.write(1, 1, 'changer de mode ')
    time.sleep(3)
    LCD1602.clear()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    global BuzzerPin
    BuzzerPin = pin
    GPIO.setup(BuzzerPin, GPIO.OUT)
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.setup(Rpin, GPIO.OUT)
    GPIO.setup(Gpin, GPIO.OUT)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BtnPin, GPIO.RISING, callback=detect, bouncetime=200)

def detect(chn):
    global buttonState
    Led(GPIO.input(BtnPin))
    if(buttonState == 0):
        LCD1602.clear()
        LCD1602.write(0, 0, 'Systeme:')
        LCD1602.write(1, 1, 'active')
        buttonState=1

    elif(buttonState == 1):
        LCD1602.clear()
        LCD1602.write(0, 0, 'Systeme:')
        LCD1602.write(1, 1, 'desactive')
        buttonState=0

def on():
    GPIO.output(BuzzerPin, GPIO.LOW)

def off():
    GPIO.output(BuzzerPin, GPIO.HIGH)




def beep(x):
    on()
    time.sleep(x)
    off()
    time.sleep(x)

def light(x,y):
    GPIO.output(Rpin, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(Rpin, GPIO.LOW)
    time.sleep(y)

def Led(x):
    if x == 0:
        GPIO.output(Rpin, 1)
        GPIO.output(Gpin, 0)
    if x == 1:
        GPIO.output(Rpin, 0)
        GPIO.output(Gpin, 1)


def loop():
    
    global buttonState


    while True:
        
        time.sleep(0.1)
        
        if(buttonState==1):
            Led(1)
          
            if (0 == GPIO.input(ObstaclePin)):
                
                LCD1602.clear()
                LCD1602.write(0, 0, 'Intrusion')
                LCD1602.write(1, 1, 'Detecte!')
                time.sleep(0.8)
                LCD1602.clear()
                beep(0.5)
                beep(0.5)
                beep(0.5)
                light(0.3, 0.02)

        else:
            
            Led(0)


def destroy():
    pass
    GPIO.output(Gpin, GPIO.HIGH)       # Green led off
    GPIO.output(Rpin, GPIO.HIGH)
    GPIO.cleanup()
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()  # Release resource

if __name__ == '__main__':     # Program start from here

    setup(Buzzer)

    try:
        
        print("Bienvenue au système de sécurité 1.0")
        print("Voulez-pouvez activer et désactiver le système d'alarme en cliquant sur le boutton")
        print("Vert : Système activé // Rouge : Système désactivé")
        Led(0)
        loop()

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()



                              
                              