# -*- coding: utf-8 -*-
import os
from time import sleep

from PyQt5.QtCore import QThread,pyqtSignal
import itchat

class autoSend(QThread):
    getMsgSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(autoSend, self).__init__(parent)
        self.sleepTime = 10
        self.message = 'happy'

    def run(self):
        # 创建BuckUp文件夹
        if not os.path.exists(".\\BackUp\\"):
            os.mkdir('.\\BackUp\\')
        # 启动itchat()
        try:
            itchat.auto_login(hotReload=True)
        except:
            itchat.auto_login(hotReload=True, enableCmdQR=True)
        # itchat.run()

        try:
            for i in range(200000):
                itchat.send(msg= self.message, toUserName='filehelper')
                self.getMsgSignal.emit(self.message + "发送成功,间隔"+ str(self.sleepTime) + "s")
                sleep(self.sleepTime)
        except Exception as e:
            pass

    def setTime(self,time):
        self.sleepTime = time

    def setSendWords(self,sendWords):
        self.message = sendWords