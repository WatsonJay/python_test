import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp,QMessageBox
from hello_world.pyqt_file_download.main.bugger import searchingflim
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
        if start == QMessageBox.Ok:
            self.page = 1
            pages = searchingflim(self.lineEdit.text(),"")
            if pages == "no such film":
                self.infoSearchNull()
            elif pages == "connect false":
                self.infoSearchError()
            else:
                for page in range(int(pages)):
                    filmList = searchingflim(self.lineEdit.text(), page+1)
                    self.writeDetailPage(filmList)
                self.infoSearchDone()
        # 取消爬取
        else:
            pass

            # 将数据显示到图形界面

    def writeDetailPage(self, filmList):
        for film in filmList:
            # 写入图形界面
            self.textEdit.append(
                "<div>"
                "<font color='red' size='3'>" + film["title"] + "</font>" + "\n"
                "<font color='orange' size='3'>第" + film["jishu"] + "集</font>" + "\n"
                "<font color='green' size='3'>下载链接：</font>" + "\n"
                "<font color='blue' size='3'>" +film["link"] + "</font>"+ "\n"
                "<font color='green' size='3'>下载大小：" +film["size"]+ "</font>"                                               
                "<p></p>"
                "</div>"
            )

    # 搜索不到结果的提示信息
    def infoSearchNull(self):
         QMessageBox.information(
             self, '提示', '搜索结果不存在，请重新输入搜索内容',
             QMessageBox.Ok, QMessageBox.Ok
         )

    # 爬取数据完毕的提示信息
    def infoSearchDone(self):
        QMessageBox.information(
            self, '提示', '爬取《' + self.lineEdit.text() + '》完毕',
            QMessageBox.Ok, QMessageBox.Ok
        )

    # 多页情况下是否继续爬取的提示信息
    def infoSearchError(self):
        QMessageBox.information(
            self, '提示', '爬取异常',
        QMessageBox.Ok, QMessageBox.Ok
                )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())