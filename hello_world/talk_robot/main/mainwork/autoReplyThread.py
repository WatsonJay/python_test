from PyQt5.QtCore import QThread,pyqtSignal
import itchat

class autoReplyThread(QThread):

    def __init__(self):
        super().__init__()

    def run(self):
        # 线程相关代码
        pass

# 创建一个新的线程
thread = autoReplyThread()
thread.start()