import socket

#create socket object, socket is the end point of the commuinication that sets an IP and port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET referes to ipv4 and socket_stream corresponds to TCP

#Bind the socket with an IP and a port

HOST = '127.0.0.1'
PORT= 8888
s.connect((HOST,PORT))

while True:
    full_msg = ''
    while True:
        msg = s.recv(8)
        print(msg)
        if len(msg) <= 0:
            break
        full_msg += msg.decode("utf-8")
        print(full_msg)

    if len(full_msg) > 0:  #never goes into this 
        print("here")