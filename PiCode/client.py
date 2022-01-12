import socket

ip = "137.112.45.15" # IP of Raspberry Pi

# connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, 8080))
print("CLIENT: connected")

# send a message
msg = "I am CLIENT"
client.send(msg.encode())

# recive a message and print it
from_server = client.recv(4096).decode()
print("Recieved: " + from_server)

# exit
client.close()