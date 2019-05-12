# -*- coding: utf-8 -*-
import os
from time import sleep

from PyQt5.QtCore import QThread,pyqtSignal
from hello_world.talk_robot.main.config.config import config
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
            config_get =config()
            groups_selects= config_get.splitword(config_get.getOption('qun','name'))
            groups = itchat.get_chatrooms(update=True)
            while True:
                i = 0
                for group in groups:
                    if group['NickName'] in groups_selects:
                        itchat.send_msg("{}".format(self.message), group['UserName'])
                        i = i+1
                self.getMsgSignal.emit(self.message + "发送成功,合计发送"+str(len(groups_selects))+"个群,成功"+str(i)+"个,间隔"+ str(self.sleepTime) + "s")
                sleep(self.sleepTime)
        except Exception as e:
            pass

    def setTime(self,time):
        self.sleepTime = time

    def setSendWords(self,sendWords):
        self.message = sendWords