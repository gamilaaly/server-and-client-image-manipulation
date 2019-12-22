import  easySocket

c = easySocket.host_tcp("127.0.0.1",8888)
print("litenining")
easySocket.send_file("g.png", c)


# import base64
# image = open('g.png', 'rb')
# image_read = image.read()
# image_64_encode = base64.encodestring(image_read)
# image_64_decode = base64.decodestring(image_64_encode)
# image_result = open('d_decoded.png', 'wb') # create a writable image and write the decoding result
# image_result.write(image_64_decode)