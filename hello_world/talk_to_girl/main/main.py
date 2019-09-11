import sys
import time

from PyQt5 import QtCore
from PyQt5.QtCore import QDate, QTime
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from hello_world.talk_to_girl.main.gui.gui import Ui_MainWindow
from hello_world.talk_to_girl.main.config.config import config


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.flag = False
        self.setupUi(self)
        self.loadConfig()

    # 无边框移动窗体
    def mousePressEvent(self, QMouseEvent):
        try:
            if QMouseEvent.button() == QtCore.Qt.LeftButton:
                self.flag = True
                self.m_Position = QMouseEvent.globalPos() - self.pos()
                QMouseEvent.accept()
                self.setCusor(QCursor(QtCore.Qt.OpenHandCursor))
        except Exception as e:
            pass

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.flag = False
        self.setCursor(QCursor(QtCore.Qt.ArrowCursor))

    # 加载配置文件
    def loadConfig(self):
        try:
            conf = config()
            self.wechatNameEdit.setText(conf.getOption("config", "wechat_name"))
            self.nickNameEdit.setText(conf.getOption("config", "nick_name"))
            self.birthMonthBox.setValue(int(conf.getOption("config", "bitrh_month")))
            self.birthDayBox.setValue(int(conf.getOption("config", "bitrh_day")))
            self.memDateEdit.setDate(QDate.fromString(conf.getOption("config", "mem_day"), 'yyyy-MM-dd'))
            self.wakeUpEdit.setTime(QTime.fromString(conf.getOption("config", "weak_time"), 'hh:mm'))
            self.lunchTimeEdit.setTime(QTime.fromString(conf.getOption("config", "lunch_time"), 'hh:mm'))
            self.dinnerTimeEdit.setTime(QTime.fromString(conf.getOption("config", "dinner_time"), 'hh:mm'))
            self.sleepTimeEdit.setTime(QTime.fromString(conf.getOption("config", "sleep_time"), 'hh:mm'))
            # self.wakeUpEdit.time().toString('hh:mm')
            # self.memDateEdit.date().toString('yyyy-MM-dd')
            enable = conf.getOption("config", "is_auto_talk")
            if enable == 'False':
                self.talkOffButton.setChecked(True)
            else:
                self.talkOnButton.setChecked(True)
            enable = conf.getOption("config", "is_weather")
            if enable == 'False':
                self.weatherOffButton.setChecked(True)
            else:
                self.weatherOnButton.setChecked(True)
            enable = conf.getOption("config", "is_emoji")
            if enable == 'False':
                self.emojiOffButton.setChecked(True)
            else:
                self.emojiOnButton.setChecked(True)
            self.valentineDayEdit.setText(conf.getOption("config", "valentine_Day"))
            self.birthDayEdit.setText(conf.getOption("config", "birth_Day"))
            self.christmasEdit.setText(conf.getOption("config", "christmas_Day"))
            self.womenDayEdit.setText(conf.getOption("config", "women_Day"))
            self.showMessage("系统配置加载完成")
        except Exception as e:
            self.Tips("系统异常，请重试")

    # 保存配置文件
    def Save(self):
        conf = config()
        conf.addoption('config', 'wechat_name', conf.split(list))
        conf.addoption('config', 'nick_name', apikey)
        conf.addoption('config', 'bitrh_month', conf.encrypt(apiPass))
        conf.addoption('config', 'nick_name', apikey)
        conf.addoption('config', 'nick_name', apikey)
        conf.addoption('config', 'nick_name', apikey)
        conf.addoption('config', 'nick_name', apikey)
        conf.addoption('config', 'nick_name', apikey)
        conf.addoption('config', 'nick_name', apikey)
        conf.addoption('config', 'nick_name', apikey)
        conf.addoption('config', 'nick_name', apikey)
        if self.replace_close.isChecked():
            conf.addoption('turing', 'enable', 'False')
        if self.replace_open.isChecked():
            conf.addoption('turing', 'enable', 'True')

    # 显示日志
    def showMessage(self, msg):
        msg = "[" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "]" + msg
        self.MsgBrowser.append(msg)

    def Tips(self, message):
        QMessageBox.about(self, "提示", message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())