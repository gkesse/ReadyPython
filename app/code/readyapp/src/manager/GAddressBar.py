#================================================
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#================================================
from .GWidget import GWidget
#================================================
class GAddressBar(GWidget):
    #================================================
    m_widgetId = {}
    #================================================
    def __init__(self): 
        super().__init__()
        self.setObjectName("GAddressBar");
        lApp = GManager.Instance().getData().app
        
        lIcon = QPushButton()
        lIcon.setObjectName("icon")
        lIcon.setIcon(lApp.qta.icon("fa5s.home", color=lApp.qta_color))
        lIcon.setIconSize(QSize(lApp.qta_size, lApp.qta_size))
        lIcon.setCursor(QCursor(Qt.PointingHandCursor))
        self.m_widgetId[lIcon] = "icon"
        
        lAddress = QLineEdit()
        lApp.address = lAddress
        lAddress.setObjectName("edit")
        
        lGoTo = QPushButton()
        lGoTo.setObjectName("goto")
        lGoTo.setIcon(lApp.qta.icon("fa5s.paper-plane", color=lApp.qta_color))
        lGoTo.setIconSize(QSize(lApp.qta_size, lApp.qta_size))
        lGoTo.setCursor(QCursor(Qt.PointingHandCursor))
        self.m_widgetId[lGoTo] = "goto"
        
        lMainLayout = QHBoxLayout()
        lMainLayout.addWidget(lIcon)
        lMainLayout.addWidget(lAddress)
        lMainLayout.addWidget(lGoTo)
        lMainLayout.setContentsMargins(0, 0, 0, 0)
        lMainLayout.setSpacing(0)
        
        self.setLayout(lMainLayout)        
#================================================
from .GManager import GManager
#================================================
