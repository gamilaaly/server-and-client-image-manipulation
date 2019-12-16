import socket

#create socket object, socket is the end point of the commuinication that sets an IP and port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET referes to ipv4 and socket_stream corresponds to TCP

#Bind the socket with an IP and a port
HOST = '127.0.0.1'
PORT= 8888
s.bind((HOST,PORT))
s.listen(5)  #Queue of five communications

#what happens when there is a request for communicatio
while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established!")
    clientsocket.send(bytes("welcome to the server!", "utf-8")) #sending data to client



