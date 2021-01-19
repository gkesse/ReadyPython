#================================================
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#================================================
from .GWidget import GWidget
#================================================
class GAddressKey(GWidget):
    #================================================
    m_mainLayout = None
    m_widgetId = {}
    #================================================
    def __init__(self): 
        super().__init__()
        lApp = GManager.Instance().getData().app
                
        lMainLayout = QHBoxLayout()
        self.m_mainLayout = lMainLayout
        lMainLayout.setAlignment(Qt.AlignLeft)
        lMainLayout.setContentsMargins(0, 0, 0, 0)
        lMainLayout.setSpacing(0)
        
        self.setLayout(lMainLayout)        
    #================================================
    # method
    #================================================
    def setContent(self, text):
        lApp = GManager.Instance().getData().app

        lMap = text.split("/")
        lKey = ""
        
        GManager.Instance().clearLayout(self.m_mainLayout)

        for i in range(len(lMap)):
            if i != 0:
                lSep = QPushButton()
                lSep.setObjectName("sep")
                lSep.setIcon(lApp.qta.icon("fa.chevron-right", color=lApp.qta_color))
                self.m_mainLayout.addWidget(lSep)
            
            if i != 0: lKey += "/"
            lKey += lMap[i]
            
            lButton = QPushButton()
            lButton.setObjectName("item")
            lButton.setText(lMap[i])
            lButton.setCursor(QCursor(Qt.PointingHandCursor))
            self.m_widgetId[lButton] = lKey
            self.m_mainLayout.addWidget(lButton)
            lButton.clicked.connect(self.slotItemClick)
    #================================================
    # callback
    #================================================
    def slotItemClick(self):
        lWidget = self.sender()
        lWidgetId = self.m_widgetId[lWidget]
        GManager.Instance().setPage(lWidgetId);
#================================================
from .GManager import GManager
#================================================
