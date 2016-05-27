# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)

#GPIO 25-Pin 22 to L293D-Pin 1    On/Off
#GPIO 24-Pin 18 to L293D-Pin 2    Backwards
#GPIO 23-Pin 16 to L293D-Pin 7    Forwards
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
print ('forwards')
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
 
sleep(2)
 
print ('backwards')
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)
 
sleep(8)
 
print ('stopping')
GPIO.output(Motor1E,GPIO.LOW)
 
GPIO.cleanup()
