# -*- coding: utf-8 -*-
# @Author  : Jaywatson
# @File    : main.py
# @Software: PyCharm
import os
import random
import sys
import time

import openpyxl as openpyxl
from openpyxl.styles import Font
from openpyxl.styles import PatternFill
from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QWidget, QFileDialog
from PyQt5 import QtWidgets
import pyqtgraph as pg

from hello_world.linx_monitor.main.DownloadThread import DownloadThread
from hello_world.linx_monitor.main.config.config import config
from hello_world.linx_monitor.main.nmon_data_deal import nmon_data_deal
from hello_world.linx_monitor.main.threadClass import Thread
from hello_world.linx_monitor.main.ui.Config_Dialog import Ui_Config_Dialog
from hello_world.linx_monitor.main.ui.MonitorWindow import Ui_Monitor_Window
from hello_world.linx_monitor.main.ui.analysis import Ui_nmonAnalysis_Form
from hello_world.linx_monitor.main.ui.config import Ui_SysConfig_Dialog
from hello_world.linx_monitor.main.ui.info import info_Form
from hello_world.linx_monitor.main.ui.simple import Ui_simple_Form
from hello_world.linx_monitor.main.ui.timer_Dialog import Ui_timer_Dialog
from hello_world.linx_monitor.main.ui.totalRun import Ui_totalRun_Form
from hello_world.linx_monitor.main.ui.totalanalysis import Ui_totanl_Form
from hello_world.linx_monitor.main.ui.user_helper import User_helper
from hello_world.linx_monitor.main.server_controller import Monitor_server


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
        self.actionnmon.triggered.connect(self.analysis_show)
        self.actionnmon_2.triggered.connect(self.totalRunShow)
        self.actiontoatalAnalysis.triggered.connect(self.totalAnalysisShow)
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

    # 打开批量运行窗口
    def totalRunShow(self):
        self.total_run_form = total_run_form()
        self.total_run_form.exec_()
        self.total_run_form.destroy()

    # 打开批量分析窗口
    def totalAnalysisShow(self):
        self.total_analysis_form = total_analysis_form()
        self.total_analysis_form.exec_()
        self.total_analysis_form.destroy()

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
                conf.cmdSection(infos['name'], infos)
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
        try:
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
        except:
            pass

    # 打开服务器监控窗口
    def showWidget(self):
        try:
            conf = config()
            sention = self.server_listWidget.item(self.server_listWidget.currentRow()).text()
            info = conf.sentionAll(sention)
            ip = info['ip']
            self.serverConfigDialog = serverConfigDialog()
            self.serverConfigDialog.setDict(info)
            self.serverConfigDialog.disable()
            if self.serverConfigDialog.exec_():
                self.tab = simpleForm()
                self.tab.setIp(ip)
                self.tab.name = sention
                self.tab.checknmon()
                self.mointorThread = Thread()
                self.mointorThread.sendinfosSignal.connect(self.tab.set_data)
                self.mointorThread.sendExptionSignal.connect(self.tab.showMessage)
                self.tab.stop.connect(self.mointorThread.__del__)
                self.tab.nameSignal.connect(lambda: self.mointorThread.getInfos(sention))  # 通过信号槽设置名称
                self.tab.nameSignal.emit()
                self.tabWidget.addTab(self.tab, sention)
                self.tabWidget.setCurrentWidget(self.tab)
                self.mointorThread.start()
            self.serverConfigDialog.destroy()
        except Exception as e:
            self.Tips("线程启动异常，请重试或联系管理员")

    # 中止服务器监控页面线程窗口
    def widget_Thread_close(self, index):
        widget = self.tabWidget.widget(index)
        widget.stopThread()
        self.tabWidget.removeTab(index)

    # 打开分析窗口
    def analysis_show(self):
        self.analysisShow = analysis_form()
        self.analysisShow.show()
        self.analysisShow.loadfile('')

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
        info = {}
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
class simpleForm(QWidget, Ui_simple_Form):
    # 信号槽
    Downstop = pyqtSignal()
    stop = pyqtSignal()
    nameSignal = pyqtSignal()
    fileNameSignal = pyqtSignal()

    # 初始化
    def __init__(self):
        self.cpu_list = []
        self.mem_list = []
        self.disk_list = []
        self.name = ''
        self.fileName = ''
        self.moveable = True
        super(simpleForm, self).__init__()
        self.setupUi(self)
        self.timer = QTimer(self)
        self.setWarnLine()
        self.visableUploadChange()
        self.visabledownloadChange()
        self.start_record.setDisabled(True)
        self.download_record.setDisabled(True)
        self.analysis_record.setDisabled(True)
        self.move_slot = pg.SignalProxy(self.graph_widget.scene().sigMouseMoved, rateLimit=60, slot=self.print_slot)
        self.upload_nmon.clicked.connect(self.uploadfile)
        self.moveable_btn.clicked.connect(self.moveType)
        self.start_record.clicked.connect(self.record_command)
        self.timer.timeout.connect(self.nmon_finished)
        self.download_record.clicked.connect(self.nmon_download)
        self.analysis_record.clicked.connect(self.analysis_show)

    # 设置预警线
    def setWarnLine(self):
        conf = config()
        self.CpuHLine.setPos(int(conf.getOption('sysconfig', 'cpuwarnline')))
        self.MemHLine.setPos(int(conf.getOption('sysconfig', 'memwarnline')))
        self.DiskHLine.setPos(int(conf.getOption('sysconfig', 'diskwarnline')))

    # 切换上传可见状态
    def visableUploadChange(self):
        self.upload_label.setHidden(bool(1 - self.upload_label.isHidden()))
        self.upload_progressBar.setHidden(bool(1 - self.upload_progressBar.isHidden()))

    # 切换下载可见状态
    def visabledownloadChange(self):
        self.download_label.setHidden(bool(1 - self.download_label.isHidden()))
        self.download_progressBar.setHidden(bool(1 - self.download_progressBar.isHidden()))

    # 填充ip
    def setIp(self, ip):
        self.ip_lineEdit.setText(ip)

    # 检测文件存在
    def checknmon(self):
        try:
            conf = config()
            infos = conf.sentionAll(self.name)
            monitor = Monitor_server()
            ssh = monitor.sshConnect(infos['ip'], int(infos['port']), infos['user'], conf.decrypt(infos['password']))
            nmon_checked = monitor.nmon_checked(ssh)
            if nmon_checked:
                self.nmon_label.setText('当前服务器已安装nmon，可进行性能监控')
                self.upload_nmon.setDisabled(True)
                self.start_record.setDisabled(False)
            else:
                self.nmon_label.setText('当前服务器未安装nmon，请点击上传')
            monitor.sshClose(ssh)
        except Exception as e:
            self.showMessage(str(e))
            pass

    # 上传文件
    def uploadfile(self):
        try:
            conf = config()
            infos = conf.sentionAll(self.name)
            monitor = Monitor_server()
            text = monitor.sftp_upload_file(infos['ip'], int(infos['port']), infos['user'],
                                            conf.decrypt(infos['password']))
            if text == '上传成功':
                self.showMessage('文件已上传')
                self.nmon_label.setText('当前服务器已安装nmon，可进行性能监控')
                self.upload_nmon.setDisabled(True)
                self.start_record.setDisabled(False)
            else:
                self.nmon_label.setText('当前服务器安装nmon失败，请点击再次上传')
        except Exception as e:
            self.showMessage(str(e))
            pass

    # 启动nmon记录
    def record_command(self):
        try:
            self.download_record.setDisabled(True)
            self.timerDialog = timerDialog()
            if self.timerDialog.exec_():
                nmon_infos = self.timerDialog.getInfos()
                conf = config()
                infos = conf.sentionAll(self.name)
                monitor = Monitor_server()
                ssh = monitor.sshConnect(infos['ip'], int(infos['port']), infos['user'],
                                         conf.decrypt(infos['password']))
                get_msgs = monitor.nmon_run(ssh, nmon_infos['name'], nmon_infos['time'], nmon_infos['tap'])
                self.showMessage(get_msgs)
                self.start_record.setDisabled(True)
                self.record_name.setText(nmon_infos['name'] + '.nmon')
                self.fileName = nmon_infos['name'] + '.nmon'
                self.timer.start((int(nmon_infos['time']) * int(nmon_infos['tap']) + 1) * 1000)
            self.timerDialog.destroy()
        except Exception as e:
            self.showMessage(str(e))
            pass

    # 返回nmon记录
    def nmon_finished(self):
        self.start_record.setDisabled(False)
        self.download_record.setDisabled(False)
        self.showMessage('nmon运行结束')
        self.timer.stop()

    # 下载nmon记录
    def nmon_download(self):
        try:
            self.visabledownloadChange()
            self.DownloadThread = DownloadThread()
            self.nameSignal.connect(lambda: self.DownloadThread.getInfos(self.name))
            self.fileNameSignal.connect(lambda: self.DownloadThread.getfileName(self.fileName))
            self.Downstop.connect(self.DownloadThread.__del__)
            self.DownloadThread.sendDownExptionSignal.connect(self.showMessage)
            self.DownloadThread.sendSignal.connect(self.showProcess)
            self.nameSignal.emit()
            self.fileNameSignal.emit()
            self.DownloadThread.start()
        except Exception as e:
            self.showMessage(str(e))
            pass

    # 下载进度
    def showProcess(self, value):
        self.download_progressBar.setValue(value)
        if value == 100:
            self.visabledownloadChange()
            self.analysis_record.setDisabled(False)
            self.Downstop.emit()

    # 停止线程
    def stopThread(self):
        self.stop.emit()

    # 打开分析页
    def analysis_show(self):
        self.analysisShow = analysis_form()
        self.analysisShow.show()
        self.analysisShow.loadfile('temp/' + self.fileName)

    # 是否自动移动
    def moveType(self):
        if self.moveable == True:
            self.moveable_btn.setText('自动')
        else:
            self.moveable_btn.setText('锁定')
        self.moveable = bool(1 - self.moveable)

    # 绘制数据图形
    def set_data(self, cpu, mem, dick):
        try:
            if len(self.cpu_list) > 13 and self.moveable == True:
                self.graph_widget.setXRange(len(self.cpu_list) - 13, len(self.cpu_list) + 2, padding=0)
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
                    if 0 <= index <= len(self.cpu_list) - 1:
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
        if "文件下载异常" in msg:
            self.visabledownloadChange()


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
            self.password_lineEdit.setText(conf.decrypt(sysconfig['password']))
        except Exception as e:
            self.Tips("配置文件出现异常，请重置配置文件")

    # 保存系统配置
    def getDict(self):
        conf = config()
        info = {}
        info['cpuwarnline'] = str(self.CPU_spinBox.value())
        info['memwarnline'] = str(self.MEM_spinBox.value())
        info['diskwarnline'] = str(self.DISK_spinBox.value())
        info['simplerating'] = str(self.Simple_Rate_spinBox.value())
        info['password'] = conf.encrypt(self.password_lineEdit.text())
        return info

    # 提示窗口
    def Tips(self, message):
        QMessageBox.about(self, "提示", message)


