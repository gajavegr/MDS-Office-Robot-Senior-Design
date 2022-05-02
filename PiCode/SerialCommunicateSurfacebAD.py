#!/usr/bin/env python3
import sys
import serial
import time
import threading

class ArduinoComm:
    def __init__(self):
        # self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.ser = serial.Serial('COM4', 9600, timeout=1)
        self.ser.reset_input_buffer()
    
    def writeData(self,data):
        # self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.ser.reset_input_buffer()
        # print(data)
        # print(str(data).encode('utf-8'))
        i = 0
        line = "BLANK"
        while i < 2:
        # while True:
            print("sending")
            self.ser.write(str(data).encode('utf-8'))
            # self.ser.write(b"hello")
            # line = self.ser.readline().decode('utf-8').rstrip()
            # line = self.ser.readline().decode('utf-8')
            time.sleep(0.1)
            # print(f"line 27 line: {line}")
            ### BREAK OUT IF WE GET SMTG####
            if len(line) > 0:
                print("received!")
            #     print(f"LINES: {line}")
            #     if "DONE" in line:
            #         print("DONE")
                break
            ### BREAK OUT IF WE GET SMTG####
            i+=1
        while (True):
            print("in while loop 2")
            lines = str(self.ser.readline().decode('utf-8').rstrip())
            print(lines)
            for line in lines:
                if "DONE" in str(line):
                    return "DONE"
        # print(f"line: {line}")
        # line = self.ser.readline().decode('utf-8').rstrip()
        # return line


if __name__ == '__main__':
    Communication = ArduinoComm()

    # data = {"x": sys.argv[1],"y":sys.argv[2]}
    # data = f"{sys.argv[1]:04}{sys.argv[2]:04}"
    x = 0
    y = 0
    z = 0
    if len(sys.argv) == 2:
        z = "1"
        print(f'Spinning {sys.argv[1]}')
        if int(sys.argv[1]) < 0:
            x = "%03d"% abs(int(sys.argv[1]))
            x = "1" + x
        else:
            x = "%04d"% int(sys.argv[1])
        x = x + "0"
        y = "00000"
    else:
        z = "0"
        if int(sys.argv[1]) < 0:
            print(sys.argv[1])
            x = "%04d"% abs(int(sys.argv[1]))
            # print(f"4 character negative x: {x}")
            x = "1" + x
            # print(f"5 character x: {x}")

        else:
            x = "%05d"% int(sys.argv[1])

        if int(sys.argv[2]) < 0:
            print(sys.argv[2])
            y = "%04d"% abs(int(sys.argv[2]))
            y = "1" + y
            # print(f"5 character y: {y}")
        else:
            y = "%05d"% int(sys.argv[2])
    
    # data = f"{x}{y}"
    data = ""+x+y+z
    print(f"data: {data}")
    # t1 = threading.Thread(target=Communication.writeData, args=(data,))
    output = Communication.writeData(data)
    # t1.start()
    print("Transmitting coordinates to Arduino...")
    print(f"Output: {output}")
    # while(True):
    #     # print("waiting for arduino")
    #     line = Communication.ser.readline().decode('utf-8').rstrip()
    #     if "DONE" in line:
    #         break

    # t1.join()