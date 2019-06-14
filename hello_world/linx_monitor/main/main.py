# -*- coding: utf-8 -*-
# @Author  : Jaywatson
# @File    : main.py
# @Software: PyCharm
import sys
import time

from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QWidget
from PyQt5 import QtWidgets
import pyqtgraph as pg

from hello_world.linx_monitor.main.config.config import config
from hello_world.linx_monitor.main.threadClass import Thread
from hello_world.linx_monitor.main.ui.Config_Dialog import Ui_Config_Dialog
from hello_world.linx_monitor.main.ui.MonitorWindow import Ui_Monitor_Window
from hello_world.linx_monitor.main.ui.config import Ui_SysConfig_Dialog
from hello_world.linx_monitor.main.ui.info import info_Form
from hello_world.linx_monitor.main.ui.simple import Ui_simple_Form
from hello_world.linx_monitor.main.ui.user_helper import User_helper

# 主页面
class MyMainWindow(QMainWindow, Ui_Monitor_Window):
    # 初始化
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.loadConfig()
        self.actionshezhi.triggered.connect(self.sysConfigDialogShow)
        self.actioninfo.triggered.connect(self.infoShow)
        self.actionuse.triggered.connect(self.helperShow)
        self.serverAdd.clicked.connect(self.serverAdd_Open)
        self.serverModif.clicked.connect(self.serverModif_Open)
        self.serverDelete.clicked.connect(self.serverDel)
        self.server_listWidget.itemDoubleClicked.connect(self.showWidget)
        self.tabWidget.tabCloseRequested.connect(self.widget_Thread_close)

    # 读取系统配置
    def loadConfig(self):
        try:
            conf = config()
            SentionList = conf.getSection()
            self.server_listWidget.clear()
            self.server_listWidget.addItems(SentionList)
        except Exception as e:
            self.Tips("配置文件出现异常，请重置配置文件")

    # 打开介绍窗口
    def infoShow(self):
        self.infoShow = infoForm()
        self.infoShow.show()

    # 打开帮助窗口
    def helperShow(self):
        self.helperShow = userhelper()
        self.helperShow.show()

    # 打开系统设置窗口
    def sysConfigDialogShow(self):
        try:
            conf = config()
            self.sysConfigDialog = sysConfigDialog()
            if self.sysConfigDialog.exec_():
                infos = self.sysConfigDialog.getDict()
                conf.cmdSection('sysconfig', infos)
            self.sysConfigDialog.destroy()
        except Exception as e:
            self.Tips("保存配置异常，请稍后重试")

    # 打开新增服务器窗口
    def serverAdd_Open(self):
        try:
            conf = config()
            self.serverConfigDialog = serverConfigDialog()
            if self.serverConfigDialog.exec_():
                infos = self.serverConfigDialog.getDict()
                conf.cmdSection(infos['name'],infos)
            self.serverConfigDialog.destroy()
            self.loadConfig()
        except Exception as e:
            self.Tips("保存配置异常，请稍后重试")

    # 打开编辑服务器窗口
    def serverModif_Open(self):
        conf = config()
        self.serverConfigDialog = serverConfigDialog()
        sention = self.server_listWidget.item(self.server_listWidget.currentRow()).text()
        info = conf.sentionAll(sention)
        self.serverConfigDialog.setDict(info)
        self.serverConfigDialog.disableName()
        if self.serverConfigDialog.exec_():
            infos = self.serverConfigDialog.getDict()
            conf.cmdSection(infos['name'], infos)
        self.serverConfigDialog.destroy()
        self.loadConfig()

    # 打开删除服务器窗口
    def serverDel(self):
        conf = config()
        sention = self.server_listWidget.item(self.server_listWidget.currentRow()).text()
        msg = QMessageBox.question(self, "删除警告", "你确定删除吗？", QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)  # 这里是固定格式，yes/no不能动
        # 判断消息的返回值
        if msg == QMessageBox.Yes:
            conf.delSection(sention)
        else:
            return
        self.loadConfig()

    # 打开服务器监控窗口
    def showWidget(self):
        try:
            conf = config()
            self.serverConfigDialog = serverConfigDialog()
            sention = self.server_listWidget.item(self.server_listWidget.currentRow()).text()
            info = conf.sentionAll(sention)
            ip = info['ip']
            self.serverConfigDialog.setDict(info)
            self.serverConfigDialog.disable()
            if self.serverConfigDialog.exec_():
                self.tab = simpleForm()
                self.tab.setIp(ip)
                self.mointorThread = Thread()
                self.mointorThread.sendinfosSignal.connect(self.tab.set_data)
                self.mointorThread.sendExptionSignal.connect(self.tab.showMessage)
                self.tab.stop.connect(self.mointorThread.__del__)
                self.tab.name.connect(lambda: self.mointorThread.getInfos(sention))  # 通过信号槽设置名称
                self.tab.name.emit()
                self.tabWidget.addTab(self.tab, sention)
                self.tabWidget.setCurrentWidget(self.tab)
                self.mointorThread.start()
            self.serverConfigDialog.destroy()
        except Exception as e:
            self.Tips("配置文件出现异常，请重置配置文件")

    # 中止服务器监控页面线程窗口
    def widget_Thread_close(self, index):
        widget = self.tabWidget.widget(index)
        widget.stopThread()
        self.tabWidget.removeTab(index)

    # 提示窗口
    def Tips(self, message):
        QMessageBox.about(self, "提示", message)

