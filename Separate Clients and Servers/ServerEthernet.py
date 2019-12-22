import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5901)) #Ip 10.0.0.1 and subnet 255.255.255.0 and the client 10.0.0.2 and tha same subnet, and put 10.0.0.1 in the connection in client633
print(socket.gethostname())
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Hey there!!!","utf-8"))
    clientsocket.close()