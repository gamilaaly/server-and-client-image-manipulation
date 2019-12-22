from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QSizePolicy
from MyClient import Ui_MainWindow
import sys
import socket
import time
import easySocket
from PyQt5.QtGui import QPixmap
import os
import shutil


class ApplicationWindow(QtWidgets.QMainWindow):
    Directory = ''
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global HEADERSIZE
        HEADERSIZE = 10
        self.ui.connectButton.clicked.connect(self.connect_with_server)
        self.ui.disconnectButton.clicked.connect(self.disconnect)
        self.ui.browseButton.clicked.connect(self.browse)
        self.ui.infoButton.clicked.connect(self.requestInfo)
        self.ui.videoButton.clicked.connect(self.requestVideo)
        self.ui.imageButton.clicked.connect(self.requestImage)
        self.ui.sendButton.clicked.connect(self.send_file)

        print("before connecting")

    def connect_with_server (self):
        print("pressed connect")
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 12445))
        print("connected")


    def send_file(self):
        shutil.make_archive("MyHead", 'zip', self.Directory)
        msg = "Patient"
        msg = f"{len(msg):<{HEADERSIZE}}" + msg
        s.send(bytes(msg, "utf-8"))
        time.sleep(1)
        easySocket.send_file("MyHead.zip",s)

    def disconnect (self):
        print ("disconnected")
        global s
        s.close()

    def browse (self):
        self.Directory = QFileDialog.getExistingDirectory(self, 'Choose Directory', os.path.expanduser('~'))
        self.ui.lineEdit.setText(self.Directory)

    def requestInfo(self):
        print("Requesting Information")
        msg = "Info"
        msg = f"{len(msg):<{HEADERSIZE}}" + msg
        s.send(bytes(msg, "utf-8"))
        time.sleep(1)
        info = easySocket.rcv_data(s)
        print(info)
        f = open("Patient_Data.txt", 'wb')
        f.write(info)
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText('Your file has been downloaded!!')
        msg.exec_()

    def requestImage(self):
        print("Requesting Image")
        msg = "Image"
        msg = f"{len(msg):<{HEADERSIZE}}" + msg
        s.send(bytes(msg, "utf-8"))
        image = easySocket.rcv_data(s)
        f = open("img0Rec.png", 'wb')
        f.write(image)
        pixmap = QPixmap("g.png")
        pixmap = pixmap.scaled(int(pixmap.height()), int(pixmap.width()), QtCore.Qt.KeepAspectRatio)
        self.ui.imageLabel.setPixmap(pixmap)
        self.ui.imageLabel.setScaledContents(True)
        self.ui.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

    def requestVideo(self):
        print("Requesting Video")
        msg = "Video"
        msg = f"{len(msg):<{HEADERSIZE}}" + msg
        s.send(bytes(msg, "utf-8"))
        video = easySocket.rcv_data(s)
        f = open("MyHead.avi", 'wb')
        f.write(video)





def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()