import tty, sys, termios

import RPi.GPIO as GPIO
import time

LED_PIN = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT,initial=GPIO.LOW)

filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
x = 0
try:
    while 1:
        x=sys.stdin.read(1)[0]
        print("You pressed", x)
        if x == " ":
            print("If condition is met")
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN,filedescriptors)