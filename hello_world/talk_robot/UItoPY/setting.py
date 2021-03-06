# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(380, 316)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.setting_window = QtWidgets.QTabWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.setting_window.setFont(font)
        self.setting_window.setStyleSheet("")
        self.setting_window.setObjectName("setting_window")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listView = QtWidgets.QListView(self.tab)
        self.listView.setStyleSheet("background-color:rgb(149,236,105);")
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setObjectName("listView")
        self.horizontalLayout_3.addWidget(self.listView)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 40)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.add_qun = QtWidgets.QPushButton(self.tab)
        self.add_qun.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.add_qun.setFont(font)
        self.add_qun.setStyleSheet("background-color:rgb(149,236,105);")
        self.add_qun.setObjectName("add_qun")
        self.verticalLayout_5.addWidget(self.add_qun)
        self.modif_qun = QtWidgets.QPushButton(self.tab)
        self.modif_qun.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.modif_qun.setFont(font)
        self.modif_qun.setStyleSheet("background-color:rgb(149,236,105);")
        self.modif_qun.setObjectName("modif_qun")
        self.verticalLayout_5.addWidget(self.modif_qun)
        self.del_qun = QtWidgets.QPushButton(self.tab)
        self.del_qun.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.del_qun.setFont(font)
        self.del_qun.setStyleSheet("background-color:rgb(149,236,105);")
        self.del_qun.setObjectName("del_qun")
        self.verticalLayout_5.addWidget(self.del_qun)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.setting_window.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color:rgb(149,236,105);")
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(149, 236, 105))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(149, 236, 105))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(90)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setMinimumSectionSize(15)
        self.horizontalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 40)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_word = QtWidgets.QPushButton(self.tab_2)
        self.add_word.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.add_word.setFont(font)
        self.add_word.setStyleSheet("background-color:rgb(149,236,105);")
        self.add_word.setObjectName("add_word")
        self.verticalLayout_2.addWidget(self.add_word)
        self.modif_word = QtWidgets.QPushButton(self.tab_2)
        self.modif_word.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.modif_word.setFont(font)
        self.modif_word.setStyleSheet("background-color:rgb(149,236,105);")
        self.modif_word.setObjectName("modif_word")
        self.verticalLayout_2.addWidget(self.modif_word)
        self.del_word = QtWidgets.QPushButton(self.tab_2)
        self.del_word.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.del_word.setFont(font)
        self.del_word.setStyleSheet("background-color:rgb(149,236,105);")
        self.del_word.setObjectName("del_word")
        self.verticalLayout_2.addWidget(self.del_word)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.setting_window.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setStyleSheet("background-color:rgb(149,236,105);")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.add_film = QtWidgets.QPushButton(self.tab_3)
        self.add_film.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.add_film.setFont(font)
        self.add_film.setStyleSheet("background-color:rgb(149,236,105);")
        self.add_film.setObjectName("add_film")
        self.horizontalLayout.addWidget(self.add_film)
        self.del_film = QtWidgets.QPushButton(self.tab_3)
        self.del_film.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.del_film.setFont(font)
        self.del_film.setStyleSheet("background-color:rgb(149,236,105);")
        self.del_film.setObjectName("del_film")
        self.horizontalLayout.addWidget(self.del_film)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 8)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setStyleSheet("background-color:rgb(149,236,105);")
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.add_filter = QtWidgets.QPushButton(self.groupBox)
        self.add_filter.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.add_filter.setFont(font)
        self.add_filter.setStyleSheet("background-color:rgb(149,236,105);")
        self.add_filter.setObjectName("add_filter")
        self.verticalLayout_4.addWidget(self.add_filter)
        self.modif_filter = QtWidgets.QPushButton(self.groupBox)
        self.modif_filter.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.modif_filter.setFont(font)
        self.modif_filter.setStyleSheet("background-color:rgb(149,236,105);")
        self.modif_filter.setObjectName("modif_filter")
        self.verticalLayout_4.addWidget(self.modif_filter)
        self.del_filter = QtWidgets.QPushButton(self.groupBox)
        self.del_filter.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.del_filter.setFont(font)
        self.del_filter.setStyleSheet("background-color:rgb(149,236,105);")
        self.del_filter.setObjectName("del_filter")
        self.verticalLayout_4.addWidget(self.del_filter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.verticalLayout_3.setStretch(0, 1)
        self.setting_window.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(20, 0, 20, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.apiKeyEdit = QtWidgets.QLineEdit(self.tab_4)
        self.apiKeyEdit.setObjectName("apiKeyEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.apiKeyEdit)
        self.apiPassEdit = QtWidgets.QLineEdit(self.tab_4)
        self.apiPassEdit.setText("")
        self.apiPassEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.apiPassEdit.setClearButtonEnabled(False)
        self.apiPassEdit.setObjectName("apiPassEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.apiPassEdit)
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.replace_open = QtWidgets.QRadioButton(self.tab_4)
        self.replace_open.setObjectName("replace_open")
        self.horizontalLayout_6.addWidget(self.replace_open)
        self.replace_close = QtWidgets.QRadioButton(self.tab_4)
        self.replace_close.setObjectName("replace_close")
        self.horizontalLayout_6.addWidget(self.replace_close)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.horizontalLayout_5.addLayout(self.formLayout)
        self.setting_window.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.setting_window)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.buttonBox.setFont(font)
        self.buttonBox.setStyleSheet("background-color:rgb(149,236,105);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.setting_window.setCurrentIndex(3)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "系统设置"))
        self.add_qun.setText(_translate("Dialog", "添加"))
        self.modif_qun.setText(_translate("Dialog", "修改"))
        self.del_qun.setText(_translate("Dialog", "删除"))
        self.setting_window.setTabText(self.setting_window.indexOf(self.tab), _translate("Dialog", "自动回复群名"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "关键词"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "回复"))
        self.add_word.setText(_translate("Dialog", "添加"))
        self.modif_word.setText(_translate("Dialog", "修改"))
        self.del_word.setText(_translate("Dialog", "删除"))
        self.setting_window.setTabText(self.setting_window.indexOf(self.tab_2), _translate("Dialog", "相应关键词"))
        self.label.setText(_translate("Dialog", "剧集:"))
        self.add_film.setText(_translate("Dialog", "添加"))
        self.del_film.setText(_translate("Dialog", "删除"))
        self.groupBox.setTitle(_translate("Dialog", "关键词列表"))
        self.add_filter.setText(_translate("Dialog", "添加"))
        self.modif_filter.setText(_translate("Dialog", "修改"))
        self.del_filter.setText(_translate("Dialog", "删除"))
        self.setting_window.setTabText(self.setting_window.indexOf(self.tab_3), _translate("Dialog", "防透设置"))
        self.label_2.setText(_translate("Dialog", "apikey:"))
        self.label_3.setText(_translate("Dialog", "密钥"))
        self.label_4.setText(_translate("Dialog", "替换关键词回复："))
        self.replace_open.setText(_translate("Dialog", "关闭"))
        self.replace_close.setText(_translate("Dialog", "启动"))
        self.setting_window.setTabText(self.setting_window.indexOf(self.tab_4), _translate("Dialog", "图灵机器人"))

