# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class info_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(236, 145)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "软件信息"))
        # 禁止最大化按钮
        Form.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">软件信息</span></p><p align=\"center\">作者：花二爷</p><p align=\"center\">Github：https://github.com/WatsonJay</p><p align=\"center\">版本：V1.0</p></body></html>"))
        self.pushButton.setText(_translate("Form", "关闭"))

