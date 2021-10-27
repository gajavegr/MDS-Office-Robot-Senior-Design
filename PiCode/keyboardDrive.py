import tty, sys, termios

import RPi.GPIO as GPIO
import time

FORWARD = 8
BACK = 10
LEFT = 3
RIGHT = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(FORWARD, GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(BACK, GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(LEFT, GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(RIGHT, GPIO.OUT,initial=GPIO.HIGH)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def forward():
    GPIO.output(FORWARD, GPIO.LOW)
    GPIO.output(BACK, GPIO.HIGH)
    GPIO.output(LEFT, GPIO.HIGH)
    GPIO.output(RIGHT, GPIO.HIGH)

def left():
    GPIO.output(FORWARD, GPIO.HIGH)
    GPIO.output(BACK, GPIO.HIGH)
    GPIO.output(LEFT, GPIO.LOW)
    GPIO.output(RIGHT, GPIO.HIGH)

def right():
    GPIO.output(FORWARD, GPIO.HIGH)
    GPIO.output(BACK, GPIO.HIGH)
    GPIO.output(LEFT, GPIO.HIGH)
    GPIO.output(RIGHT, GPIO.LOW)

def back():
    GPIO.output(FORWARD, GPIO.HIGH)
    GPIO.output(BACK, GPIO.LOW)
    GPIO.output(LEFT, GPIO.HIGH)
    GPIO.output(RIGHT, GPIO.HIGH)

    
while 1:
    char = getch()
    print("You pressed", char)
    #forward
    if(char == "w"):
        print("forward")
        forward()
    if(char == "a"):
        print("left")
        left()
    if(char == "s"):
        print("back")
        back()
    if(char == "d"):
        print("right")
        right()
    if(char == "x"):
        print("Program Ended")
        break

    char = ""

GPIO.cleanup()