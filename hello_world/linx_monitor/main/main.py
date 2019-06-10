import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QWidget
from PyQt5 import QtWidgets

from hello_world.linx_monitor.main.config.config import config
from hello_world.linx_monitor.main.ui.Config_Dialog import Ui_Config_Dialog
from hello_world.linx_monitor.main.ui.MonitorWindow import Ui_Monitor_Window
from hello_world.linx_monitor.main.ui.simple import Ui_simple_Form


class MyMainWindow(QMainWindow, Ui_Monitor_Window):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.loadConfig()
        self.serverAdd.clicked.connect(self.serverAdd_Open)
        self.serverModif.clicked.connect(self.serverModif_Open)
        self.serverDelete.clicked.connect(self.serverDel)
        self.server_listWidget.itemDoubleClicked.connect(self.showWidget)
        self.tabWidget.tabCloseRequested.connect(self.tabWidget.removeTab)

    def loadConfig(self):
        try:
            conf = config()
            SentionList = conf.getSection()
            self.server_listWidget.clear()
            self.server_listWidget.addItems(SentionList)
        except Exception as e:
            self.Tips("配置文件出现异常，请重置配置文件")

    def serverAdd_Open(self):
        conf = config()
        self.serverConfigDialog = serverConfigDialog()
        if self.serverConfigDialog.exec_():
            infos = self.serverConfigDialog.getDict()
            conf.cmdSection(infos['name'],infos)
        self.serverConfigDialog.destroy()
        self.loadConfig()

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
                self.tabWidget.addTab(self.tab, sention)
                self.tabWidget.setCurrentWidget(self.tab)
            self.serverConfigDialog.destroy()
        except Exception as e:
            self.Tips("配置文件出现异常，请重置配置文件")

    def Tips(self, message):
        QMessageBox.about(self, "提示", message)

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
        info['password'] = conf.encrypt(self.nameEdit.text())
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

class simpleForm(QWidget,Ui_simple_Form):
    def __init__(self):
        super(simpleForm,self).__init__()
        self.setupUi(self)

    def setIp(self, ip):
        self.ip_lineEdit.setText(ip)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())