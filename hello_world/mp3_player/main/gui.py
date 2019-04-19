# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer


class Ui_musicPlayer(object):
    def setupUi(self, musicPlayer):
        musicPlayer.setObjectName("musicPlayer")
        musicPlayer.resize(491, 225)
        self.songs_list = []
        self.song_formats = ['mp3', 'm4a', 'flac', 'wav', 'ogg']
        self.player = QMediaPlayer()
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.cur_playing_song = ''
        self.is_switching = False
        self.is_pause = True
        self.centralwidget = QtWidgets.QWidget(musicPlayer)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.songUp = QtWidgets.QPushButton(self.centralwidget)
        self.songUp.setObjectName("songUp")
        self.verticalLayout.addWidget(self.songUp)
        self.songDn = QtWidgets.QPushButton(self.centralwidget)
        self.songDn.setObjectName("songDn")
        self.verticalLayout.addWidget(self.songDn)
        self.playType = QtWidgets.QComboBox(self.centralwidget)
        self.playType.setObjectName("playType")
        self.playType.addItem("")
        self.playType.addItem("")
        self.playType.addItem("")
        self.verticalLayout.addWidget(self.playType)
        self.openDir = QtWidgets.QPushButton(self.centralwidget)
        self.openDir.setObjectName("openDir")
        self.verticalLayout.addWidget(self.openDir)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.playStop = QtWidgets.QPushButton(self.centralwidget)
        self.playStop.setObjectName("playStop")
        self.verticalLayout_2.addWidget(self.playStop)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 2)
        musicPlayer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(musicPlayer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 491, 23))
        self.menubar.setObjectName("menubar")
        musicPlayer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(musicPlayer)
        self.statusbar.setObjectName("statusbar")
        musicPlayer.setStatusBar(self.statusbar)

        self.retranslateUi(musicPlayer)
        QtCore.QMetaObject.connectSlotsByName(musicPlayer)

    def retranslateUi(self, musicPlayer):
        _translate = QtCore.QCoreApplication.translate
        musicPlayer.setWindowTitle(_translate("musicPlayer", "简易播放器"))
        self.label.setText(_translate("musicPlayer", "--:--"))
        self.label_2.setText(_translate("musicPlayer", "--:--"))
        self.songUp.setText(_translate("musicPlayer", "上一首"))
        self.songDn.setText(_translate("musicPlayer", "下一首"))
        self.playType.setItemText(0, _translate("musicPlayer", "顺序播放"))
        self.playType.setItemText(1, _translate("musicPlayer", "单曲循环"))
        self.playType.setItemText(2, _translate("musicPlayer", "随机播放"))
        self.openDir.setText(_translate("musicPlayer", "打开文件夹"))
        self.playStop.setText(_translate("musicPlayer", "播放"))

