import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from hello_world.talk_robot.main.gui import Ui_MainWindow
from hello_world.talk_robot.main.setting import Ui_settingDialog
from hello_world.talk_robot.main.intro import Ui_introDialog

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionsetting.triggered.connect(self.settingShow)
        self.introduction.clicked.connect(self.infoShow)
    def settingShow(self):
        setting.show()#打开设置窗口
    def infoShow(self):
        intro.show()#打开介绍窗口

class MySettingWindow(QDialog, Ui_settingDialog):
    def __init__(self, parent=None):
        super(MySettingWindow, self).__init__(parent)
        self.setupUi(self)

class MyIntroWindow(QDialog, Ui_introDialog):
    def __init__(self, parent=None):
        super(MyIntroWindow, self).__init__(parent)
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    setting = MySettingWindow()
    intro = MyIntroWindow()
    win.show()
    sys.exit(app.exec_())