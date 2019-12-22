# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyClient.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(650, 20, 131, 31))
        self.browseButton.setObjectName("browseButton")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(260, 60, 251, 31))
        self.connectButton.setObjectName("connectButton")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(260, 140, 251, 31))
        self.sendButton.setObjectName("sendButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 170, 591, 391))
        self.groupBox.setObjectName("groupBox")
        self.imageLabel = QtWidgets.QLabel(self.groupBox)
        self.imageLabel.setGeometry(QtCore.QRect(10, 30, 271, 351))
        self.imageLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.videoLabel = QtWidgets.QLabel(self.groupBox)
        self.videoLabel.setGeometry(QtCore.QRect(310, 30, 271, 351))
        self.videoLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.videoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.videoLabel.setObjectName("videoLabel")
        self.infoButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoButton.setGeometry(QtCore.QRect(620, 240, 141, 25))
        self.infoButton.setObjectName("infoButton")
        self.imageButton = QtWidgets.QPushButton(self.centralwidget)
        self.imageButton.setGeometry(QtCore.QRect(620, 340, 141, 25))
        self.imageButton.setObjectName("imageButton")
        self.videoButton = QtWidgets.QPushButton(self.centralwidget)
        self.videoButton.setGeometry(QtCore.QRect(620, 440, 141, 25))
        self.videoButton.setObjectName("videoButton")
        self.disconnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.disconnectButton.setGeometry(QtCore.QRect(260, 100, 251, 31))
        self.disconnectButton.setObjectName("disconnectButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 621, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.sendButton.setText(_translate("MainWindow", "Send Patient\'s Files"))
        self.groupBox.setTitle(_translate("MainWindow", "Patient\'s Data "))
        self.imageLabel.setText(_translate("MainWindow", "Image"))
        self.videoLabel.setText(_translate("MainWindow", "Video"))
        self.infoButton.setText(_translate("MainWindow", "Information"))
        self.imageButton.setText(_translate("MainWindow", "Image"))
        self.videoButton.setText(_translate("MainWindow", "Video"))
        self.disconnectButton.setText(_translate("MainWindow", "Disconnect"))
