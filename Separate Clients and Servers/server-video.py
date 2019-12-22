import  easySocket

c = easySocket.host_tcp("127.0.0.1",8899)
print("litenining")
easySocket.send_file("drop.avi", c)