# -*- coding: utf-8 -*-
import os

from PyQt5.QtCore import QThread,pyqtSignal
import itchat
from itchat.content import *
from hello_world.talk_robot.main.config.config import config
from hello_world.talk_robot.main.mainwork.TuringAPI import talk


class autoReplyThread(QThread):
    getMsgSignal = pyqtSignal(str)
    def __init__(self):

        super().__init__()

    def run(self):

        @itchat.msg_register(TEXT, isGroupChat=True)
        def group_text(msg):
            msg_content = None
            if msg.isAt:
                groups = itchat.get_chatrooms(update=True)
                config_get = config()
                groups_selects = config_get.splitword(config_get.getOption('qun', 'name'))
                for group in groups:
                    if group['NickName'] in groups_selects:
                        msg_content = msg['']
                        if config_get.getOption('turing', 'enable') == 'True':
                           apiKey = config_get.getOption('turing', 'apikey')
                           msg_reply = talk(apiKey,msg_content,msg['FromUserName'])
                        else:
                            p=1
        # 创建BuckUp文件夹
        if not os.path.exists(".\\BackUp\\"):
            os.mkdir('.\\BackUp\\')
        # 启动itchat()
        itchat.auto_login(hotReload=True)
        itchat.run()
