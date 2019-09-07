import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp,QMessageBox
from hello_world.talk_to_girl.UItoPY.gui import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())