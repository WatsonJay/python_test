# -*- coding: utf-8 -*-
import os
import re
import sys
import time
import itchat
from PyQt5.QtCore import QThread,pyqtSignal

from itchat.content import *

MSGINFO = {}
FACEPACKAGE = None

class goBackCatch(QThread):
    getMsgSignal = pyqtSignal(str)
    def __init__(self):
        super(goBackCatch, self).__init__()

    @staticmethod
    def checkMsgInfo():
        need_del_msgs = []
        for msg in MSGINFO:
            msg_time_stay = int(time.time()) - MSGINFO[msg]['msg_send_time']
            if msg_time_stay > 180:
                need_del_msgs.append(msg)
        if need_del_msgs:
            for msg in need_del_msgs:
                MSGINFO.pop(msg)

    def run(self):
        # 处理接受到的消息
        @itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO, NOTE],
                             isFriendChat=True, isGroupChat=True, isMpChat=True)
        def saveReceiveMsg(msg):
            msg_receive_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if 'ActualNickName' in msg:
                msg_from_nickname = msg['ActualNickName']
                msg_from = msg_from_nickname
                msg_from_username = msg['ActualUserName']
                friends = itchat.get_friends(update=True)
                for friend in friends:
                    if msg_from_username == friend['UserName']:
                        if friend['RemarkName']:
                            msg_from = friend['RemarkName']
                        else:
                            msg_from = friend['NickName']
                groups = itchat.get_chatrooms(update=True)
                for group in groups:
                    if msg['FromUserName'] == group['UserName']:
                        group_name = group['NickName']
                        group_member = group['MemberCount']
                        break
                if not group_name:
                    group_name = u'未命名群聊'
                group_name = group_name + u'(%s)人' % str(group_member)
                msg_from = group_name + '-->' + msg_from
            else:
                try:
                    msg_from = itchat.search_friends(userName=msg['FromUserName'])['RemarkName']
                    if not msg_from:
                        msg_from = itchat.search_friends(userName=msg['FromUserName'])['NickName']
                except:
                    msg_from = u'微信官方消息'
            msg_send_time = msg['CreateTime']
            msg_id = msg['MsgId']
            msg_content = None
            msg_link = None
            if msg['Type'] == 'Text' or msg['Type'] == 'Friends':
                msg_content = msg['Text']
                self.getMsgSignal.emit('[TEXT/FRIENDS]%s:%s' % (msg_from,msg_content))
            elif msg['Type'] == 'Attachment' or msg['Type'] == 'Video' or msg['Type'] == 'Recording' or msg[
                'Type'] == 'Picture':
                msg_content = msg['FileName']
                msg['Text'](str(msg_content))
                self.getMsgSignal.emit('[Attachment/Video/Picture/Recording]%s: %s' % (msg_from,msg_content))
            # 位置信息
            elif msg['Type'] == 'Map':
                x, y, location = re.search("<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*",
                                           msg['OriContent']).group(1, 2, 3)
                if location is None:
                    msg_content = r"纬度:" + x.__str__() + ", 经度:" + y.__str__()
                else:
                    msg_content = r"" + location
                self.getMsgSignal.emit('[Map]%s: %s' % (msg_from,msg_content))
            # 分享的音乐/文章
            elif msg['Type'] == 'Sharing':
                msg_content = msg['Text']
                msg_link = msg['Url']
                self.getMsgSignal.emit('[Sharing]%s: %s' % (msg_from,msg_content))
            FACEPACKAGE = msg_content
            MSGINFO.update(
                {
                    msg_id: {
                        "msg_from": msg_from,
                        "msg_send_time": msg_send_time,
                        "msg_receive_time": msg_receive_time,
                        "msg_type": msg['Type'],
                        "msg_content": msg_content,
                        "msg_link": msg_link
                    }
                }
            )
            goBackCatch.checkMsgInfo()

        # 监听是否有消息撤回
        @itchat.msg_register(NOTE, isFriendChat=True, isGroupChat=True, isMpChat=True)
        def monitorMsg(msg):
            if u'撤回了一条消息' in msg['Content']:
                callBack_msg_id = re.search("\<msgid\>(.*?)\<\/msgid\>", msg['Content']).group(1)
                callBack_msg = MSGINFO.get(callBack_msg_id)
                if len(callBack_msg_id) < 11:
                    itchat.send_file(FACEPACKAGE, toUserName='filehelper')
                else:
                    prompt = u'+++' + callBack_msg.get('msg_from') + u'撤回了一条消息+++\n' \
                                                                     u'--消息类型：' + callBack_msg.get('msg_type') + '\n' \
                                                                                                                 u'--接收时间：' + callBack_msg.get(
                        'msg_receive_time') + '\n' \
                                              u'--消息内容：' + callBack_msg.get('msg_content')
                    if callBack_msg['msg_type'] == 'Sharing':
                        prompt += u'\n链接：' + callBack_msg.get('msg_link')
                    itchat.send_msg(str(prompt), toUserName='filehelper')
                    if callBack_msg['msg_type'] == 'Attachment' or callBack_msg['msg_type'] == "Video" or callBack_msg[
                        'msg_type'] == 'Picture' or callBack_msg['msg_type'] == 'Recording':
                        file = '@fil@%s' % (callBack_msg['msg_content'])
                        itchat.send(msg=file, toUserName='filehelper')
                        os.remove(callBack_msg['msg_content'])
                    self.getMsgSignal.emit('当前一条消息被撤回，已发送至文件助手')
                    MSGINFO.pop(callBack_msg_id)


        # 创建BuckUp文件夹
        if not os.path.exists(".\\BackUp\\"):
            os.mkdir('.\\BackUp\\')
        # 启动itchat()
        try:
            itchat.auto_login(hotReload=True)
        except:
            itchat.auto_login(hotReload=True, enableCmdQR=True)
        itchat.run()
