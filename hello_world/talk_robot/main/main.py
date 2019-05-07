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
from hello_world.talk_robot.main.config.config import config

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
        if self.settingWindow.exec_():
            self.Tips("通过")
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
    tempfilmName = []
    def __init__(self, parent=None):
        super(MySettingWindow, self).__init__(parent)
        self.setupUi(self)
        self.loadCsv("config/keyword.csv")
        self.loadConfig()
        self.add_word.clicked.connect(self.addwordShow)
        self.modif_word.clicked.connect(self.modwordShow)
        self.del_word.clicked.connect(self.delline)
        self.add_film.clicked.connect(self.addfilmName)
        self.del_film.clicked.connect(self.delfilmName)
        self.filmNameBox.currentTextChanged.connect(self.loadFilter)

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

    # 加载配置文件
    def loadConfig(self):
        try:
            conf = config()
            qunNames = conf.splitword(conf.getOption("qun","name"))
            filmNames = conf.getSection()
            for qunName in qunNames:
                if qunName != '':
                    self.qunNameList.addItem(qunName)
            for filmName in filmNames:
                if filmName != '':
                    self.filmNameBox.addItem(filmName)
        except Exception as e:
            pass

    def loadFilter(self):
        try:
            conf = config()
            index = self.filmNameBox.currentIndex()
            filmName = self.filmNameBox.itemText(index)
            filterWords = conf.splitword(conf.getOption(filmName,"filterWord"))
            for filterWord in filterWords:
                if filterWord != '':
                    self.filterWordList.addItem(filterWord)
        except Exception as e:
            pass

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
            return
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

    # 新增/修改自动回复一行数据
    def modifyline(self,keyword,reply,line):
        if line == '':
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
        else:
            rowPosition = line
        self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(keyword))
        self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(reply))

    # 删除自动回复一行数据
    def delline(self):
        if self.tableWidget.currentIndex().row() == -1:
            return
        else:
            index = self.tableWidget.currentIndex().row()
        msg = QMessageBox.question(self, "退出警告", "你确定退出吗？", QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)  # 这里是固定格式，yes/no不能动
        # 判断消息的返回值
        if msg == QMessageBox.Yes:
            self.tableWidget.removeRow(index)
        else:
            return

    # 打开新增电影名窗口
    def addfilmName(self):
        self.filmWindow = MyFilmWindow()
        if self.filmWindow.exec_():
            # 数据插入表格
            conf = config()
            filmName = self.filmWindow.getFilmName()
            self.tempfilmName.append(filmName)
            self.filmNameBox.addItem(filmName)
            conf.addSection(filmName)
        self.filmWindow.destroy()

    # 删除当前电影名
    def delfilmName(self):
        if self.filmNameBox.currentIndex() == -1:
            return
        index = self.filmNameBox.currentIndex()
        filmName = self.filmNameBox.itemText(index)
        if filmName != '---请选择---':
            conf = config()
            conf.delSection(filmName)
            self.filmNameBox.removeItem(index)

    def Tips(self, message):
        QMessageBox.about(self, "提示", message)

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

    def getKeyword(self):
        return self.keyWord.text()

    def getreply(self):
        return self.reply.toPlainText()

    def setKeyword(self,keyword):
        return self.keyWord.setText(keyword)

    def setreply(self,reply):
        return self.reply.setText(reply)

# 电影窗口
class MyFilmWindow(QDialog, Ui_FilmDialog):
    def __init__(self, parent=None):
        super(MyFilmWindow, self).__init__(parent)
        self.setupUi(self)

    def getFilmName(self):
        return self.filmName.text()



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