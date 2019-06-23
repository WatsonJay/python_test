# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'totalanalysis.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_totanl_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(223, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addFile_pushButton = QtWidgets.QPushButton(Form)
        self.addFile_pushButton.setObjectName("addFile_pushButton")
        self.horizontalLayout.addWidget(self.addFile_pushButton)
        self.remove_pushButton = QtWidgets.QPushButton(Form)
        self.remove_pushButton.setObjectName("remove_pushButton")
        self.horizontalLayout.addWidget(self.remove_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.file_listWidget = QtWidgets.QListWidget(Form)
        self.file_listWidget.setObjectName("file_listWidget")
        self.verticalLayout.addWidget(self.file_listWidget)
        self.analysis_pushButton = QtWidgets.QPushButton(Form)
        self.analysis_pushButton.setObjectName("analysis_pushButton")
        self.verticalLayout.addWidget(self.analysis_pushButton)
        self.save_pushButton = QtWidgets.QPushButton(Form)
        self.save_pushButton.setObjectName("save_pushButton")
        self.verticalLayout.addWidget(self.save_pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addFile_pushButton.setText(_translate("Form", "添加文件..."))
        self.remove_pushButton.setText(_translate("Form", "删除选中"))
        self.analysis_pushButton.setText(_translate("Form", "开始分析"))
        self.save_pushButton.setText(_translate("Form", "合并保存"))

