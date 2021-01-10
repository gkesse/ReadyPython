#================================================
from PyQt5.QtWidgets import *
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
        lLogo.setIcon(lApp.qta.icon("fa.times", color=lApp.qta_color))
        self.m_widgetId[lLogo] = "logo"
        
        lAppName = QPushButton()
        lAppName.setObjectName("app_name")
        lAppName.setText(lApp.app_name)
        self.m_widgetId[lAppName] = "app_name"
        
        lTitle = QLabel()
        lApp.title = lTitle
        lTitle.setObjectName("title")
        lTitle.setText(lApp.app_name)
        self.m_widgetId[lTitle] = "title"
        
        lLogin = QPushButton()
        lLogin.setObjectName("login")
        lLogin.setIcon(lApp.qta.icon("fa.times", color=lApp.qta_color))
        self.m_widgetId[lLogin] = "login"

        lFullscreen = QPushButton()
        lFullscreen.setObjectName("fullscreen")
        lFullscreen.setIcon(lApp.qta.icon("fa.times", color=lApp.qta_color))
        self.m_widgetId[lFullscreen] = "fullscreen"

        lMinimize = QPushButton()
        lMinimize.setObjectName("minimize")
        lMinimize.setIcon(lApp.qta.icon("fa.times", color=lApp.qta_color))
        self.m_widgetId[lMinimize] = "minimize"

        lMaximize = QPushButton()
        lMaximize.setObjectName("maximize")
        lMaximize.setIcon(lApp.qta.icon("fa.times", color=lApp.qta_color))
        self.m_widgetId[lMaximize] = "maximize"

        lClose = QPushButton()
        lClose.setObjectName("close")
        lClose.setIcon(lApp.qta.icon("fa.times", color=lApp.qta_color))
        self.m_widgetId[lClose] = "close"
        
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
