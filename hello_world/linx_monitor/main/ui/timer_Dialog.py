# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_timer_Dialog(object):
    def setupUi(self, timer_Dialog):
        timer_Dialog.setObjectName("timer_Dialog")
        timer_Dialog.resize(312, 70)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(timer_Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(timer_Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.hour_spinBox = QtWidgets.QSpinBox(timer_Dialog)
        self.hour_spinBox.setObjectName("hour_spinBox")
        self.horizontalLayout.addWidget(self.hour_spinBox)
        self.label_2 = QtWidgets.QLabel(timer_Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.min_spinBox = QtWidgets.QSpinBox(timer_Dialog)
        self.min_spinBox.setObjectName("min_spinBox")
        self.horizontalLayout.addWidget(self.min_spinBox)
        self.label_3 = QtWidgets.QLabel(timer_Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(timer_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout_2.setStretch(0, 7)
        self.horizontalLayout_2.setStretch(1, 3)

        self.retranslateUi(timer_Dialog)
        self.buttonBox.accepted.connect(timer_Dialog.accept)
        self.buttonBox.rejected.connect(timer_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(timer_Dialog)

    def retranslateUi(self, timer_Dialog):
        _translate = QtCore.QCoreApplication.translate
        timer_Dialog.setWindowTitle(_translate("timer_Dialog", "Dialog"))
        self.label.setText(_translate("timer_Dialog", "记录时长："))
        self.label_2.setText(_translate("timer_Dialog", "小时"))
        self.label_3.setText(_translate("timer_Dialog", "分"))

