import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp,QMessageBox
from hello_world.pyqt_file_download.main.gui import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        start = QMessageBox.information(
            self, '提示', '是否开始爬取《' + self.lineEdit.text() + "》",
                        QMessageBox.Ok | QMessageBox.No, QMessageBox.Ok
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())