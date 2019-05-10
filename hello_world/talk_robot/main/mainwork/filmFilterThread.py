# -*- coding: utf-8 -*-
import os
import itchat
from PyQt5.QtCore import QThread,pyqtSignal


MSGINFO = {}
FACEPACKAGE = None

from itchat.content import *

class filmFilter(QThread):

    def __init__(self):
        getMsgSignal = pyqtSignal(str)
        super().__init__()

    def run(self):


        # 创建BuckUp文件夹
        if not os.path.exists(".\\BackUp\\"):
            os.mkdir('.\\BackUp\\')
        # 启动itchat()
        itchat.auto_login(hotReload=True)
        itchat.run()
