# -*- coding: utf-8 -*-
import time

from PyQt5.QtCore import pyqtSignal

__author__ = 'Jaywatson'

import sys
import csv

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QTableWidgetItem
from hello_world.talk_robot.main.ui.gui import Ui_MainWindow
from hello_world.talk_robot.main.ui.setting import Ui_settingDialog
from hello_world.talk_robot.main.ui.intro import Ui_introDialog
from hello_world.talk_robot.main.ui.add_auto_word import Ui_WordDialog
from hello_world.talk_robot.main.ui.add_film import Ui_FilmDialog
from hello_world.talk_robot.main.ui.add_filter import Ui_FilterDialog
from hello_world.talk_robot.main.ui.add_qun import Ui_QunDialog
from hello_world.talk_robot.main.ui.auto_send_setting import Ui_auto_send_Dialog
from hello_world.talk_robot.main.config.config import config

#主页面
class MyMainWindow(QMainWindow, Ui_MainWindow):
    autoSendSign = 0
    time = pyqtSignal()  # 提前申明
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionsetting.triggered.connect(self.settingShow)
        self.introduction.clicked.connect(self.infoShow)
        self.auto_send.clicked.connect(self.autoSend)

    # 打开设置窗口
    def settingShow(self):
        self.settingWindow = MySettingWindow()
        if self.settingWindow.exec_():
            self.settingWindow.Save()
            self.settingWindow.writeCsv("config/keyword.csv")
            self.Tips("保存成功")
        else:
            self.settingWindow.tempDelete()
        self.settingWindow.destroy()

    # 打开介绍窗口
    def infoShow(self):
        self.introWindow = MyIntroWindow()
        self.introWindow.exec_()
        self.introWindow.destroy()

    #显示日志
    def showMessage(self, msg):
        msg = "["+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"]"+msg
        self.infomation_area.append(msg)

    #自动发送子线程创建与毁灭
    def autoSend(self):
        try:
            from hello_world.talk_robot.main.mainwork.autoSendThread import autoSend
            if self.autoSendSign == 0:
                self.auto_send.setText('停止自动发送')
                self.autoSendSign = 1
                self.autoSendThread = autoSend()
                self.time.connect(lambda:self.autoSendThread.setTime(20))
                self.time.emit()
                self.autoSendThread.getMsgSignal.connect(self.showMessage)
                self.autoSendThread.start()
            else:
                self.auto_send.setText('定时发送设定')
                self.autoSendSign = 0
                self.autoSendThread.terminate()
                del self.autoSendThread
        except Exception as e:
            pass

    def Tips(self, message):
        QMessageBox.about(self, "提示", message)

# 自动发送设置窗口
class MyAutoSendWindow(QDialog, Ui_auto_send_Dialog):
    def __init__(self, parent=None):
        super(MyAutoSendWindow, self).__init__(parent)
        self.setupUi(self)

    def getTime(self):
        return self.timeBox.text()

    def getSendWords(self):
        return self.sendWords.toPlainText()

    def setTime(self, time):
        return self.timeBox.setText(time)

    def setSendWords(self, sendword):
        return self.sendWords.setText(sendword)

