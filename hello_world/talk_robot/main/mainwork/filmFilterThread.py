# -*- coding: utf-8 -*-
import os
import itchat
import jieba
from PyQt5.QtCore import QThread,pyqtSignal
from hello_world.talk_robot.main.config.config import config


MSGINFO = {}
FACEPACKAGE = None

from itchat.content import *

class filmFilter(QThread):
    getMsgSignal = pyqtSignal(str)

    def __init__(self):
        getMsgSignal = pyqtSignal(str)
        super().__init__()
        WARNING_KEYWORDS = []
        WARNING_REPLY = ''

    def run(self):

        @itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO, NOTE],
                             isFriendChat=True, isGroupChat=True, isMpChat=True)
        def text_replay(msg):
            if 'ActualNickName' in msg:
                msg_from_nickname = msg['ActualNickName']
                groups = itchat.get_chatrooms(update=True)
                for group in groups:
                    if msg['FromUserName'] == group['UserName'] and group['NickName'] == '谁是谁的谁':
                        if check_msg(msg.text):
                            self.getMsgSignal.emit('WARNING! 消息涉嫌剧透,现已自动屏蔽 FROM：{}'.format(group['NickName'] + '的' + msg_from_nickname))
                            # return WARNING_REPLY

        # 创建BuckUp文件夹
        if not os.path.exists(".\\BackUp\\"):
            os.mkdir('.\\BackUp\\')
        # 启动itchat()
        itchat.auto_login(hotReload=True)
        itchat.run()

        # 检测是否存在过滤关键词
        def check_msg(msg):
            keyword_list = jieba.cut(msg)
            for word in keyword_list:
                dict = filmFilter.filmDictBuild()
                for filmName, value in a.items():
                if word in self.WARNING_KEYWORDS:

                    return True
            return False

    @staticmethod
    def filmDictBuild():
        conf = config()
        dict = {}
        filmNames = conf.getSection()
        for filmName in filmNames:
            filterWords = conf.splitword(conf.getOption(filmName, "filterWord"))
            dict.update({filmName: filterWords})
        return dict

    def setfilmName(self,filmName):
        self.WARNING_REPLY = '我觉得你在搞{}的剧透，我就清个屏!!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'.format(filmName)