# 介绍页面
class infoForm(QWidget, info_Form):
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


# nmon启动参数页面
class timerDialog(QDialog, Ui_timer_Dialog):
    # 初始化
    def __init__(self, parent=None):
        super(timerDialog, self).__init__(parent)
        self.setupUi(self)

    def getInfos(self):
        infos = {}
        infos['time'] = str(self.time_spinBox.value())
        infos['tap'] = str(self.tap_spinBox.value())
        infos['name'] = self.fileName_lineEdit.text()
        return infos


# 分析页面
class analysis_form(QWidget, Ui_nmonAnalysis_Form):
    # 初始化
    def __init__(self, parent=None):
        super(analysis_form, self).__init__(parent)
        self.setupUi(self)
        self.prepare_list = locals()
        self.cwd = os.getcwd()
        self.cpu_user = []
        self.cpu_sys = []
        self.cpu_Idle = []
        self.mem = []
        self.disk_info = {}
        self.iops = []
        self.net_read = []
        self.net_write = []
        self.len = 0
        self.pushButton_2.clicked.connect(self.calculation_again)
        self.analysis_pushButton.clicked.connect(lambda: self.loadfile(''))
        self.pushButton_4.clicked.connect(self.write07Excel)
        self.cpu_move_slot = pg.SignalProxy(self.cpu_widget.scene().sigMouseMoved, rateLimit=60,
                                            slot=self.print_cpu_slot)
        self.mem_move_slot = pg.SignalProxy(self.mem_widget.scene().sigMouseMoved, rateLimit=60,
                                            slot=self.print_mem_slot)
        self.iops_move_slot = pg.SignalProxy(self.iops_widget.scene().sigMouseMoved, rateLimit=60,
                                             slot=self.print_iops_slot)
        self.net_move_slot = pg.SignalProxy(self.net_widget.scene().sigMouseMoved, rateLimit=60,
                                            slot=self.print_net_slot)
        self.disk_move_slot = pg.SignalProxy(self.disk_widget.scene().sigMouseMoved, rateLimit=60,
                                             slot=self.print_disk_slot)

    def loadfile(self, filePath):
        try:
            if filePath == '':
                filePath, fileType = QFileDialog.getOpenFileName(self, "选取文件", "temp/", "nmon文件 (*.nmon);;所有文件 (*)")
            if filePath == '':
                return
            nmon = nmon_data_deal()
            self.textBrowser.clear()
            infos = nmon.file_read(filePath)
            self.analysis(infos)
            self.calculation(1, self.len)
            self.fileName_lineEdit.setText(filePath)
            self.simpleNum_label.setText(str(self.len) + '次')
            self.UI_init()
        except Exception as e:
            self.Tips('nmon文件解析异常，请重试')
            self.close()

    def analysis(self, infos):
        for cpu in infos['cpu']:
            self.cpu_user.append(cpu[0])
            self.cpu_sys.append(cpu[1])
            self.cpu_Idle.append(cpu[2])
        for mem in infos['mem']:
            self.mem.append(round((mem[0] - mem[1] - mem[2] - mem[3]) / mem[0] * 100, 3))
        for net in infos['NET']:
            self.net_read.append(round(net[0] / 128, 3))
            self.net_write.append(round(net[1] / 128, 3))
        self.disk_info['diskName'] = infos['diskName']
        for diskName in infos['diskName']:
            self.disk_info[diskName + '_DISKBUSY'] = infos[diskName + '_DISKBUSY']
        self.iops = infos['DISKXFER']
        self.len = infos['simpleNumber']
        self.ip_lineEdit.setText(infos['ip'])
        self.infoShow('当前系统版本：' + infos['os'])

    def UI_init(self):
        self.star_spinBox.setMinimum(1)
        self.star_spinBox.setMaximum(self.len - 1)
        self.end_spinBox.setMinimum(2)
        self.end_spinBox.setMaximum(self.len)
        self.end_spinBox.setValue(self.len)
        self.cpu_user_line.setData(self.cpu_user)
        self.cpu_sys_line.setData(self.cpu_sys)
        self.cpu_idle_line.setData(self.cpu_Idle)
        self.mem_line.setData(self.mem)
        self.iops_line.setData(self.iops)
        self.net_read_line.setData(self.net_read)
        self.net_write_line.setData(self.net_write)
        for diskName in self.disk_info['diskName']:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self.prepare_list[diskName + '_line'] = self.disk_widget.plot(pen=(r, g, b), name=diskName,
                                                                          symbolBrush=(r, g, b))
            self.prepare_list[diskName + '_line'].setData(self.disk_info[diskName + '_DISKBUSY'])

    def calculation_again(self):
        self.calculation(self.star_spinBox.value(), self.end_spinBox.value())

    # 计算平均值
    def calculation(self, start, end):
        cpu_temp = 0
        mem_temp = 0
        net_temp = 0
        IOPS_temp = 0
        temp1 = 0
        disk_temp = 0
        count = 0
        for i in range(start - 1, end):
            cpu_temp += self.cpu_user[i] + self.cpu_sys[i]
            mem_temp += self.mem[i]
            net_temp += self.net_read[i] + self.net_write[i]
            IOPS_temp += self.iops[i]
        for disk_name in self.disk_info['diskName']:
            temp1 = 0
            for i in range(start - 1, end):
                temp1 += self.disk_info[disk_name + '_DISKBUSY'][i]
            if round(temp1 / (end - start + 1), 2) != 0.0:
                disk_temp += temp1
                count += 1
        if count == 0:
            count = 1
        self.cpu_label.setText(str(round(cpu_temp / (end - start + 1), 2)) + '%')
        self.men_label.setText(str(round(mem_temp / (end - start + 1), 2)) + '%')
        self.disk_label.setText(str(round(disk_temp / count / (end - start + 1), 2)) + '%')
        self.net_label.setText(str(round(net_temp / (end - start + 1), 2)) + 'Mbps')
        self.IOPS_label.setText(str(round(IOPS_temp / (end - start + 1), 2)) + '次')

    # 导出
    def write07Excel(self):
        try:
            wb = openpyxl.Workbook()
            sheet = wb.active
            sheet.title = self.ip_lineEdit.text() + '统计表'
            value = [[self.label_7.text(), self.label_9.text(), self.label_13.text(), self.label_11.text(),
                      self.label_16.text()],
                     [self.cpu_label.text(), self.men_label.text(), self.disk_label.text(), self.net_label.text(),
                      self.IOPS_label.text()]]
            for i in range(0, 2):
                for j in range(0, len(value[i])):
                    sheet.cell(row=i + 1, column=j + 1, value=str(value[i][j]))
            filePath, ok2 = QFileDialog.getSaveFileName(self,
                                                        "文件保存",
                                                        "temp/",
                                                        "Xlsx Files (*.xlsx);;All Files (*)")
            if filePath == '':
                return
            wb.save(filePath)
            self.Tips('写入数据成功！')
        except Exception as e:
            self.Tips('导出execl异常，请重试')

    # 消息显示
    def infoShow(self, msg):
        self.textBrowser.append(msg)

    # 提示窗口
    def Tips(self, message):
        QMessageBox.about(self, "提示", message)

    # CPU光标
    def print_cpu_slot(self, event=None):
        if event is None:
            print("事件为空")
        else:
            pos = event[0]  # 获取事件的鼠标位置
            try:
                # 如果鼠标位置在绘图部件中
                if self.cpu_widget.sceneBoundingRect().contains(pos):
                    mousePoint = self.cpu_widget.plotItem.vb.mapSceneToView(pos)  # 转换鼠标坐标
                    index = int(mousePoint.x())  # 鼠标所处的X轴坐标
                    if 0 <= index < self.len:
                        # 在label中写入HTML
                        self.cpu_point_label.setHtml(
                            "<p style='color:white'>CPU用户使用率：{0}%</p><p style='color:white'>CPU系统使用率：{1}%</p><p style='color:white'>CPU空闲率：{2}%</p>".format(
                                self.cpu_user[index], self.cpu_sys[index], self.cpu_Idle[index]))
                        self.cpu_point_label.setPos(mousePoint.x(), mousePoint.y())  # 设置label的位置
                        # 设置垂直线条和水平线条的位置组成十字光标
                        self.cpu_vLine.setPos(mousePoint.x())
            except Exception as e:
                pass

    # mem光标
    def print_mem_slot(self, event=None):
        if event is None:
            print("事件为空")
        else:
            pos = event[0]  # 获取事件的鼠标位置
            try:
                # 如果鼠标位置在绘图部件中
                if self.mem_widget.sceneBoundingRect().contains(pos):
                    mousePoint = self.mem_widget.plotItem.vb.mapSceneToView(pos)  # 转换鼠标坐标
                    index = int(mousePoint.x())  # 鼠标所处的X轴坐标
                    if 0 <= index < len(self.mem):
                        # 在label中写入HTML
                        self.mem_point_label.setHtml(
                            "<p style='color:white'>内存用户使用率：{}%</p>".format(
                                self.mem[index]))
                        self.mem_point_label.setPos(mousePoint.x(), mousePoint.y())  # 设置label的位置
                        # 设置垂直线条和水平线条的位置组成十字光标
                        self.mem_vLine.setPos(mousePoint.x())
            except Exception as e:
                pass

    # disk光标
    def print_disk_slot(self, event=None):
        if event is None:
            print("事件为空")
        else:
            pos = event[0]  # 获取事件的鼠标位置
            try:
                # 如果鼠标位置在绘图部件中
                if self.disk_widget.sceneBoundingRect().contains(pos):
                    mousePoint = self.disk_widget.plotItem.vb.mapSceneToView(pos)  # 转换鼠标坐标
                    index = int(mousePoint.x())  # 鼠标所处的X轴坐标
                    html = ""
                    if 0 <= index < len(self.mem):
                        for diskName in self.disk_info['diskName']:
                            html += "<p style='color:white'>{0}使用率：{1}%</p>".format(diskName, self.disk_info[
                                diskName + '_DISKBUSY'][index])
                        # 在label中写入HTML
                        self.disk_point_label.setHtml(html)
                        self.disk_point_label.setPos(mousePoint.x(), mousePoint.y())  # 设置label的位置
                        # 设置垂直线条和水平线条的位置组成十字光标
                        self.disk_vLine.setPos(mousePoint.x())
            except Exception as e:
                pass

    # IOPS光标
    def print_iops_slot(self, event=None):
        if event is None:
            print("事件为空")
        else:
            pos = event[0]  # 获取事件的鼠标位置
            try:
                # 如果鼠标位置在绘图部件中
                if self.iops_widget.sceneBoundingRect().contains(pos):
                    mousePoint = self.iops_widget.plotItem.vb.mapSceneToView(pos)  # 转换鼠标坐标
                    index = int(mousePoint.x())  # 鼠标所处的X轴坐标
                    if 0 <= index < len(self.iops):
                        # 在label中写入HTML
                        self.iops_point_label.setHtml(
                            "<p style='color:white'>IO/sec：{}次</p>".format(
                                self.iops[index]))
                        self.iops_point_label.setPos(mousePoint.x(), mousePoint.y())  # 设置label的位置
                        # 设置垂直线条和水平线条的位置组成十字光标
                        self.iops_vLine.setPos(mousePoint.x())
            except Exception as e:
                pass

    # NET光标
    def print_net_slot(self, event=None):
        if event is None:
            print("事件为空")
        else:
            pos = event[0]  # 获取事件的鼠标位置
            try:
                # 如果鼠标位置在绘图部件中
                if self.net_widget.sceneBoundingRect().contains(pos):
                    mousePoint = self.net_widget.plotItem.vb.mapSceneToView(pos)  # 转换鼠标坐标
                    index = int(mousePoint.x())  # 鼠标所处的X轴坐标
                    if 0 <= index < len(self.net_read):
                        # 在label中写入HTML
                        self.net_point_label.setHtml(
                            "<p style='color:white'>net-读：{0}Mbps</p><p style='color:white'>net-写：{1}Mbps</p>".format(
                                self.net_read[index], self.net_write[index]))
                        self.net_point_label.setPos(mousePoint.x(), mousePoint.y())  # 设置label的位置
                        # 设置垂直线条和水平线条的位置组成十字光标
                        self.net_vLine.setPos(mousePoint.x())
            except Exception as e:
                pass


