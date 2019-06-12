import random
from time import sleep

from PyQt5.QtCore import QThread, pyqtSignal


class Thread(QThread):
    getMsgSignal = pyqtSignal(int)
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(5):
            self.getMsgSignal.emit(random.randint(1,100))
            sleep(5)
