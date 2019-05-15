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
        self.dict ={}

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
                        group_id = msg['FromUserName']
                        if not group_id == group['UserName']:
                            continue
                        msg_content = msg['Text']
                        msg_fromUser = msg['ActualUserName']
                        msg_reply = ''
                        group_info = itchat.update_chatroom(group_id, detailedMember=True)
                        memberlist = group_info['MemberList']
                        group_Name = group['NickName']
                        for member in memberlist:
                            # 找到消息的发送者
                            if member['UserName'] == msg_fromUser:
                                # 否则显示成员自己修改的在群里的昵称
                                msg_fromUser = member['DisplayName']
                                if len(msg_fromUser) == 0:
                                    # 否则显示他微信号的昵称
                                    msg_fromUser = member['NickName']
                        if config_get.getOption('turing', 'enable') == 'True':
                            apiKey = config_get.getOption('turing', 'apikey')
                            msg_reply = talk(apiKey,msg_content,msg['FromUserName'])
                            itchat.send_msg('@{}\n{}'.format(msg_fromUser, msg_reply), msg['FromUserName'])
                            self.getMsgSignal.emit("已自动回复" + group_Name + "的消息")
                        else:
                            for key, value in self.dict.items():
                                if key in msg_content:
                                    msg_reply = value
                                    itchat.send_msg('@{}\n{}'.format(msg_fromUser, msg_reply), msg['FromUserName'])
                                    self.getMsgSignal.emit("已自动回复" + group_Name + "的消息")

        # 创建BuckUp文件夹
        if not os.path.exists(".\\BackUp\\"):
            os.mkdir('.\\BackUp\\')
        # 启动itchat()
        itchat.auto_login(hotReload=True)
        itchat.run()

    def setDict(self,dict):
        self.dict = dict