#!/usr/bin/env python3

import socket

s = socket.socket()

HOST = '137.112.44.139'  # The server's hostname or IP address
PORT = 12345        # The port used by the server

s.connect((HOST, PORT))

print("Received ", s.recv(1024).decode())

s.close()