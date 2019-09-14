import hashlib
import json
import random
import string
import time
from urllib.parse import quote

import itchat
import requests
from PyQt5.QtCore import QThread
from itchat.content import TEXT

from hello_world.talk_to_girl.main.config.config import config


class wechatThread(QThread):

    def __init__(self):
        super().__init__()

    def run(self):
        # 启动itchat()
        try:
            itchat.auto_login(hotReload=True)
        except:
            itchat.auto_login(hotReload=True, enableCmdQR=True)
        itchat.run()

        @itchat.msg_register([TEXT], isFriendChat=True, isGroupChat=True, isMpChat=True)
        def girl_msg(msg):
            config_get = config()
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
            if msg_from == config_get.getOption("config", "nick_name"):
                apiId = config_get.getOption('config', 'app_id')
                apiKey = config_get.getOption('config', 'app_key')
                polar = self.mood(msg['Text'],apiId,apiKey)
                if config_get.getOption('config', 'is_auto_talk') == 'True':
                    answer = self.talk(msg['Text'],apiId,apiKey)
                    itchat.send_msg('@{}\n{}'.format(msg_from, answer), msg['FromUserName'])
                    self.getMsgSignal.emit("已自动回复" + msg_from + "的消息")

    def parm(self,text,apiId,apiKey):
        global params
        #请求时间戳（秒级），用于防止请求重放（保证签名5分钟有效）
        t = time.time()
        time_stamp=int(t)
        # 请求随机字符串，用于保证签名不可预测
        nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        # 应用标志，这里修改成自己的id和key
        app_id = apiId
        app_key = apiKey
        params = {'app_id': app_id,
                  'text': text,
                  'time_stamp': time_stamp,
                  'nonce_str': nonce_str,
                  }
        sign_before = ''
        # 要对key排序再拼接
        for key in sorted(params):
            # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写。
            sign_before += '{}={}&'.format(key, quote(params[key], safe=''))
        # 将应用密钥以app_key为键名，拼接到字符串sign_before末尾
        sign_before += 'app_key={}'.format(app_key)
        # 对字符串sign_before进行MD5运算，得到接口请求签名
        sign = self.curlmd5(sign_before)
        params['sign'] = sign


    def curlmd5(src):
        m = hashlib.md5(src.encode('UTF-8'))
        # 将得到的MD5值所有字符转换成大写
        return m.hexdigest().upper()

    def mood(self,text,apiId,apiKey):
        url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textpolar"
        payload = self.parm(text,apiId,apiKey)
        r = requests.post(url, data=params)
        data = json.loads(r)
        polar = data['data']['polar']
        return polar

    def talk(self,text,apiId,apiKey):
        url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
        # 获取请求参数
        payload = self.parm(text,apiId,apiKey)
        r = requests.post(url, data=payload)
        return r.json()["data"]["answer"]
