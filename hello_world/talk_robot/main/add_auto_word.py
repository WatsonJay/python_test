# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_auto_word.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WordDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(394, 235)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.horizontalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.buttonBox.setFont(font)
        self.buttonBox.setStyleSheet("background-color:rgb(149,236,105);")
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "关键词"))
        self.label.setText(_translate("Dialog", "关键词："))
        self.label_2.setText(_translate("Dialog", "回复："))

