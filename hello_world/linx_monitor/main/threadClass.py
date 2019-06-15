# -*- coding: utf-8 -*-
# @Author  : Jaywatson
# @File    : threadClass.py
# @Software: PyCharm
from time import sleep

from PyQt5.QtCore import QThread, pyqtSignal
from hello_world.linx_monitor.main.config.config import config
from hello_world.linx_monitor.main.server_controller import Monitor_server


class Thread(QThread):
    sendinfosSignal = pyqtSignal(float, float, float)
    sendExptionSignal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        conf = config()
        self.time = int(conf.getOption('sysconfig','simplerating'))
        self.working = True
        self.infos = {}

    def run(self):
        try:
            monitor = Monitor_server()
            self.ssh = monitor.sshConnect(self.infos['ip'], int(self.infos['port']), self.infos['user'], self.infos['password'])
            while self.working :
                cpu_info = monitor.get_Cpu_info(self.ssh)
                Mem_info = monitor.get_mem_info(self.ssh)
                disk_info = monitor.get_disk_stat(self.ssh)
                self.sendinfosSignal.emit(cpu_info, Mem_info, disk_info)
                sleep(self.time)
        except Exception as e:
            self.sendExptionSignal.emit("SSH链接失败：[hostname:%s];[username:%s];[error:%s],请关闭tab页并检查配置" % (self.infos['ip'], self.infos['user'], e))

    def __del__(self):
        try:
            monitor = Monitor_server()
            # 线程状态改变与线程终止
            self.working = False
            monitor.sshClose(self.ssh)
            self.wait()
        except Exception as e:
            pass
        self.terminate()

    def getInfos(self,name):
        try:
            conf = config()
            infos = conf.sentionAll(name)
            infos['password'] = conf.decrypt(infos['password'])
            self.infos = infos
        except Exception as e:
            self.sendExptionSignal.emit("配置读取异常,请关闭tab页并检查配置")