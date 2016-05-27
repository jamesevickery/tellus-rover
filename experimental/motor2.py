#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

number_of_motors = 2
w, h = 3, number_of_motors
motor = [[0 for x in range(w)] for y in range(h)]

GPIO.setmode(GPIO.BOARD)


def define_motors():
    '''motor[index][direction] where 0=on/off, 1=forwards, 2=backwards'''
    #motor[0] in L293D pins 3 and 6
    motor[0][0]=22 #25 #01
    motor[0][1]=16 #23 #07
    motor[0][2]=18 #24 #02
    #motor[1] in L293D pins 11 and 14
    motor[1][0]=23 #11 #09
    motor[1][1]=19 #10 #15
    motor[1][2]=21 #09 #10


def gpio_setup():
    for i1 in range(len(motor)):
        for i2 in range(len(motor[i1])):
            GPIO.setup(motor[i1][i2], GPIO.OUT)


def drive_motor(motor_index, direction=1):
    if (direction == 0):
        GPIO.output(motor[motor_index][0], GPIO.LOW)
    else:
        GPIO.output(motor[motor_index][direction], GPIO.HIGH)
        GPIO.output(motor[motor_index][direction*-1], GPIO.LOW)
        GPIO.output(motor[motor_index][0], GPIO.HIGH)



def main():
    define_motors()
    gpio_setup()
    

    
    

    
    #drive_motor(1, 1)
    #sleep(3)
    #drive_motor(1, 0)
    #sleep(3)
    #drive_motor(1, -1)
    #sleep(3)
    
    GPIO.cleanup()



main()





