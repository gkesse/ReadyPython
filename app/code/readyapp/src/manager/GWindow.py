#================================================
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#================================================
from .GWidget import GWidget
#================================================
class GWindow(GWidget):
    #================================================
    def __init__(self): 
        super().__init__()
        self.setObjectName("GWindow")
        lApp = GManager.Instance().getData().app
        lApp.win = self
        
        lTitleBar = GWidget.Create("titlebar")
        lAddressBar = GWidget.Create("addressbar")
        
        lAddressKey = GWidget.Create("addresskey")
        lApp.address_key = lAddressKey
        
        lWorkspace = QStackedWidget()
        lWorkspace.setObjectName("workspace")
        lApp.page_map = lWorkspace
        
        self.addPage("home", "Accueil", GWidget.Create("home"), 1)
        self.addPage("home/login", "Connexion", GWidget.Create("login"))
        self.addPage("home/sqlite", "SQLite", GWidget.Create("sqlite"))
        self.addPage("home/opencv", "OpenCV", GWidget.Create("opencv"))
        self.addPage("home/debug", "Debug", GWidget.Create("debug"))
        
        lMainLayout = QVBoxLayout()
        lMainLayout.addWidget(lTitleBar)
        lMainLayout.addWidget(lAddressBar)
        lMainLayout.addWidget(lAddressKey)
        lMainLayout.addWidget(lWorkspace, 1)
        lMainLayout.setContentsMargins(0, 0, 0, 0)
        lMainLayout.setSpacing(10)
        
        self.setLayout(lMainLayout)
        
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(lApp.img_map["logo.png"]))
        self.setWindowTitle(lApp.app_name)
        self.resize(lApp.win_width, lApp.win_height)
    #================================================
    def addPage(self, key, title, widget, isDefault = 0):
        lApp = GManager.Instance().getData().app
        lWidgetId = lApp.page_map.count()
        lApp.page_id[key] = lWidgetId
        lApp.title_map[key] = title
        lApp.page_map.addWidget(widget)
        if isDefault == 1: GManager.Instance().setPage(key)
#================================================
from .GManager import GManager
#================================================
