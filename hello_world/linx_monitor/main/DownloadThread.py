# -*- coding: utf-8 -*-
# @Author  : Jaywatson
# @File    : threadClass.py
# @Software: PyCharm
from time import sleep
import paramiko
from PyQt5.QtCore import QThread, pyqtSignal
from hello_world.linx_monitor.main.config.config import config
from hello_world.linx_monitor.main.server_controller import Monitor_server


class DownloadThread(QThread):
    sendSignal = pyqtSignal(float)
    sendExptionSignal = pyqtSignal(float)
    def __init__(self):
        super().__init__()
        self.infos = {}
        self.fileName = ''

    def run(self):
        try:
            t = paramiko.Transport((self.infos['ip'], int(self.infos['port'])))
            t.connect(username=self.infos['user'], password=self.infos['password'])
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.get('/home/monitor/'+self.fileName, 'temp/'+self.fileName, callback=self.callback)
            t.close()
        except Exception as e:
            self.sendExptionSignal.emit("SSH链接失败：[hostname:%s];[username:%s];[error:%s],请关闭tab页并检查配置" % (self.infos['ip'], self.infos['user'], e))

    def __del__(self):
        try:
            self.wait()
        except Exception as e:
            pass
        self.terminate()

    def getInfos(self, name):
        try:
            conf = config()
            infos = conf.sentionAll(name)
            infos['password'] = conf.decrypt(infos['password'])
            self.infos = infos
        except Exception as e:
            self.sendExptionSignal.emit("下载异常，请重试")

    def getfileName(self, fileName):
        self.fileName = fileName

    def callback(self, current, total):
        self.sendSignal.emit(int(current/total*100))
