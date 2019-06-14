# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_helper.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class User_helper(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 202)
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
        Form.setWindowTitle(_translate("Form", "Form"))
        Form.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">使用说明</span></p><p>1.新增服务器连接信息，包括ip,端口，用户名，密码，可进行测试连接</p><p>2.双击新增好的服务器，确认连接，进入监控页面</p><p>3.如目标服务器未上传nmon,可点击上传，上传路径默认为~,请确认用户权限</p><p>4.在目标服务器存在nmon的前提条件下，可开启性能监控记录</p><p>5.在nmon性能记录生成完成后，可进行下载，点击清除可清除当前记录</p><p>6.数据折线图自动滚动，点击锁定后停止滚动，再次点击恢复</p></body></html>"))
        self.pushButton.setText(_translate("Form", "关闭"))

