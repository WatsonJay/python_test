import random
from time import sleep

from PyQt5.QtCore import QThread, pyqtSignal


class Thread(QThread):
    getMsgSignal = pyqtSignal(int, int, int)
    def __init__(self):
        super().__init__()
        self.working = True

    def run(self):
        while self.working :
            self.getMsgSignal.emit(random.randint(1,100), random.randint(1,100), random.randint(1,100))
            sleep(1)

    def __del__(self):
        # 线程状态改变与线程终止
        self.working = False
        self.wait()
        self.terminate()