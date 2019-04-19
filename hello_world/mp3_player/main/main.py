import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp,QMessageBox,QFileDialog
from hello_world.mp3_player.main.gui import Ui_musicPlayer

class MyMainWindow(QMainWindow, Ui_musicPlayer):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


    def openDir(self):
        self.cur_path = QFileDialog.getExistingDirectory(self, "选取文件夹", self.cur_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())