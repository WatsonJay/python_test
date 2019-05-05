import csv
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QTableWidgetItem
from hello_world.talk_robot.main.gui import Ui_MainWindow
from hello_world.talk_robot.main.setting import Ui_settingDialog
from hello_world.talk_robot.main.intro import Ui_introDialog
from hello_world.talk_robot.main.add_auto_word import Ui_WordDialog
from hello_world.talk_robot.main.add_film import Ui_FilmDialog
from hello_world.talk_robot.main.add_filter import Ui_FilterDialog
from hello_world.talk_robot.main.add_qun import Ui_QunDialog

#主页面
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionsetting.triggered.connect(self.settingShow)
        self.introduction.clicked.connect(self.infoShow)

    # 打开设置窗口
    def settingShow(self):
        self.settingWindow = MySettingWindow()
        self.settingWindow.exec_()
        self.settingWindow.destroy()

    # 打开介绍窗口
    def infoShow(self):
        self.introWindow = MyIntroWindow()
        self.introWindow.exec_()
        self.introWindow.destroy()

    def Tips(self, message):
        QMessageBox.about(self, "提示", message)

# 设置窗口
class MySettingWindow(QDialog, Ui_settingDialog):
    def __init__(self, parent=None):
        super(MySettingWindow, self).__init__(parent)
        self.setupUi(self)
        self.loadCsv("config/keyword.csv")
        self.add_word.clicked.connect(self.addwordShow)
        self.modif_word.clicked.connect(self.modwordShow)

    # 读取csv配置文件
    def loadCsv(self, fileName):
        with open(fileName, "r" , encoding='utf-8') as fileInput:
            reader = csv.reader(fileInput)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                for j in  range(len(row)):
                    self.tableWidget.setItem(rowPosition, j, QTableWidgetItem(row[j]))

    # 打开新增关键词窗口
    def addwordShow(self):
        self.wordWindow = MyWordWindow()
        if self.wordWindow.exec_():
            # 数据插入表格
            keyword = self.wordWindow.getKeyword()
            reply = self.wordWindow.getreply()
            line = ''
            self.modifyline(keyword,reply,line)
        self.wordWindow.destroy()

    # 打开编辑关键词窗口
    def modwordShow(self):
        if self.tableWidget.currentIndex().row() == -1:
            index = 0
        else:
            index = self.tableWidget.currentIndex().row()
        keyword =self.tableWidget.item(index,0).text()
        reply = self.tableWidget.item(index, 1).text()
        self.wordWindow = MyWordWindow()
        self.wordWindow.setKeyword(keyword)
        self.wordWindow.setreply(reply)
        if self.wordWindow.exec_():
            # 数据插入表格
            keyword = self.wordWindow.getKeyword()
            reply = self.wordWindow.getreply()
            line = index
            self.modifyline(keyword, reply, line)
        self.wordWindow.destroy()

    # 新增一行数据
    def modifyline(self,keyword,reply,line):
        if line == '':
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
        else:
            rowPosition = line
        self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(keyword))
        self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(reply))

# 介绍窗口
class MyIntroWindow(QDialog, Ui_introDialog):
    def __init__(self, parent=None):
        super(MyIntroWindow, self).__init__(parent)
        self.setupUi(self)

# 设置关键词窗口
class MyWordWindow(QDialog, Ui_WordDialog):
    def __init__(self, parent=None):
        super(MyWordWindow, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def getKeyword(self):
        return self.keyWord.text()

    def getreply(self):
        return self.reply.text()

    def setKeyword(self,keyword):
        return self.keyWord.setText(keyword)

    def setreply(self,reply):
        return self.reply.setText(reply)

# 电影窗口
class MyFilmWindow(QDialog, Ui_FilmDialog):
    def __init__(self, parent=None):
        super(MyFilmWindow, self).__init__(parent)
        self.setupUi(self)

# 电影过滤词窗口
class MyFilterindow(QDialog, Ui_FilterDialog):
    def __init__(self, parent=None):
        super(MyFilterindow, self).__init__(parent)
        self.setupUi(self)

# 群窗口
class MyQunWindow(QDialog, Ui_QunDialog):
    def __init__(self, parent=None):
        super(MyQunWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())