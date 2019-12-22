import easySocket

s = easySocket.connect_tcp("127.0.0.1", 8888)
image = easySocket.rcv_data(s)
print(image)
f= open("grec.png",'wb')
f.write(image)