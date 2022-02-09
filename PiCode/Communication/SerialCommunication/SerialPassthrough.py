#!/usr/bin/env python3
import curses
import serial
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


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    while True:
        ser.write(b"red!\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)

        off()
        inp = screen.getch()
        char = inp
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

        char = ""
        inp = ""