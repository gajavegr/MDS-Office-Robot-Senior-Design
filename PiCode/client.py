#!/usr/bin/env python3

import socket

ip = "137.112.45.15" # IP of Raspberry Pi

HOST = '137.112.44.139'  # The server's hostname or IP address
PORT = 12345        # The port used by the server

s.connect((HOST, PORT))

print("Received ", s.recv(1024).decode())

s.close()