# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auto_send_setting.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_auto_send_Dialog(object):
    def setupUi(self, auto_send_Dialog):
        auto_send_Dialog.setObjectName("auto_send_Dialog")
        auto_send_Dialog.resize(361, 162)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(auto_send_Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(auto_send_Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(auto_send_Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.sendWords = QtWidgets.QTextEdit(auto_send_Dialog)
        self.sendWords.setObjectName("sendWords")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sendWords)
        self.timeLineEdit = QtWidgets.QLineEdit(auto_send_Dialog)
        self.timeLineEdit.setObjectName("timeLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.timeLineEdit)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(auto_send_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(auto_send_Dialog)
        self.buttonBox.accepted.connect(auto_send_Dialog.accept)
        self.buttonBox.rejected.connect(auto_send_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(auto_send_Dialog)

    def retranslateUi(self, auto_send_Dialog):
        _translate = QtCore.QCoreApplication.translate
        auto_send_Dialog.setWindowTitle(_translate("auto_send_Dialog", "自动回复设定"))
        self.label.setText(_translate("auto_send_Dialog", "发送时间："))
        self.label_2.setText(_translate("auto_send_Dialog", "自动回复内容："))
