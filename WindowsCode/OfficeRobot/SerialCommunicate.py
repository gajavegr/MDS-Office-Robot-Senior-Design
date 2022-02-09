#!/usr/bin/env python3
import sys
import serial
import time

class ArduinoComm:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.ser.reset_input_buffer()
    
    def writeData(self,data):
        self.ser.write(str(data).encode('utf-8'))
        line = self.ser.readline().decode('utf-8').rstrip()
        print(line)


if __name__ == '__main__':
    Communication = ArduinoComm()
    print(sys.argv[1])
    print(sys.argv[1])
    # Communication.writeData(sys.argv[1])

    # while True:
    
    # time.sleep(1)