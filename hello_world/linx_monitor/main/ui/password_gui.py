# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
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
        self.buttonBox = QtWidgets.QDialogButtonBox(password_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText('确定')
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText('取消')
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(0, 8)

        self.retranslateUi(password_Dialog)
        self.buttonBox.accepted.connect(password_Dialog.accept)
        self.buttonBox.rejected.connect(password_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(password_Dialog)

    def retranslateUi(self, password_Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("password_Dialog", "密码:"))

import hello_world.linx_monitor.main.ui.icons
