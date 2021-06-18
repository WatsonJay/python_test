# -*- coding: utf-8 -*-
import datetime
import os
from time import sleep

from PyQt5.QtCore import QThread,pyqtSignal
from hello_world.talk_robot.main.config.config import config
import itchat

class autoSend(QThread):
    getMsgSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(autoSend, self).__init__(parent)
        self.timelist = []
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
                send = True

                time = datetime.datetime.now().strftime('%H:%M')
                if (time in self.timelist) and send:
                    send = False
                    for group in groups:
                        if group['NickName'] in groups_selects:
                            date = datetime.datetime.now().strftime('%m{}%d{} %H:00').format('月', '日')
                            itchat.send_msg("{}".format(self.message).format(date), group['UserName'])
                            i = i+1
                    self.getMsgSignal.emit("{}".format(self.message).format(date) + "发送成功,合计发送"+str(len(groups_selects))+"个群,成功"+str(i)+"个")
                else:
                    send = True
                sleep(59)
        except Exception as e:
            pass

    def setTime(self,time):
        self.timelist = time.split(",");

    def setSendWords(self,sendWords):
        self.message = sendWords