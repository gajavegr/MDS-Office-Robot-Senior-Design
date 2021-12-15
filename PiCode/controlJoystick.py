import tty, sys, termios

import RPi.GPIO as GPIO
import time

yellow = 8
blue = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setup(yellow, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(blue, GPIO.OUT,initial=GPIO.LOW)

filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
x = 0
sleeptime = 4
try:
    while 1:
        print("forward")
        GPIO.output(yellow, GPIO.HIGH)
        GPIO.output(blue, GPIO.HIGH)
        # time.sleep(sleeptime)
        # print("backward")
        # GPIO.output(yellow, GPIO.LOW)
        # GPIO.output(blue, GPIO.LOW)
        # time.sleep(sleeptime)
        # print("left")
        # GPIO.output(yellow, GPIO.LOW)
        # GPIO.output(blue, GPIO.HIGH)
        # time.sleep(sleeptime)
        # print("right")
        # GPIO.output(yellow, GPIO.HIGH)
        # GPIO.output(blue, GPIO.LOW)
        # time.sleep(sleeptime)
        # GPIO.output(yellow, GPIO.LOW)
        # GPIO.output(blue, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN,filedescriptors)