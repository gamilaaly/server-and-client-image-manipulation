import socket
import time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QSizePolicy
from MyServer import Ui_MainWindow
import sys
import easySocket
from PyQt5.QtGui import QPixmap
import shutil
import app
import ImgToVideo

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global HEADERSIZE
        HEADERSIZE = 10
        self.ui.listenButton.clicked.connect(self.listen)
        print("heey before listen")
        global server_socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('', 12445))

    def listen(self):
        # This makes server listen to new connections
        server_socket.listen()
        print("listening ....")

        while True:
            # now our endpoint knows about the OTHER endpoint.
            clientsocket, address = server_socket.accept()
            print(f"Connection from {address} has been established.")
            while True:
                full_msg = ''
                new_msg = True
                msg = clientsocket.recv(64)
                if new_msg:
                    print("new msg len:", msg[:HEADERSIZE])
                    msglen = int(msg[:HEADERSIZE])
                    new_msg = False

                print(f"full message length: {msglen}")

                full_msg += msg.decode("utf-8")

                if len(full_msg) - HEADERSIZE == msglen:
                    print(full_msg[HEADERSIZE:])
                    new_msg = True

                if str(full_msg[HEADERSIZE:]) == "Patient":
                    print("Patient File Received!")
                    dicom = easySocket.rcv_data(clientsocket)
                    f = open("Patient_File.zip", 'wb')
                    f.write(dicom)
                    shutil.unpack_archive("Patient_File.zip", "./unzippedMyHead", 'zip')
                    app.process("./unzippedMyHead")
                    ImgToVideo.img_to_video()


                if str(full_msg[HEADERSIZE:]) == "Info":
                    print("Requesting Info!")
                    easySocket.send_file("Patient_Data.txt", clientsocket)

                if str(full_msg[HEADERSIZE:]) == "Image":
                    print("Requesting Image")
                    self.ui.image_label.setText("here")
                    pixmap = QPixmap("/home/gamila/Documents/4th year/1st Term/Network/server-and-client-image-manipulation/g.png")
                    pixmap = pixmap.scaled(int(pixmap.height()), int(pixmap.width()), QtCore.Qt.KeepAspectRatio)
                    self.ui.image_label.setPixmap(pixmap)
                    self.ui.image_label.setScaledContents(True)
                    self.ui.image_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
                    easySocket.send_file("g.png", clientsocket)

                if str(full_msg[HEADERSIZE:]) == "Video":
                    print("Requesting Video!")
                    easySocket.send_file("head.avi", clientsocket)




def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