# 设置窗口
class MySettingWindow(QDialog, Ui_settingDialog):
    tempfilmNames = []
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
        self.add_filter.clicked.connect(self.addFilterShow)
        self.modif_filter.clicked.connect(self.modFilterShow)
        self.del_filter.clicked.connect(self.delFilter)
        self.add_qun.clicked.connect(self.addQunShow)
        self.modif_qun.clicked.connect(self.modifQunShow)
        self.del_qun.clicked.connect(self.delQun)

    # 读取csv配置文件
    def loadCsv(self, fileName):
        with open(fileName, "r", encoding='utf-8') as fileInput:
            reader = csv.reader(fileInput)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                for j in range(len(row)):
                    self.tableWidget.setItem(rowPosition, j, QTableWidgetItem(row[j]))

    # 写入csv
    def writeCsv(self, fileName):
        with open(fileName, "w", encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)  # 先写入columns_name
            writer.writerow(["关键词", "回复"])
            for index in range(self.tableWidget.rowCount()):
                keyword = self.tableWidget.item(index, 0).text()
                reply = self.tableWidget.item(index, 1).text()
                writer.writerow([keyword, reply])

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

    # 加载过滤词
    def loadFilter(self):
        try:
            self.filterWordList.clear()
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
        msg = QMessageBox.question(self, "删除警告", "你确定删除吗？", QMessageBox.Yes | QMessageBox.No,
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
            self.tempfilmNames.append(filmName)
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
            if filmName in self.tempfilmNames:
                self.tempfilmNames.remove(filmName)
            conf.delSection(filmName)
            self.filmNameBox.removeItem(index)

    # 打开新增电影过滤词窗口
    def addFilterShow(self):
        self.filterWindow = MyFilterwindow()
        if self.filterWindow.exec_():
            # 数据插入表格
            Filter = self.filterWindow.getFilter()
            filmName=self.filmNameBox.itemText(self.filmNameBox.currentIndex())
            self.filterWordList.addItem(Filter)
            self.tempSave(filmName)
        self.filterWindow.destroy()

    # 打开编辑电影过滤词窗口
    def modFilterShow(self):
        self.filterWindow = MyFilterwindow()
        index = self.filterWordList.currentRow()
        filterWord = self.filterWordList.item(index).text()
        self.filterWindow.setFilter(filterWord)
        if self.filterWindow.exec_():
            # 数据插入表格
            Filter = self.filterWindow.getFilter()
            filmName = self.filmNameBox.itemText(self.filmNameBox.currentIndex())
            self.filterWordList.takeItem(index)
            self.filterWordList.addItem(Filter)
            self.tempSave(filmName)
        self.filterWindow.destroy()

    # 删除电影过滤词
    def delFilter(self):
        msg = QMessageBox.question(self, "删除警告", "你确定删除吗？", QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)  # 这里是固定格式，yes/no不能动
        # 判断消息的返回值
        if msg == QMessageBox.Yes:
            self.filterWordList.takeItem(self.filterWordList.currentRow())
        else:
            return

    #临时保存
    def tempSave(self,filmName):
        list = []
        conf = config()
        for i in range(self.filterWordList.count()):
            list.append(self.filterWordList.item(i).text())
        conf.addoption(filmName,'filterword',conf.split(list))

    #临时配置删除
    def tempDelete(self):
        conf = config()
        for tempfilmName in self.tempfilmNames:
            conf.delSection(tempfilmName)

    # 打开新增群名窗口
    def addQunShow(self):
        self.qunWindow = MyQunWindow()
        if self.qunWindow.exec_():
            # 数据插入表格
            qunName = self.qunWindow.getQunName()
            self.qunNameList.addItem(qunName)
        self.qunWindow.destroy()

    # 打开编辑群名窗口
    def modifQunShow(self):
        self.qunWindow = MyQunWindow()
        index = self.qunNameList.currentRow()
        qunName = self.qunNameList.item(index).text()
        self.qunWindow.setQunName(qunName)
        if self.qunWindow.exec_():
            # 数据插入表格
            qunName = self.qunWindow.getQunName()
            self.qunNameList.takeItem(index)
            self.qunNameList.addItem(qunName)
        self.qunWindow.destroy()

    # 群名删除
    def delQun(self):
        msg = QMessageBox.question(self, "删除警告", "你确定删除吗？", QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)  # 这里是固定格式，yes/no不能动
        # 判断消息的返回值
        if msg == QMessageBox.Yes:
            self.qunNameList.takeItem(self.qunNameList.currentRow())
        else:
            return

    # 临时保存
    def Save(self):
        list = []
        conf = config()
        for i in range(self.qunNameList.count()):
            list.append(self.qunNameList.item(i).text())
        conf.addoption('qun', 'name', conf.split(list))

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
class MyFilterwindow(QDialog, Ui_FilterDialog):
    def __init__(self, parent=None):
        super(MyFilterwindow, self).__init__(parent)
        self.setupUi(self)

    def getFilter(self):
        return self.filter.text()

    def setFilter(self,filterWord):
        return self.filter.setText(filterWord)

# 群窗口
class MyQunWindow(QDialog, Ui_QunDialog):
    def __init__(self, parent=None):
        super(MyQunWindow, self).__init__(parent)
        self.setupUi(self)

    def getQunName(self):
        return self.qunName.text()

    def setQunName(self,QunName):
        return self.qunName.setText(QunName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())