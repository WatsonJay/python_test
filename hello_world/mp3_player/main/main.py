import os
import random
import sys
import configparser
import time

from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp,QMessageBox,QFileDialog
from hello_world.mp3_player.main.gui import Ui_musicPlayer

class MyMainWindow(QMainWindow, Ui_musicPlayer):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.player = QMediaPlayer()
        # --计时器
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.songs_list_select = []
        self.song_formats = ['mp3', 'm4a', 'flac', 'wav', 'ogg']
        self.settingfilename = 'setting.ini'
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.cur_playing_song = ''
        self.is_switching = False
        self.is_pause = True
        self.openDir.clicked.connect(self.open_Dir)
        self.playStop.clicked.connect(self.playMusic)
        self.horizontalSlider.sliderMoved[int].connect(lambda: self.player.setPosition(self.horizontalSlider.value()))
        self.songUp.clicked.connect(self.previewMusic)
        self.songDn.clicked.connect(self.nextMusic)
        self.listWidget.doubleClicked.connect(self.doubleClicked)
        self.timer.timeout.connect(self.playByMode)

    def loadsetting(self):
        if os.path.isfile(self.settingfilename):
            config = configparser.ConfigParser()
            config.read(self.settingfilename)
            self.cur_path = config.get('MusicPlayer','PATH')
            self.showMusicList()

    def savesetting(self):
        config = configparser.ConfigParser()
        config.read(self.settingfilename)
        if not os.path.isfile(self.settingfilename):
            config.add_section('MusicPlayer')
        config.set('MusicPlayer', 'PATH', self.cur_path)
        config.write(open(self.settingfilename, 'w'))

    '''提示'''
    def Tips(self, message):
        QMessageBox.about(self, "提示", message)

    def open_Dir(self):
        self.cur_path = QFileDialog.getExistingDirectory(self, "选取文件夹", self.cur_path)
        if self.cur_path:
            self.showMusicList()
            self.cur_playing_song = ''
            self.setCurPlaying()
            self.label.setText('00:00')
            self.label_2.setText('00:00')
            self.horizontalSlider.setSliderPosition(0)
            self.is_pause = True
            self.playStop.setText('播放')

    def showMusicList(self):
        self.listWidget.clear()
        # self.updateSetting()
        for song in os.listdir(self.cur_path):
            if song.split('.')[-1] in self.song_formats:
                self.songs_list_select.append([song, os.path.join(self.cur_path, song).replace('\\', '/')])
                self.listWidget.addItem(song)
        self.listWidget.setCurrentRow(0)
        if self.songs_list_select:
            self.cur_playing_song = self.songs_list_select[self.listWidget.currentRow()][-1]

    '''根据播放模式播放音乐'''
    def playByMode(self):
        if (not self.is_pause) and (not self.is_switching):
            self.horizontalSlider.setMinimum(0)
            self.horizontalSlider.setMaximum(self.player.duration())
            self.horizontalSlider.setValue(self.horizontalSlider.value() + 1000)
            self.label.setText(time.strftime('%M:%S', time.localtime(self.player.position() / 1000)))
            self.label_2.setText(time.strftime('%M:%S', time.localtime(self.player.duration() / 1000)))

            if (self.playType.currentIndex() == 0) and (not self.is_pause) and (not self.is_switching):
                if self.listWidget.count() == 0:
                    return
                if self.player.position() == self.player.duration():
                    self.nextMusic()
            elif (self.playType.currentIndex() == 1) and (not self.is_pause) and (not self.is_switching):
                if self.listWidget.count() == 0:
                    return
                if self.player.position() == self.player.duration():
                    self.is_switching = True
                    self.setCurPlaying()
                    self.horizontalSlider.setValue(0)
                    self.playMusic()
                    self.is_switching = False
            elif (self.playType.currentIndex() == 2) and (not self.is_pause) and (not self.is_switching):
                if self.listWidget.count() == 0:
                    return
                if self.player.position() == self.player.duration():
                    self.is_switching = True
                    self.listWidget.setCurrentRow(random.randint(0, self.qlist.count() - 1))
                    self.setCurPlaying()
                    self.horizontalSlider.setValue(0)
                    self.playMusic()
                    self.is_switching = False
    '''双击播放音乐'''
    def doubleClicked(self):
        self.horizontalSlider.setValue(0)
        self.is_switching=True
        self.setCurPlaying()
        self.playMusic()
        self.is_switching = False

    '''设置当前播放的音乐'''
    def setCurPlaying(self):
        self.cur_playing_song = self.songs_list_select[self.listWidget.currentRow()][-1]
        self.player.setMedia(QMediaContent(QUrl(self.cur_playing_song)))

    '''播放音乐'''
    def playMusic(self):
        if self.listWidget.count()==0:
            self.Tips('当前路径内无可播放的音乐文件')
            return
        if not self.player.isAudioAvailable():
            self.setCurPlaying()
        if self.is_switching or self.is_pause:
            self.player.play()
            self.is_pause = False
            self.playStop.setText('暂停')
        elif (not self.is_pause) and (not self.is_switching):
            self.player.pause()
            self.is_pause = True
            self.playStop.setText('播放')

    '''上一首'''
    def previewMusic(self):
        self.horizontalSlider.setValue(0)
        if self.listWidget.count() == 0:
            self.Tips('当前路径内无可播放的音乐文件')
            return
        pre_row = self.listWidget.currentRow() - 1 if self.listWidget.currentRow()!=0 else self.listWidget.count() - 1
        self.listWidget.setCurrentRow(pre_row)
        self.is_switching = True
        self.setCurPlaying()
        self.playMusic()
        self.is_switching = False

    '''下一首'''
    def nextMusic(self):
        self.horizontalSlider.setValue(0)
        if self.listWidget.count() == 0:
            self.Tips('当前路径内无可播放的音乐文件')
            return
        next_row = self.listWidget.currentRow() + 1 if self.listWidget.currentRow() != self.listWidget.count()-1 else 0
        self.listWidget.setCurrentRow(next_row)
        self.is_switching = True
        self.setCurPlaying()
        self.playMusic()
        self.is_switching = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())