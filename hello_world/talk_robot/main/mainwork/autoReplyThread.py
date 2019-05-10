import os

from PyQt5.QtCore import QThread,pyqtSignal
import itchat

class autoReplyThread(QThread):

    def __init__(self):
        getMsgSignal = pyqtSignal(str)
        super().__init__()

    def run(self):
        # 线程相关代码
        pass

    # 创建BuckUp文件夹
    if not os.path.exists(".\\BackUp\\"):
        os.mkdir('.\\BackUp\\')
    # 启动itchat()
    itchat.auto_login(hotReload=True)
    itchat.run()

# 创建一个新的线程
thread = autoReplyThread()
thread.start()