# 服务器配置页面
class serverConfigDialog(QDialog, Ui_Config_Dialog):
    def __init__(self, parent=None):
        super(serverConfigDialog, self).__init__(parent)
        self.setupUi(self)

    def setDict(self, dict):
        conf = config()
        self.nameEdit.setText(dict['name'])
        self.ipEdit.setText(dict['ip'])
        self.portEdit.setText(dict['port'])
        self.userEdit.setText(dict['user'])
        self.passwordEdit.setText(conf.decrypt(dict['password']))

    def getDict(self):
        conf = config()
        info ={}
        info['name'] = self.nameEdit.text()
        info['ip'] = self.ipEdit.text()
        info['port'] = self.portEdit.text()
        info['user'] = self.userEdit.text()
        info['password'] = conf.encrypt(self.passwordEdit.text())
        return info

    def disableName(self):
        self.nameEdit.setDisabled(True)

    def disable(self):
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText('连接')
        self.nameEdit.setDisabled(True)
        self.ipEdit.setDisabled(True)
        self.portEdit.setDisabled(True)
        self.userEdit.setDisabled(True)
        self.passwordEdit.setDisabled(True)

# 性能监控统一页面
class simpleForm(QWidget,Ui_simple_Form):
    # 信号槽
    stop = pyqtSignal()
    name = pyqtSignal()
    # 初始化
    def __init__(self):
        self.cpu_list = []
        self.mem_list = []
        self.disk_list = []
        self.moveable = True
        super(simpleForm,self).__init__()
        self.setupUi(self)
        self.setWarnLine()
        self.move_slot = pg.SignalProxy(self.graph_widget.scene().sigMouseMoved, rateLimit=60, slot=self.print_slot)
        self.moveable_btn.clicked.connect(self.moveType)

    # 设置预警线
    def setWarnLine(self):
        conf = config()
        self.CpuHLine.setPos(int(conf.getOption('sysconfig','cpuwarnline')))
        self.MemHLine.setPos(int(conf.getOption('sysconfig', 'memwarnline')))
        self.DiskHLine.setPos(int(conf.getOption('sysconfig', 'diskwarnline')))

    # 填充ip
    def setIp(self, ip):
        self.ip_lineEdit.setText(ip)

    # 停止线程
    def stopThread(self):
        self.stop.emit()

    # 是否自动移动
    def moveType(self):
        if self.moveable == True:
            self.moveable_btn.setText('自动')
        else:
            self.moveable_btn.setText('锁定')
        self.moveable = bool(1-self.moveable)

    # 绘制数据图形
    def set_data(self,cpu,mem,dick):
        try:
            if len(self.cpu_list) > 13 and self.moveable == True:
                self.graph_widget.setXRange(len(self.cpu_list)-13, len(self.cpu_list)+2, padding=0)
            self.showMessage('采样正常')
            self.cpu_list.append(cpu)
            self.mem_list.append(mem)
            self.disk_list.append(dick)
            self.cpu_line.setData(self.cpu_list)
            self.memory_line.setData(self.mem_list)
            self.disk_line.setData(self.disk_list)
        except Exception as e:
            pass

    # 响应鼠标移动绘制光标
    def print_slot(self, event=None):
        if event is None:
            print("事件为空")
        else:
            pos = event[0]  # 获取事件的鼠标位置
            try:
                # 如果鼠标位置在绘图部件中
                if self.graph_widget.sceneBoundingRect().contains(pos):
                    mousePoint = self.graph_widget.plotItem.vb.mapSceneToView(pos)  # 转换鼠标坐标
                    index = int(mousePoint.x())  # 鼠标所处的X轴坐标
                    if 0 <= index <= len(self.cpu_list)-1:
                        # 在label中写入HTML
                        self.point_label.setHtml(
                            "<p style='color:white'>CPU：{0}%</p><p style='color:white'>内存：{1}%</p><p style='color:white'>磁盘：{2}%</p>".format(
                            self.cpu_list[index], self.mem_list[index], self.disk_list[index]))
                        self.point_label.setPos(mousePoint.x(), mousePoint.y())  # 设置label的位置
                        # 设置垂直线条和水平线条的位置组成十字光标
                        self.vLine.setPos(mousePoint.x())
            except Exception as e:
                pass

    # 显示日志
    def showMessage(self, msg):
        msg = "[" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "]" + msg
        self.info_borwser.append(msg)

# 系统设置页面
class sysConfigDialog(QDialog, Ui_SysConfig_Dialog):
    # 初始化
    def __init__(self, parent=None):
        super(sysConfigDialog, self).__init__(parent)
        self.setupUi(self)
        self.loadConfig()

    # 读取系统配置
    def loadConfig(self):
        try:
            conf = config()
            sysconfig = conf.sentionAll('sysconfig')
            self.CPU_spinBox.setValue(int(sysconfig['cpuwarnline']))
            self.MEM_spinBox.setValue(int(sysconfig['memwarnline']))
            self.DISK_spinBox.setValue(int(sysconfig['diskwarnline']))
            self.Simple_Rate_spinBox.setValue(int(sysconfig['simplerating']))
        except Exception as e:
            self.Tips("配置文件出现异常，请重置配置文件")

    def getDict(self):
        info ={}
        info['cpuwarnline'] = str(self.CPU_spinBox.value())
        info['memwarnline'] = str(self.MEM_spinBox.value())
        info['diskwarnline'] = str(self.DISK_spinBox.value())
        info['simplerating'] = str(self.Simple_Rate_spinBox.value())
        return info
    # 提示窗口
    def Tips(self, message):
        QMessageBox.about(self, "提示", message)

# 介绍页面
class infoForm(QWidget,info_Form):
    # 初始化
    def __init__(self, parent=None):
        super(infoForm, self).__init__(parent)
        self.setupUi(self)

# 帮助页面
class userhelper(QWidget, User_helper):
    # 初始化
    def __init__(self, parent=None):
        super(userhelper, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
