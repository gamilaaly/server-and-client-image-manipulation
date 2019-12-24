# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyClient.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
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
        self.browseButton.setGeometry(QtCore.QRect(650, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(12)
        self.browseButton.setFont(font)
        self.browseButton.setObjectName("browseButton")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(90, 120, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(14)
        self.connectButton.setFont(font)
        self.connectButton.setObjectName("connectButton")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(540, 220, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(14)
        self.sendButton.setFont(font)
        self.sendButton.setObjectName("sendButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 160, 511, 411))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.imageLabel = QtWidgets.QLabel(self.groupBox)
        self.imageLabel.setGeometry(QtCore.QRect(10, 40, 491, 321))
        self.imageLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.infoButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoButton.setGeometry(QtCore.QRect(540, 280, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(13)
        self.infoButton.setFont(font)
        self.infoButton.setObjectName("infoButton")
        self.imageButton = QtWidgets.QPushButton(self.centralwidget)
        self.imageButton.setGeometry(QtCore.QRect(540, 340, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(13)
        self.imageButton.setFont(font)
        self.imageButton.setObjectName("imageButton")
        self.videoButton = QtWidgets.QPushButton(self.centralwidget)
        self.videoButton.setGeometry(QtCore.QRect(540, 400, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(13)
        self.videoButton.setFont(font)
        self.videoButton.setObjectName("videoButton")
        self.disconnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.disconnectButton.setGeometry(QtCore.QRect(480, 120, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(14)
        self.disconnectButton.setFont(font)
        self.disconnectButton.setObjectName("disconnectButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 621, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 65, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ip_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_edit.setGeometry(QtCore.QRect(110, 60, 191, 31))
        self.ip_edit.setObjectName("ip_edit")
        self.port_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.port_edit.setGeometry(QtCore.QRect(530, 60, 191, 31))
        self.port_edit.setObjectName("port_edit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 70, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.contourButton = QtWidgets.QPushButton(self.centralwidget)
        self.contourButton.setGeometry(QtCore.QRect(540, 460, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(13)
        self.contourButton.setFont(font)
        self.contourButton.setObjectName("contourButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 26))
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
        self.infoButton.setText(_translate("MainWindow", "REQUEST INFORMATION"))
        self.imageButton.setText(_translate("MainWindow", "REQUEST IMAGE"))
        self.videoButton.setText(_translate("MainWindow", "REQUEST VIDEO"))
        self.disconnectButton.setText(_translate("MainWindow", "Disconnect"))
        self.label.setText(_translate("MainWindow", "IP"))
        self.label_2.setText(_translate("MainWindow", "PORT"))
        self.contourButton.setText(_translate("MainWindow", "CONTOUR"))