# 批量分析
class total_run_form(QDialog, Ui_totalRun_Form):
    # 初始化
    def __init__(self, parent=None):
        super(total_run_form, self).__init__(parent)
        self.setupUi(self)


# 批量运行
class total_analysis_form(QDialog, Ui_totanl_Form):
    # 初始化
    def __init__(self, parent=None):
        super(total_analysis_form, self).__init__(parent)
        self.setupUi(self)
        self.addFile_pushButton.clicked.connect(self.addFile)
        self.remove_pushButton.clicked.connect(self.delFile)
        self.analysis_pushButton.clicked.connect(self.totalanlysis)

    #添加
    def addFile(self):
        filePath, fileType = QFileDialog.getOpenFileName(self, "选取文件", "temp/", "nmon文件 (*.nmon);;所有文件 (*)")
        if filePath == '':
            return
        self.file_listWidget.addItem(filePath)

    # 删除
    def delFile(self):
        try:
            self.file_listWidget.takeItem(self.file_listWidget.currentRow())
        except:
            pass

    #分析
    def totalanlysis(self):
        try:
            for i in range(self.file_listWidget.count()):
                file = self.file_listWidget.item(i).text()
                self.analysisShow = analysis_form()
                self.analysisShow.show()
                self.analysisShow.loadfile(file)
            self.close()
        except:
            pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
