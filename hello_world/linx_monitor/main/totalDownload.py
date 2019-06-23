# -*- coding: utf-8 -*-
# @Author  : Jaywatson
# @File    : threadClass.py
# @Software: PyCharm
from time import sleep
import paramiko
from PyQt5.QtCore import QThread, pyqtSignal
from hello_world.linx_monitor.main.config.config import config
from hello_world.linx_monitor.main.server_controller import Monitor_server


class TotalDownloadThread(QThread):
    sendDownMsgSignal = pyqtSignal(str,float)
    def __init__(self):
        super().__init__()
        self.name = ''
        self.serverList = []
        self.fileName =''

    def run(self):
        conf = config()
        for i in range(len(self.serverList)):
            try:
                infos = conf.sentionAll(self.serverList[i])
                infos['password'] = conf.decrypt(infos['password'])
                t = paramiko.Transport((infos['ip'], int(infos['port'])))
                t.connect(username=infos['user'], password=infos['password'])
                sftp = paramiko.SFTPClient.from_transport(t)
                sftp.stat('/home/monitor/'+self.fileName+str(i)+'.nmon')
                sftp.get('/home/monitor/'+self.fileName+str(i)+'.nmon', 'temp/'+self.fileName+str(i)+'.nmon')
                t.close()
                self.sendDownMsgSignal.emit('success', int((i+1) / len(self.serverList) * 100))
            except Exception as e:
                self.sendDownMsgSignal.emit('failed', 0.0)
                t.close()
                pass

    def __del__(self):
        try:
            self.wait()
        except Exception as e:
            pass
        self.terminate()

    def getInfos(self, name):
        self.serverList = name

    def getfileName(self, fileName):
        self.fileName = fileName

