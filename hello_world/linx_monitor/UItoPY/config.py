# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SysConfig_Dialog(object):
    def setupUi(self, SysConfig_Dialog):
        SysConfig_Dialog.setObjectName("SysConfig_Dialog")
        SysConfig_Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(SysConfig_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(SysConfig_Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CPU_spinBox = QtWidgets.QSpinBox(self.tab)
        self.CPU_spinBox.setObjectName("CPU_spinBox")
        self.horizontalLayout.addWidget(self.CPU_spinBox)
        self.label_4 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.horizontalLayout.setStretch(0, 9)
        self.horizontalLayout.setStretch(1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MEM_spinBox = QtWidgets.QSpinBox(self.tab)
        self.MEM_spinBox.setObjectName("MEM_spinBox")
        self.horizontalLayout_2.addWidget(self.MEM_spinBox)
        self.label_5 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_2.setStretch(0, 9)
        self.horizontalLayout_2.setStretch(1, 1)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.DISK_spinBox = QtWidgets.QSpinBox(self.tab)
        self.DISK_spinBox.setObjectName("DISK_spinBox")
        self.horizontalLayout_3.addWidget(self.DISK_spinBox)
        self.label_6 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_3.setStretch(0, 9)
        self.horizontalLayout_3.setStretch(1, 1)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Simple_Rate_spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.Simple_Rate_spinBox.setObjectName("Simple_Rate_spinBox")
        self.horizontalLayout_4.addWidget(self.Simple_Rate_spinBox)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_4.setStretch(0, 9)
        self.horizontalLayout_4.setStretch(1, 1)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(SysConfig_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SysConfig_Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(SysConfig_Dialog.accept)
        self.buttonBox.rejected.connect(SysConfig_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SysConfig_Dialog)

    def retranslateUi(self, SysConfig_Dialog):
        _translate = QtCore.QCoreApplication.translate
        SysConfig_Dialog.setWindowTitle(_translate("SysConfig_Dialog", "系统设置"))
        self.label.setText(_translate("SysConfig_Dialog", "Cpu预警线："))
        self.label_2.setText(_translate("SysConfig_Dialog", "内存预警线："))
        self.label_3.setText(_translate("SysConfig_Dialog", "磁盘预警线："))
        self.label_4.setText(_translate("SysConfig_Dialog", "%"))
        self.label_5.setText(_translate("SysConfig_Dialog", "%"))
        self.label_6.setText(_translate("SysConfig_Dialog", "%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SysConfig_Dialog", "预警辅助线"))
        self.label_7.setText(_translate("SysConfig_Dialog", "采样间隔时间："))
        self.label_8.setText(_translate("SysConfig_Dialog", "秒"))
        self.label_9.setText(_translate("SysConfig_Dialog", "开启密码："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SysConfig_Dialog", "采样频率"))

