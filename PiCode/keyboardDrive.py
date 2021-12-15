import curses

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

screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

def off():
    time.sleep(0.01)
    GPIO.output(FORWARD, GPIO.HIGH)
    GPIO.output(BACK, GPIO.HIGH)
    GPIO.output(LEFT, GPIO.HIGH)
    GPIO.output(RIGHT, GPIO.HIGH)

def forward():
    GPIO.output(FORWARD, GPIO.LOW)
    GPIO.output(BACK, GPIO.HIGH)
    GPIO.output(LEFT, GPIO.HIGH)
    GPIO.output(RIGHT, GPIO.HIGH)
    # off()

def left():
    GPIO.output(FORWARD, GPIO.HIGH)
    GPIO.output(BACK, GPIO.HIGH)
    GPIO.output(LEFT, GPIO.LOW)
    GPIO.output(RIGHT, GPIO.HIGH)
    # off()

def right():
    GPIO.output(FORWARD, GPIO.HIGH)
    GPIO.output(BACK, GPIO.HIGH)
    GPIO.output(LEFT, GPIO.HIGH)
    GPIO.output(RIGHT, GPIO.LOW)
    # off()

def back():
    GPIO.output(FORWARD, GPIO.HIGH)
    GPIO.output(BACK, GPIO.LOW)
    GPIO.output(LEFT, GPIO.HIGH)
    GPIO.output(RIGHT, GPIO.HIGH)
    # off()

while 1:
    off()
    char = screen.getch()
    # char = inp
    print("You pressed", char)
    if char == ord('q'):
        break
    elif char == curses.KEY_UP:
        print("forward")
        forward()
    elif char == curses.KEY_DOWN:
        print("back")
        back()
    elif char == curses.KEY_RIGHT:
        print("right")
        right()
    elif char == curses.KEY_LEFT:
        print("left")
        left()
    # char = ""
    # inp = ""

GPIO.cleanup()