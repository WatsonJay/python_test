import os
import sys
import configparser
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp,QMessageBox,QFileDialog
from hello_world.mp3_player.main.gui import Ui_musicPlayer

class MyMainWindow(QMainWindow, Ui_musicPlayer):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.songs_list_select = []
        self.song_formats = ['mp3', 'm4a', 'flac', 'wav', 'ogg']
        self.settingfilename = 'setting.ini'
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.cur_playing_song = ''
        self.is_switching = False
        self.is_pause = True
        self.openDir.clicked.connect(self.open_Dir)

    def loadsetting(self):


    def savesetting(self):
        config = config

    def open_Dir(self):
        self.cur_path = QFileDialog.getExistingDirectory(self, "选取文件夹", self.cur_path)
        if self.cur_path:
            self.showMusicList()
            self.cur_playing_song = ''
            # self.setCurPlaying()
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

    '''提示'''
    def Tips(self, message):
        QMessageBox.about(self, "提示", message)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())