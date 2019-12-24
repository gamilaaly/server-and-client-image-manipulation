import socket
import threading
import time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QSizePolicy
from MyServer import Ui_MainWindow
import sys
import easySocket
from PyQt5.QtGui import QPixmap
import shutil
import Processing
import ImgToVideo


class ApplicationWindow(QtWidgets.QMainWindow):
    image_flag = False
    IP = ''
    PORT = 0

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global HEADERSIZE
        HEADERSIZE = 10
        self.ui.listenButton.clicked.connect(self.listen)
        self.ui.bind_button.clicked.connect(self.bind)
        print("heey before listen")
        global server_socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        global th_listen
        th_listen = threading.Thread(target=self.listen_function, args=())

    def bind(self):
        self.IP = self.ui.ip_edit.text()
        self.PORT = self.ui.port_edit.text()
        self.PORT = int(self.PORT)
        server_socket.bind((self.IP, self.PORT))

    def listen(self):
        th_listen.start()

    def listen_function(self):
        # This makes server listen to new connections
        server_socket.listen()
        print("Listening ....")

        while True:
            # now our endpoint knows about the OTHER endpoint.
            clientsocket, address = server_socket.accept()
            print(f"Connection from {address} has been established.")

            while True:
                if self.image_flag == True:
                    self.set_image()
                    QApplication.processEvents()

                full_msg = ''
                new_msg = True
                msg = clientsocket.recv(64)  # buffer size
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
                    shutil.unpack_archive("Patient_File.zip", "./unzippedMyHead", 'zip')  # decompress
                    Processing.process("./unzippedMyHead")
                    QApplication.processEvents()
                    ImgToVideo.img_to_video()


                if str(full_msg[HEADERSIZE:]) == "Info":
                    print("Requesting Info!")
                    easySocket.send_file("Patient_Data.txt", clientsocket)

                if str(full_msg[HEADERSIZE:]) == "Image":
                    print("Requesting Image")
                    self.set_image()
                    self.image_flag = True
                    easySocket.send_file("Images/img100.png", clientsocket)

                if str(full_msg[HEADERSIZE:]) == "Contour":
                    print("Requesting Image")
                    easySocket.send_file("Tumor_Contour.png", clientsocket)

                if str(full_msg[HEADERSIZE:]) == "Video":
                    print("Requesting Video!")
                    shutil.make_archive("MyHeadVideo", 'zip', "./server_video")
                    easySocket.send_file("MyHeadVideo.zip", clientsocket)

    def set_image(self):
        pixmap = QPixmap("Images/img100.png")  # needs to modify image
        pixmap = pixmap.scaled(int(pixmap.height()), int(pixmap.width()), QtCore.Qt.KeepAspectRatio)
        self.ui.image_label.setPixmap(pixmap)
        self.ui.image_label.setScaledContents(True)
        self.ui.image_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
