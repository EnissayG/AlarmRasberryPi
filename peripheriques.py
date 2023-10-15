import configparser
import RPi.GPIO as GPIO
from gpiozero import Button,LED
import LCD1602
import time
from evenement import Evenement
from exceptions.peripheriqueException import PeripheriqueException
global buttonState
buttonState=0


class Peripherique:
    global buttonState
    buttonState=0

    def __init__(self) -> None:
        self._LEDs = list()
        self._boutons = list()
        self._evenements = list()
        self._buzzers= list()
        self._obstacles = list()
        self._LCD1602s = list()
        
    def setup(self, fichierConfig):
        #Lecture du fichier de configuration
        config_obj = configparser.ConfigParser()

        try:
            config_obj.read(fichierConfig)
            boutonsParam = config_obj["boutons"]
            buzzersParam = config_obj["Buzzer"]
            obstaclesParam = config_obj["Obstacle"]
            LEDsParam = config_obj["LED"]

            #récupère la config des boutons
            for bouton in boutonsParam:
                self._boutons.append(Button(boutonsParam[bouton]))

            #récupère la config des LED 
            for led in LEDsParam:
                self._LEDs.append(LED(LEDsParam[led]))

            #configure le temps entre 2 clics de bouton
            for bouton in self._boutons:
                bouton.hold_time = 0.5
                
            global BuzzerPin
            BuzzerPin = int(buzzersParam['Buzzer'])
            global Rpin
            Rpin = int(LEDsParam['Rpin'])
            global Gpin
            Gpin = int(LEDsParam['Gpin'])
            global BtnPin
            BtnPin = int(boutonsParam['BtnPin'])
            
            LCD1602.init(0x27, 1)   # init(slave address, background light)
            LCD1602.write(0, 0, 'Bienvenu :) !')
            LCD1602.write(1, 1, 'SECU MOYA 1.0')
            time.sleep(2)
            LCD1602.clear()
            time.sleep(2)
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
            GPIO.setup(int(obstaclesParam['ObstaclePin']), GPIO.IN, pull_up_down=GPIO.PUD_UP)

            #GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            
            GPIO.setup(BuzzerPin, GPIO.OUT)
            GPIO.output(BuzzerPin, GPIO.HIGH)
            GPIO.setup(Rpin, GPIO.OUT)
            GPIO.setup(Gpin, GPIO.OUT)
            GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            #GPIO.add_event_detect(BtnPin, GPIO.RISING, callback=detect, bouncetime=200)

        except Exception as err:
            raise PeripheriqueException("Échec de la configuration des périphériques")
        
            
    '''def detect(chn):
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
            buttonState=0'''

    @property   
    def LCD1602s(self):
        return self._LCD1602s
    
    @property   
    def LEDs(self):
        return self._LEDs
    
    @property   
    def buzzers(self):
        return self._buzzers
    
    @property   
    def boutons(self):
        return self._boutons

    @property
    def obstacles(self):
        return self._obstacles

    @property
    def evenements(self):
        return self._evenements


                    

    def allumer_LED(self, couleur):
        self._evenements.append(Evenement(self._LEDs[couleur].pin.number, time.time()))
        self._LEDs[couleur].on()

    
        

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
            
        
