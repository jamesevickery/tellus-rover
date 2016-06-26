#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

number_of_motors = 4
w, h = 3, number_of_motors
motor = [[0 for x in range(w)] for y in range(h)]

GPIO.setmode(GPIO.BOARD)


def define_motors():
    '''motor[index][direction] where 0=on/off, 1=forwards, 2=backwards'''
    
    #motor[0] in L293D A pins 3 and 6
    motor[0][0]=22 #25 #01
    motor[0][1]=16 #23 #07
    motor[0][2]=18 #24 #02
    #motor[1] in L293D A pins 11 and 14
    motor[1][0]=23 #11 #09
    motor[1][1]=19 #10 #15
    motor[1][2]=21 #09 #10
    
    #motor[2] in L293D B pins 3 and 6
    motor[2][0]=36 #16 #01
    motor[2][1]=38 #20 #07
    motor[2][2]=40 #21 #02
    #motor[3] in L293D B pins 11 and 14
    motor[3][0]=33 #13 #09
    motor[3][1]=35 #19 #15
    motor[3][2]=37 #26 #10


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


def m_all_stop():
    for motor_index, ind_motor in enumerate(motor):
        drive_motor(motor_index, 0)

def m_all_on():
    for motor_index, ind_motor in enumerate(motor):
        drive_motor(motor_index, 1)

def m_all_back():
    for motor_index, ind_motor in enumerate(motor):
        drive_motor(motor_index, -1)

def m_left_turn():
    for motor_index, ind_motor in enumerate(motor):
        if ((motor_index % 2) != 0):
            drive_motor(motor_index, 1)
        else:
            drive_motor(motor_index, 0)

def m_right_turn():
    for motor_index, ind_motor in enumerate(motor):
        if ((motor_index % 2) == 0):
            drive_motor(motor_index, 1)
        else:
            drive_motor(motor_index, 0)

def m_left_spin():
    for motor_index, ind_motor in enumerate(motor):
        if ((motor_index % 2) != 0):
            drive_motor(motor_index, 1)
        else:
            drive_motor(motor_index, -1)

def m_right_spin():
    for motor_index, ind_motor in enumerate(motor):
        if ((motor_index % 2) == 0):
            drive_motor(motor_index, 1)
        else:
            drive_motor(motor_index, -1)


def getChar():
    # figure out which function to use once, and store it in _func
    if "_func" not in getChar.__dict__:
        try:
            # for Windows-based systems
            import msvcrt # If successful, we are on Windows
            getChar._func=msvcrt.getch()

        except ImportError:
            # for POSIX-based systems (with termios & tty support)
            import tty, sys, termios # raises ImportError if unsupported

            def _ttyRead():
                fd = sys.stdin.fileno()
                oldSettings = termios.tcgetattr(fd)

                try:
                    tty.setraw(fd)
                    answer = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)

                return answer

            getChar._func=_ttyRead

    return getChar._func()



def main():
    
    define_motors()
    gpio_setup()
    
    user_in = '0'
    while(user_in != '#'):
        #print('<3 : ')
        print(user_in)
        user_in=getChar()
        if user_in=='w': m_all_on()
        if user_in=='s': m_all_back()
        if user_in=='a': m_left_spin()
        if user_in=='d': m_right_spin()
        if user_in=='q' or user_in=='e': m_all_stop()
        
    GPIO.cleanup()

try:
    main()
except:
    m_all_stop()
    GPIO.cleanup()
    print('\n\nExciting')


