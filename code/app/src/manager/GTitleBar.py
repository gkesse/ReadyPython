#================================================
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#================================================
from .GWidget import GWidget
#================================================
class GTitleBar(GWidget):
    #================================================
    m_widgetId = {}
    #================================================
    def __init__(self):
        super().__init__()
        self.setObjectName("GTitleBar")
        lApp = GManager.Instance().getData().app
        
        lLogo = QPushButton()
        lLogo.setObjectName("logo")
        lLogo.setIcon(QIcon(lApp.img_map["logo.png"]))
        lLogo.setIconSize(QSize(lApp.qta_size, lApp.qta_size))
        lLogo.setCursor(QCursor(Qt.PointingHandCursor))
        self.m_widgetId[lLogo] = "logo"
        
        lAppName = QPushButton()
        lAppName.setObjectName("app_name")
        lAppName.setText(lApp.app_name)
        lAppName.setCursor(QCursor(Qt.PointingHandCursor))
        self.m_widgetId[lAppName] = "app_name"
        
        lTitle = QLabel()
        lApp.title = lTitle
        lTitle.setObjectName("title")
        lTitle.setText(lApp.app_name)
        lTitle.setAlignment(Qt.AlignCenter)
        self.m_widgetId[lTitle] = "title"
        
        lLogin = QPushButton()
        lLogin.setObjectName("login")
        lLogin.setIcon(lApp.qta.icon("fa5s.user", color=lApp.qta_color))
        lLogin.setIconSize(QSize(lApp.qta_size, lApp.qta_size))
        lLogin.setText("Se Connecter")
        lLogin.setCursor(QCursor(Qt.PointingHandCursor))
        self.m_widgetId[lLogin] = "login"

        lFullscreen = QPushButton()
        lFullscreen.setObjectName("fullscreen")
        lFullscreen.setIcon(lApp.qta.icon("fa5s.expand", color=lApp.qta_color))
        lFullscreen.setIconSize(QSize(lApp.qta_size, lApp.qta_size))
        lFullscreen.setCursor(QCursor(Qt.PointingHandCursor))
        self.m_widgetId[lFullscreen] = "fullscreen"

        lMinimize = QPushButton()
        lMinimize.setObjectName("minimize")
        lMinimize.setIcon(lApp.qta.icon("fa5s.window-minimize", color=lApp.qta_color))
        lMinimize.setIconSize(QSize(lApp.qta_size, lApp.qta_size))
        lMinimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.m_widgetId[lMinimize] = "minimize"

        lMaximize = QPushButton()
        lMaximize.setObjectName("maximize")
        lMaximize.setIcon(lApp.qta.icon("fa5s.window-maximize", color=lApp.qta_color))
        lMaximize.setIconSize(QSize(lApp.qta_size, lApp.qta_size))
        lMaximize.setCursor(QCursor(Qt.PointingHandCursor))
        self.m_widgetId[lMaximize] = "maximize"

        lClose = QPushButton()
        lClose.setObjectName("close")
        lClose.setIcon(lApp.qta.icon("fa5s.times", color=lApp.qta_color))
        lClose.setIconSize(QSize(lApp.qta_size, lApp.qta_size))
        lClose.setCursor(QCursor(Qt.PointingHandCursor))
        self.m_widgetId[lClose] = "close"
        
        lLogoLayout = QHBoxLayout()
        lLogoLayout.addWidget(lLogo)
        lLogoLayout.addWidget(lAppName)
        lLogoLayout.setContentsMargins(0, 0, 0, 0)
        lLogoLayout.setSpacing(0)
        
        lMainLayout = QHBoxLayout()
        lMainLayout.addLayout(lLogoLayout)
        lMainLayout.addWidget(lTitle, 1)
        lMainLayout.addWidget(lLogin)
        lMainLayout.addWidget(lFullscreen)
        lMainLayout.addWidget(lMinimize)
        lMainLayout.addWidget(lMaximize)
        lMainLayout.addWidget(lClose)
        lMainLayout.setContentsMargins(0, 0, 0, 0)
        lMainLayout.setSpacing(5)
        
        self.setLayout(lMainLayout)
#================================================
from .GManager import GManager
#================================================
