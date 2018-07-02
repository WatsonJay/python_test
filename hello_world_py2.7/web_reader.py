import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

class Browser(QWidget):

    def __init__(self):
        super(Browser,self).__init__()

        self.webview = QWebView(self)
        self.webview.load("http://www.nothingistrue.top")
        self.setGeometry(0,0,800,600)
        #back and forward
        self.back_btn = QPushButton("<",self)
        self.back_btn.clicked.connect(self.webview.back)
        self.back_btn.setMaximumSize(20,20)
        self.forward_btn = QPushButton(">", self)
        self.forward_btn.clicked.connect(self.webview.forward)
        self.forward_btn.setMaximumSize(20, 20)
        #url
        self.url_entry = QLineEdit(self)
        self.url_entry.setMinimumSize(200,20)
        self.url_entry.setMaximumSize(300,20)

        #go
        self.go_btn = QPushButton("GO",self)
        self.go_btn.clicked.connect(self.go_btn_clicked)
        self.go_btn.setMaximumSize(20,20)

        #favourite
        self.favourites = QComboBox(self)
        self.favourites.addItems(["http://www.google.com",
                                  "http://www.raspberrypi.org",
                                  "http://docs.python.org/3/",
                                  "http://www.nothingistrue.top"])
        self.favourites.activated.connect(self.favourite_selected)
        self.favourites.setMinimumSize(200,20)
        self.favourites.setMaximumSize(300,20)

        #search
        self.search_box = QLineEdit(self)
        self.search_box.setMinimumSize(200,20)
        self.search_box.setMaximumSize(300,20)

        self.search_btn = QPushButton("Search",self)
        self.search_btn.clicked.connect(self.search_btn_clicked)
        self.search_btn.setMaximumSize(50,20)

        #zoom
        self.zoom_slider = QSlider(Qt.Orientation(1),self)
        self.zoom_slider.setRange(2,50)
        self.zoom_slider.setValue(10)
        self.zoom_slider.valueChanged.connect(self.zoom_changed)

        self.zoom_label = QLabel("Zoom:")

        self.webview.loadFinished.connect(self.page_loading)

        self.menu_bar = QHBoxLayout()
        self.menu_bar.addWidget(self.back_btn)
        self.menu_bar.addWidget(self.forward_btn)
        self.menu_bar.addWidget(self.url_entry)
        self.menu_bar.addWidget(self.go_btn)
        self.menu_bar.addStretch()
        self.menu_bar.addWidget(self.favourites)
        self.menu_bar.addStretch()
        self.menu_bar.addWidget(self.search_box)
        self.menu_bar.addWidget(self.search_btn)
        self.menu_bar.addWidget(self.zoom_label)
        self.menu_bar.addWidget(self.zoom_slider)
        self.main_layout =QVBoxLayout()
        self.main_layout.addLayout(self.menu_bar)
        self.main_layout.addWidget(self.webview)
        self.setLayout(self.main_layout)

    def go_btn_clicked(self):
        self.webview.load(self.url_entry.text())

    def favourite_selected(self):
        self.webview.load(self.favourites.currentText())

    def zoom_changed(self):
        self.webview.setZoomFactor(self.zoom_slider.value()/10)

    def search_btn_clicked(self):
        self.webview.load("https://www.baidu.com/baidu?wd="+
                          self.search_box.text()+"&tn=monline_4_dg&ie=utf-8")

    def page_loading(self):
        self.url_entry.setText(self.webview.url().toString())

class BrowserWindow(QMainWindow):
    def __init__(self):
        super(BrowserWindow,self).__init__()
        self.widget = Browser()
        self.setCentralWidget(self.widget)

        self.exitAction = QAction(QIcon('exit.png'),'&Exit',self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(self.close)

        self.openFile  = QAction(QIcon('open.png'),'Open',self)
        self.openFile.setShortcut('Ctrl+O')
        self.openFile.setStatusTip('Open new File')
        self.openFile.triggered.connect(self.showDialog)

        self.menu= self.menuBar()
        self.fileMenu = self.menu.addMenu('&File')
        self.fileMenu.addAction(self.openFile)
        self.fileMenu.addAction(self.exitAction)

    def showDialog(self):
        fname,_ = QFileDialog.getOpenFileName(self,'Open file','/home')
        self.widget.webview.load("file:///"+fname)
# Create a Qt application
app = QApplication(sys.argv)
window = BrowserWindow()
window.show()

# Enter Qt application main loop
app.exec_()
sys.exit()