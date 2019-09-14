import hashlib
import json
import random
import string
import time
from urllib.parse import quote

import itchat
import requests
from PyQt5.QtCore import QThread, pyqtSignal
from itchat.content import *

from hello_world.talk_to_girl.main.config.config import config


class wechatThread(QThread):
    getMsgSignal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(wechatThread, self).__init__(parent)

    def run(self):
        @itchat.msg_register([TEXT], isFriendChat=True, isGroupChat=True, isMpChat=True)
        def girl_msg(msg):
            config_get = config()
            if 'ActualNickName' in msg:
                return
            else:
                try:
                    msg_from = itchat.search_friends(userName=msg['FromUserName'])['RemarkName']
                    if not msg_from:
                        msg_from = itchat.search_friends(userName=msg['FromUserName'])['NickName']
                except:
                    msg_from = u'微信官方消息'
            friends = itchat.get_friends(update=True)
            for friend in friends:
                if msg_from == friend['UserName']:
                    if friend['RemarkName']:
                        msg_from = friend['RemarkName']
                    else:
                        msg_from = friend['NickName']
            if msg_from == config_get.getOption("config", "nick_name"):
                apiId = config_get.getOption('config', 'app_id')
                apiKey = config_get.getOption('config', 'app_key')
                polar = self.mood(msg['Text'],apiId,apiKey)
                if polar == 1:
                    self.getMsgSignal.emit("女友心情挺不错")
                if polar == 0:
                    self.getMsgSignal.emit("女友心情还行")
                if polar == -1:
                    self.getMsgSignal.emit("女友心情不好，快哄哄她")
                if config_get.getOption('config', 'is_auto_talk') == 'True':
                    answer = self.talk(msg['Text'],apiId,apiKey,msg_from)
                    itchat.send_msg('{}'.format(answer), msg['FromUserName'])
                    self.getMsgSignal.emit("已自动回复" + msg_from + "的消息")

        # 启动itchat()
        try:
            itchat.auto_login(hotReload=True)
        except:
            itchat.auto_login(hotReload=True, enableCmdQR=True)
        itchat.run()

    def parm(self,params,apiKey):
        sign_before = ''
        # 要对key排序再拼接
        for key in sorted(params):
            # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写。
            sign_before += '{}={}&'.format(key, quote(params[key], safe=''))
        # 将应用密钥以app_key为键名，拼接到字符串sign_before末尾
        sign_before += 'app_key={}'.format(apiKey)
        # 对字符串sign_before进行MD5运算，得到接口请求签名
        sign = self.curlmd5(sign_before)
        params['sign'] = sign
        return params

    def curlmd5(self,src):
        m = hashlib.md5(src.encode('UTF-8'))
        # 将得到的MD5值所有字符转换成大写
        return m.hexdigest().upper()

    def mood(self,text,apiId,apiKey):
        url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textpolar"
        app_id = apiId
        # 请求时间戳（秒级），用于防止请求重放（保证签名5分钟有效）
        t = time.time()
        time_stamp = str(int(t))
        # 请求随机字符串，用于保证签名不可预测
        nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        params = {'app_id': app_id,
                  'text': text,
                  'time_stamp': time_stamp,
                  'nonce_str': nonce_str,
                  }
        payload = self.parm(params,apiKey)
        r = requests.post(url, data=params)
        data = r.json()
        polar = data['data']['polar']
        return polar

    def talk(self,text,apiId,apiKey,msg_from):
        url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
        # 获取请求参数
        app_id = apiId
        # 请求时间戳（秒级），用于防止请求重放（保证签名5分钟有效）
        t = time.time()
        time_stamp = str(int(t))
        # 请求随机字符串，用于保证签名不可预测
        nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        params = {'app_id': app_id,
                  'question': text,
                  'time_stamp': time_stamp,
                  'nonce_str': nonce_str,
                  'session': msg_from
                  }
        payload = self.parm(params,apiKey)
        r = requests.post(url, data=payload)
        return r.json()["data"]["answer"]
