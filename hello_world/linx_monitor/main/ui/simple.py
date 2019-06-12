# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui_simple_Form(object):
    def setupUi(self, simple_Form):
        simple_Form.setObjectName("simple_Form")
        simple_Form.resize(616, 497)
        self.verticalLayout = QtWidgets.QVBoxLayout(simple_Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(simple_Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ip_lineEdit = QtWidgets.QLineEdit(simple_Form)
        self.ip_lineEdit.setReadOnly(True)
        self.ip_lineEdit.setObjectName("ip_lineEdit")
        self.horizontalLayout.addWidget(self.ip_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nmon_label = QtWidgets.QLabel(simple_Form)
        self.nmon_label.setObjectName("nmon_label")
        self.horizontalLayout_2.addWidget(self.nmon_label)
        self.upload_nmon = QtWidgets.QPushButton(simple_Form)
        self.upload_nmon.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.upload_nmon.setFont(font)
        self.upload_nmon.setObjectName("upload_nmon")
        self.horizontalLayout_2.addWidget(self.upload_nmon)
        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(1, 2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.start_record = QtWidgets.QPushButton(simple_Form)
        self.start_record.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.start_record.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_record.setIcon(icon)
        self.start_record.setObjectName("start_record")
        self.gridLayout.addWidget(self.start_record, 0, 1, 1, 1)
        self.stop_record = QtWidgets.QPushButton(simple_Form)
        self.stop_record.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.stop_record.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icon/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_record.setIcon(icon1)
        self.stop_record.setObjectName("stop_record")
        self.gridLayout.addWidget(self.stop_record, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(simple_Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.record_name = QtWidgets.QLabel(simple_Form)
        self.record_name.setObjectName("record_name")
        self.horizontalLayout_3.addWidget(self.record_name)
        self.download_record = QtWidgets.QPushButton(simple_Form)
        self.download_record.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.download_record.setFont(font)
        self.download_record.setObjectName("download_record")
        self.horizontalLayout_3.addWidget(self.download_record)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 7)
        self.horizontalLayout_3.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.clean_info = QtWidgets.QPushButton(simple_Form)
        self.clean_info.setMaximumSize(QtCore.QSize(60, 20))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icon/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clean_info.setIcon(icon2)
        self.clean_info.setObjectName("clean_info")
        self.gridLayout.addWidget(self.clean_info, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupBox = QtWidgets.QGroupBox(simple_Form)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.info_borwser = QtWidgets.QTextBrowser(self.groupBox)
        self.info_borwser.setObjectName("info_borwser")
        self.horizontalLayout_4.addWidget(self.info_borwser)
        self.verticalLayout.addWidget(self.groupBox)
        self.graph_widget = pg.PlotWidget(simple_Form)
        self.graph_widget.setMinimumSize(QtCore.QSize(300, 200))
        self.graph_widget.setObjectName("graph_widget")
        self.graph_widget.showGrid(x=True, y=True, alpha=0.5)  # 显示图形网格
        self.graph_widget.setLabel(axis='left', text='百分比(%)')  # 设置Y轴标签
        self.graph_widget.setYRange(0, 150)
        self.graph_widget.setXRange(0, 20, padding=0)
        self.graph_widget.setLabel(axis='bottom', text='采样点(个)')  # 设置X轴标签
        self.graph_widget.addLegend(size=(20, 10), offset=(12, 12))
        self.verticalLayout.addWidget(self.graph_widget)
        self.point_label = pg.TextItem()  # 创建一个文本项
        self.graph_widget.addItem(self.point_label)  # 在图形部件中添加文本项
        self.cpu_line = self.graph_widget.plot(pen="r", name="cpu", symbolBrush=(255,0,0))
        self.memory_line = self.graph_widget.plot(pen="g", name="内存", symbolBrush=(0,255,0))
        self.disk_line = self.graph_widget.plot(pen="y", name="磁盘", symbolBrush=(255,255,0))
        self.vLine = pg.InfiniteLine(angle=90, movable=False)  # 创建一个垂直线条
        self.graph_widget.addItem(self.vLine, ignoreBounds=True)  # 在图形部件中添加垂直线条
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 7)

        self.retranslateUi(simple_Form)
        QtCore.QMetaObject.connectSlotsByName(simple_Form)

    def retranslateUi(self, simple_Form):
        _translate = QtCore.QCoreApplication.translate
        simple_Form.setWindowTitle(_translate("simple_Form", "Form"))
        self.label.setText(_translate("simple_Form", "当前服务器："))
        self.nmon_label.setText(_translate("simple_Form", "当前服务器未安装nmon"))
        self.upload_nmon.setText(_translate("simple_Form", "上传"))
        self.start_record.setText(_translate("simple_Form", "开始"))
        self.stop_record.setText(_translate("simple_Form", "终止"))
        self.label_3.setText(_translate("simple_Form", "当前性能记录："))
        self.record_name.setText(_translate("simple_Form", "TextLabel"))
        self.download_record.setText(_translate("simple_Form", "下载"))
        self.clean_info.setText(_translate("simple_Form", "清除"))
        self.groupBox.setTitle(_translate("simple_Form", "消息日志"))

