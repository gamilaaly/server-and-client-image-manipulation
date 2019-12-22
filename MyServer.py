# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyServer.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listenButton = QtWidgets.QPushButton(self.centralwidget)
        self.listenButton.setGeometry(QtCore.QRect(180, 20, 321, 41))
        self.listenButton.setObjectName("listenButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 671, 491))
        self.groupBox.setObjectName("groupBox")
        self.videoLabel = QtWidgets.QLabel(self.groupBox)
        self.videoLabel.setGeometry(QtCore.QRect(340, 50, 321, 421))
        self.videoLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.videoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.videoLabel.setObjectName("videoLabel")
        self.image_label = QtWidgets.QLabel(self.groupBox)
        self.image_label.setGeometry(QtCore.QRect(0, 50, 321, 421))
        self.image_label.setFrameShape(QtWidgets.QFrame.Box)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 22))
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
        self.listenButton.setText(_translate("MainWindow", "listen"))
        self.groupBox.setTitle(_translate("MainWindow", "Patient\'s Data "))
        self.videoLabel.setText(_translate("MainWindow", "Video"))
        self.image_label.setText(_translate("MainWindow", "Image "))
