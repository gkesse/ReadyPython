#================================================
from PyQt5.QtWidgets import *
#================================================
from .GWidget import GWidget
#================================================
class GTitleBar(GWidget):
    #================================================
    def __init__(self):
        super().__init__()
        lApp = GManager.Instance().getData().app
        
        lLogo = QPushButton()
        lLogo.setObjectName("logo")
        lLogo.setText("logo")
        
        lAppName = QPushButton()
        lAppName.setObjectName("app_name")
        lAppName.setText(lApp.app_name)
        
        lTitle = QLabel()
        lTitle.setObjectName("title")
        lTitle.setText(lApp.title)
        
        lLogin = QPushButton()
        lLogin.setObjectName("login")
        lLogin.setText("login")

        lFullscreen = QPushButton()
        lFullscreen.setObjectName("fullscreen")
        lFullscreen.setText("fullscreen")

        lMinimize = QPushButton()
        lMinimize.setObjectName("minimize")
        lMinimize.setText("minimize")

        lMaximize = QPushButton()
        lMaximize.setObjectName("maximize")
        lMaximize.setText("maximize")

        lClose = QPushButton()
        lClose.setObjectName("close")
        lClose.setText("close")
        
        lMainLayout = QHBoxLayout()
        lMainLayout.addWidget(lLogo)
        lMainLayout.addWidget(lAppName)
        lMainLayout.addWidget(lTitle, 1)
        lMainLayout.addWidget(lLogin)
        lMainLayout.addWidget(lFullscreen)
        lMainLayout.addWidget(lMinimize)
        lMainLayout.addWidget(lMaximize)
        lMainLayout.addWidget(lClose)
        lMainLayout.setContentsMargins(0, 0, 0, 0)
        lMainLayout.setSpacing(0)
        
        self.setLayout(lMainLayout)
#================================================
from .GManager import GManager
#================================================
