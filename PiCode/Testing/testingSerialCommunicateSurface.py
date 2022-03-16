import sys
import serial
import time
import threading

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
def write_read(x):
    arduino.write(str(x).encode('utf-8'))
    time.sleep(0.05)
    data = arduino.readline().decode('utf-8').rstrip()
    return data
while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value) # printing the value