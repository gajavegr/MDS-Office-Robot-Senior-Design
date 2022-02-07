#!/usr/bin/env python3
import sys
import serial
import time
import threading


class ArduinoComm:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.ser.reset_input_buffer()
    
    def writeData(self,data):
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.ser.reset_input_buffer()
        # print(data)
        # print(str(data).encode('utf-8'))
        while True:
            print("sending")
            self.ser.write(str(data).encode('utf-8'))
            # self.ser.write(b"hello")
            line = self.ser.readline().decode('utf-8').rstrip()
            time.sleep(0.1)
            if len(line) > 0:
                print("received!")
                break
        print(line)


if __name__ == '__main__':
    Communication = ArduinoComm()

    data = {"x": sys.argv[1],"y":sys.argv[2]}

    t1 = threading.Thread(target=Communication.writeData, args=(data,))
    # Communication.writeData(data)
    t1.start()
    print("Transmitting coordinates to Arduino...")

    t1.join()