import easySocket

s = easySocket.connect_tcp("127.0.0.1", 8899)
video = easySocket.rcv_data(s)
f= open("droprec.avi",'wb')
f.write(video)