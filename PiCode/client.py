#!/usr/bin/env python3

import socket

ip = "137.112.45.15" # IP of Raspberry Pi

# HOST = '137.112.44.139'  # The server's hostname or IP address
HOST = '137.112.233.12'  # The server's hostname or IP address
PORT = 8080        # The port used by the server

s.connect((HOST, PORT))
msg = ""
while True:
    newmsg = s.recv(1024).decode()
    if (newmsg is not msg):
        msg = newmsg
        print("Received ", msg)

s.close()