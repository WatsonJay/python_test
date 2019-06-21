# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_password_Dialog(object):
    def setupUi(self, password_Dialog):
        password_Dialog.setObjectName("password_Dialog")
        password_Dialog.resize(174, 216)
        password_Dialog.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(password_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(password_Dialog)
        self.widget.setStyleSheet("border-image: url(:/icon/background.jpg);")
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(password_Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.password_lineEdit = QtWidgets.QLineEdit(password_Dialog)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout.addWidget(self.password_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.unlock_pushButton = QtWidgets.QPushButton(password_Dialog)
        self.unlock_pushButton.setObjectName("unlock_pushButton")
        self.horizontalLayout_2.addWidget(self.unlock_pushButton)
        self.pushButton = QtWidgets.QPushButton(password_Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 8)

        self.retranslateUi(password_Dialog)
        self.pushButton.clicked.connect(password_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(password_Dialog)

    def retranslateUi(self, password_Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("password_Dialog", "密码:"))
        self.unlock_pushButton.setText(_translate("password_Dialog", "解锁"))
        self.pushButton.setText(_translate("password_Dialog", "关闭"))

import hello_world.linx_monitor.main.ui.icons
