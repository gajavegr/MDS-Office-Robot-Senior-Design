import socket

# ip = "137.112.45.15" # IP of Raspberry Pi
ip = "137.112.234.14" # IP of Raspberry Pi
# hostname = socket.gethostname()
# ip_address = socket.gethostbyname(hostname)

# start server
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((ip, 8080))
serv.listen(5)
print("SERVER: started")

while True:
    # establish connection
    conn, addr = serv.accept()
    from_client = ''
    print("SERVER: connection to Client established")

    while True:
        # receive data and print
        data = conn.recv(4096).decode()
        if not data: break
        from_client += data
        print("Recieved: " + from_client)

        # send message back to client
        msg = "I am SERVER"
        conn.send(msg.encode())

    # close connection and exit
    conn.close()
    break