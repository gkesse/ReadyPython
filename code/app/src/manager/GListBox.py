#================================================
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
#================================================
from .GWidget import GWidget
#================================================
class GListBox(GWidget):
    #================================================
    m_scrollLayout = None
    m_widgetId = {}
    m_rowId = {}
    m_index = 0
    #================================================
    def __init__(self): 
        super().__init__()
        lApp = GManager.Instance().getData().app
        self.setObjectName("GListBox")
        
        lScrollLayout = QVBoxLayout()
        self.m_scrollLayout = lScrollLayout
        lScrollLayout.setAlignment(Qt.AlignTop)
        lScrollLayout.setContentsMargins(0, 0, 0, 0)
        lScrollLayout.setSpacing(0)

        lScrollWidget = QFrame()
        lScrollWidget.setLayout(lScrollLayout)

        lScrollArea = QScrollArea()
        lScrollArea.setWidget(lScrollWidget)
        lScrollArea.setWidgetResizable(True)

        self.m_index = 0

        lMainLayout = QVBoxLayout()
        lMainLayout.addWidget(lScrollArea)
        lMainLayout.setAlignment(Qt.AlignTop)
        lMainLayout.setContentsMargins(0, 0, 0, 0)
        lMainLayout.setSpacing(0)

        self.setLayout(lMainLayout)
    #================================================
    # method
    #================================================
    def addItem(self, key, text):
        lButton = QPushButton()
        lButton.setObjectName("item")
        lButton.setText(text)
        lButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.m_scrollLayout.addWidget(lButton)
        self.m_widgetId[lButton] = key
        self.m_rowId[self.m_index] = lButton
        self.m_index += 1
        lButton.clicked.connect(self.slotItemClick)
    #================================================
    # callback
    #================================================
    def slotItemClick(self):
        lApp = GManager.Instance().getData().app
        lWidget = self.sender()
        lApp.widget_id = self.m_widgetId[lWidget]
        self.emitItemClcik.emit()
#================================================
from .GManager import GManager
#================================================
