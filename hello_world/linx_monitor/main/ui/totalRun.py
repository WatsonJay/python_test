# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'totalRun.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_totalRun_Form(object):
    def setupUi(self, totalRun_Form):
        totalRun_Form.setObjectName("totalRun_Form")
        totalRun_Form.resize(534, 257)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(totalRun_Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.server_listWidget = QtWidgets.QListWidget(totalRun_Form)
        self.server_listWidget.setObjectName("server_listWidget")
        self.horizontalLayout_2.addWidget(self.server_listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_pushButton = QtWidgets.QPushButton(totalRun_Form)
        self.add_pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.add_pushButton.setObjectName("add_pushButton")
        self.verticalLayout.addWidget(self.add_pushButton)
        self.remove_pushButton = QtWidgets.QPushButton(totalRun_Form)
        self.remove_pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.remove_pushButton.setObjectName("remove_pushButton")
        self.verticalLayout.addWidget(self.remove_pushButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.added_listWidget = QtWidgets.QListWidget(totalRun_Form)
        self.added_listWidget.setObjectName("added_listWidget")
        self.horizontalLayout_2.addWidget(self.added_listWidget)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, 20, -1, -1)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(totalRun_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(totalRun_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(totalRun_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.time_spinBox = QtWidgets.QSpinBox(totalRun_Form)
        self.time_spinBox.setObjectName("time_spinBox")
        self.time_spinBox.setMinimum(1)
        self.time_spinBox.setMaximum(60)
        self.horizontalLayout_3.addWidget(self.time_spinBox)
        self.label_6 = QtWidgets.QLabel(totalRun_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_3.setStretch(0, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tap_spinBox = QtWidgets.QSpinBox(totalRun_Form)
        self.tap_spinBox.setObjectName("tap_spinBox")
        self.tap_spinBox.setMinimum(1)
        self.tap_spinBox.setMaximum(6000)
        self.horizontalLayout_4.addWidget(self.tap_spinBox)
        self.label_5 = QtWidgets.QLabel(totalRun_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_4.setStretch(0, 1)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupName_lineEdit = QtWidgets.QLineEdit(totalRun_Form)
        self.groupName_lineEdit.setObjectName("groupName_lineEdit")
        self.horizontalLayout_5.addWidget(self.groupName_lineEdit)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(totalRun_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.totalFile_label = QtWidgets.QLabel(totalRun_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.totalFile_label.setFont(font)
        self.totalFile_label.setObjectName("totalFile_label")
        self.horizontalLayout_6.addWidget(self.totalFile_label)
        self.label_8 = QtWidgets.QLabel(totalRun_Form)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777205))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:green")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.successFile_label = QtWidgets.QLabel(totalRun_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.successFile_label.setFont(font)
        self.successFile_label.setStyleSheet("color:green\n"
"")
        self.successFile_label.setObjectName("successFile_label")
        self.horizontalLayout_6.addWidget(self.successFile_label)
        self.label_4 = QtWidgets.QLabel(totalRun_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:red")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.failFile_label = QtWidgets.QLabel(totalRun_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.failFile_label.setFont(font)
        self.failFile_label.setStyleSheet("color:red")
        self.failFile_label.setObjectName("failFile_label")
        self.horizontalLayout_6.addWidget(self.failFile_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.progressBar = QtWidgets.QProgressBar(totalRun_Form)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_pushButton = QtWidgets.QPushButton(totalRun_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.start_pushButton.setFont(font)
        self.start_pushButton.setObjectName("start_pushButton")
        self.horizontalLayout.addWidget(self.start_pushButton)
        self.download_pushButton = QtWidgets.QPushButton(totalRun_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.download_pushButton.setFont(font)
        self.download_pushButton.setObjectName("download_pushButton")
        self.horizontalLayout.addWidget(self.download_pushButton)
        self.close_pushButton = QtWidgets.QPushButton(totalRun_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.close_pushButton.setFont(font)
        self.close_pushButton.setObjectName("close_pushButton")
        self.horizontalLayout.addWidget(self.close_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(totalRun_Form)
        self.close_pushButton.clicked.connect(totalRun_Form.close)
        QtCore.QMetaObject.connectSlotsByName(totalRun_Form)

    def retranslateUi(self, totalRun_Form):
        _translate = QtCore.QCoreApplication.translate
        totalRun_Form.setWindowTitle(_translate("totalRun_Form", "批量启动Nmon"))
        self.add_pushButton.setText(_translate("totalRun_Form", ">>"))
        self.remove_pushButton.setText(_translate("totalRun_Form", "<<"))
        self.label.setText(_translate("totalRun_Form", "间隔时长："))
        self.label_2.setText(_translate("totalRun_Form", "采样次数："))
        self.label_3.setText(_translate("totalRun_Form", "批量组名："))
        self.label_6.setText(_translate("totalRun_Form", "秒"))
        self.label_5.setText(_translate("totalRun_Form", "次"))
        self.label_10.setText(_translate("totalRun_Form", "总文件数:"))
        self.totalFile_label.setText(_translate("totalRun_Form", "0"))
        self.label_8.setText(_translate("totalRun_Form", "下载成功数:"))
        self.successFile_label.setText(_translate("totalRun_Form", "0"))
        self.label_4.setText(_translate("totalRun_Form", "下载失败数:"))
        self.failFile_label.setText(_translate("totalRun_Form", "0"))
        self.start_pushButton.setText(_translate("totalRun_Form", "批量开始任务"))
        self.download_pushButton.setText(_translate("totalRun_Form", "批量下载"))
        self.close_pushButton.setText(_translate("totalRun_Form", "关闭"))

