# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MonitorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Monitor_Window(object):
    def setupUi(self, Monitor_Window):
        Monitor_Window.setObjectName("Monitor_Window")
        Monitor_Window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Monitor_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.serverAdd = QtWidgets.QPushButton(self.centralwidget)
        self.serverAdd.setMinimumSize(QtCore.QSize(30, 10))
        self.serverAdd.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/cloud-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.serverAdd.setIcon(icon)
        self.serverAdd.setObjectName("serverAdd")
        self.horizontalLayout.addWidget(self.serverAdd)
        self.serverModif = QtWidgets.QPushButton(self.centralwidget)
        self.serverModif.setMinimumSize(QtCore.QSize(30, 10))
        self.serverModif.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icon/cloud.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.serverModif.setIcon(icon1)
        self.serverModif.setObjectName("serverModif")
        self.horizontalLayout.addWidget(self.serverModif)
        self.serverDelete = QtWidgets.QPushButton(self.centralwidget)
        self.serverDelete.setMinimumSize(QtCore.QSize(30, 10))
        self.serverDelete.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icon/cloud-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.serverDelete.setIcon(icon2)
        self.serverDelete.setObjectName("serverDelete")
        self.horizontalLayout.addWidget(self.serverDelete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.server_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.server_listWidget.setObjectName("server_listWidget")
        self.verticalLayout.addWidget(self.server_listWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 8)
        Monitor_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Monitor_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        Monitor_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Monitor_Window)
        self.statusbar.setObjectName("statusbar")
        Monitor_Window.setStatusBar(self.statusbar)
        self.actionuse = QtWidgets.QAction(Monitor_Window)
        self.actionuse.setObjectName("actionuse")
        self.actioninfo = QtWidgets.QAction(Monitor_Window)
        self.actioninfo.setObjectName("actioninfo")
        self.actionshezhi = QtWidgets.QAction(Monitor_Window)
        self.actionshezhi.setObjectName("actionshezhi")
        self.menu_2.addAction(self.actionuse)
        self.menu_2.addAction(self.actioninfo)
        self.menu.addAction(self.actionshezhi)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(Monitor_Window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Monitor_Window)

    def retranslateUi(self, Monitor_Window):
        _translate = QtCore.QCoreApplication.translate
        Monitor_Window.setWindowTitle(_translate("Monitor_Window", "linux远程监控器"))
        self.menu_2.setTitle(_translate("Monitor_Window", "帮助"))
        self.menu.setTitle(_translate("Monitor_Window", "设置"))
        self.actionuse.setText(_translate("Monitor_Window", "使用说明"))
        self.actioninfo.setText(_translate("Monitor_Window", "软件信息"))
        self.actionshezhi.setText(_translate("Monitor_Window", "系统设置"))


