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
    goBackSign = 0
    filmFilterSign = 0
    autoReplySign = 0
    time = pyqtSignal()  # 提前申明
    sendWords = pyqtSignal()
    sendKeys = pyqtSignal()
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionsetting.triggered.connect(self.settingShow)
        self.introduction.clicked.connect(self.infoShow)
        self.auto_send.clicked.connect(self.autoSend)
        self.message_back.clicked.connect(self.goBack)
        self.film_filter.clicked.connect(self.filmFilter)
        self.auto_reply.clicked.connect(self.autoReply)
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
            if self.goBackSign == 0 and self.filmFilterSign == 0 and self.autoReplySign == 0:
                from hello_world.talk_robot.main.mainwork.autoSendThread import autoSend
                if self.autoSendSign == 0:
                    self.AutoSendWindow = MyAutoSendWindow()
                    if self.AutoSendWindow.exec_():
                        # 数据插入表格
                        time = int(self.AutoSendWindow.getTime())
                        sendWords = self.AutoSendWindow.getSendWords()
                        self.infomation_area.clear()
                        self.auto_send.setText('停止自动发送')
                        self.showMessage("自动发送助手已启动")
                        self.autoSendSign = 1
                        self.autoSendThread = autoSend()
                        self.time.connect(lambda: self.autoSendThread.setTime(time))#通过信号槽设置时间
                        self.time.emit()
                        self.sendWords.connect(lambda: self.autoSendThread.setSendWords(sendWords))#通过信号槽设置发送词
                        self.sendWords.emit()
                            self.autoSendThread.getMsgSignal.connect(self.showMessage)
                        self.autoSendThread.start()
                else:
                    self.auto_send.setText('定时发送设定')
                    self.showMessage("自动发送助手已终止")
                    self.autoSendSign = 0
                    self.autoSendThread.terminate()
                    del self.autoSendThread
                self.AutoSendWindow.destroy()
            else:
                self.Tips('请关闭其他功能')

        except Exception as e:
            pass

    # 防撤回子线程创建与毁灭
    def goBack(self):
        try:
            if self.autoSendSign == 0 and self.filmFilterSign == 0 and self.autoReplySign == 0:
                from hello_world.talk_robot.main.mainwork.goBackCatchThread import goBackCatch
                if self.goBackSign == 0:
                    self.goBackSign = 1
                    self.message_back.setText('关闭防撤回工具')
                    self.infomation_area.clear()
                    self.showMessage("防撤回助手已启动")
                    self.goBackCatchThread = goBackCatch()
                    self.goBackCatchThread.getMsgSignal.connect(self.showMessage)
                    self.goBackCatchThread.start()
                else:
                    self.goBackSign = 0
                    self.message_back.setText('开启防撤回工具')
                    self.showMessage("防撤回助手已终止")
                    self.goBackCatchThread.terminate()
                    del self.goBackCatchThread
            else:
                self.Tips('请关闭其他功能')
        except Exception as e:
            pass

    # 电影防剧透子线程创建与毁灭
    def filmFilter(self):
        try:
            if self.autoSendSign == 0 and self.goBackSign == 0 and self.autoReplySign == 0:
                from hello_world.talk_robot.main.mainwork.filmFilterThread import filmFilter
                if self.filmFilterSign == 0:
                    self.filmFilterSign = 1
                    self.film_filter.setText('关闭防剧透助手')
                    self.infomation_area.clear()
                    self.showMessage("防剧透助手已启动")
                    self.filmFilterThread = filmFilter()
                    self.filmFilterThread.getMsgSignal.connect(self.showMessage)
                    self.filmFilterThread.start()
                else:
                    self.filmFilterSign = 0
                    self.film_filter.setText('开启防剧透助手')
                    self.showMessage("防剧透助手已终止")
                    self.filmFilterThread.terminate()
                    del self.filmFilterThread
            else:
                self.Tips('请关闭其他功能')
        except Exception as e:
            pass

    # 自动回复子线程创建与毁灭
    def autoReply(self):
        try:
            if self.autoSendSign == 0 and self.filmFilterSign == 0 and self.goBackSign == 0:
                from hello_world.talk_robot.main.mainwork.autoReplyThread import autoReplyThread
                if self.autoReplySign == 0:
                    self.autoReplySign = 1
                    self.auto_reply.setText('关闭自动回复')
                    self.infomation_area.clear()
                    self.showMessage("自动回复已启动")
                    dict =self.loadCsv("config/keyword.csv")
                    self.autoReplyThread = autoReplyThread()
                    self.autoReplyThread.getMsgSignal.connect(self.showMessage)
                    self.sendKeys.connect(lambda: self.autoReplyThread.setDict(dict))  # 通过信号槽设置发送回复关键词
                    self.sendKeys.emit()
                    self.autoReplyThread.start()
                else:
                    self.autoReplySign = 0
                    self.auto_reply.setText('开启自动回复')
                    self.showMessage("自动回复已终止")
                    self.autoReplyThread.terminate()
                    del self.autoReplyThread
            else:
                self.Tips('请关闭其他功能')
        except Exception as e:
            pass

    # 读取csv配置文件
    def loadCsv(self, fileName):
        dict = {}
        with open(fileName, "r", encoding='utf-8') as fileInput:
            reader = csv.reader(fileInput)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                dict.update({row[0]: row[1]})
        return dict
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
            apiKey = conf.getOption("turing", "apikey")
            self.apiKeyEdit.setText(apiKey)
            enable = conf.getOption("turing", "enable")
            if enable == 'False':
                self.replace_close.setChecked(True)
            else:
                self.replace_open.setChecked(True)
            apipass = conf.decrypt(conf.getOption("turing", "apiPass"))
            self.apiPassEdit.setText(apipass)
        except Exception as e:
            self.Tips("系统异常，请重试")

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
            text=self.filterWordList.item(i).text()
            if text != '':
                list.append(text)
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

    # 保存配置文件
    def Save(self):
        list = []
        conf = config()
        for i in range(self.qunNameList.count()):
            list.append(self.qunNameList.item(i).text())
        conf.addoption('qun', 'name', conf.split(list))
        apikey = self.apiKeyEdit.text()
        conf.addoption('turing', 'apikey', apikey)
        apiPass = self.apiPassEdit.text()
        conf.addoption('turing', 'apiPass', conf.encrypt(apiPass))
        if self.replace_close.isChecked():
            conf.addoption('turing', 'enable', 'False')
        if self.replace_open.isChecked():
            conf.addoption('turing', 'enable', 'True')

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