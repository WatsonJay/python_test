import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5 import QtWidgets

from hello_world.linx_monitor.main.config.config import config
from hello_world.linx_monitor.main.ui.Config_Dialog import Ui_Config_Dialog
from hello_world.linx_monitor.main.ui.MonitorWindow import Ui_Monitor_Window


class MyMainWindow(QMainWindow, Ui_Monitor_Window):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.loadConfig()
        self.serverAdd.clicked.connect(self.serverAdd_Open)
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

    def showWidget(self):
        try:
            conf = config()
            self.serverConfigDialog = serverConfigDialog()
            sention = self.server_listWidget.item(self.server_listWidget.currentRow()).text()
            info = conf.sentionAll(sention)
            self.serverConfigDialog.setDict(info)
            self.serverConfigDialog.disable()
            if self.serverConfigDialog.exec_():
                self.tab = QtWidgets.QWidget()
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

    def disable(self):
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText('连接')
        self.nameEdit.setDisabled(True)
        self.ipEdit.setDisabled(True)
        self.portEdit.setDisabled(True)
        self.userEdit.setDisabled(True)
        self.passwordEdit.setDisabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())