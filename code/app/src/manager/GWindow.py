#================================================
from PyQt5.QtWidgets import *
#================================================
from .GWidget import GWidget
#================================================
class GWindow(GWidget):
    #================================================
    def __init__(self): 
        super().__init__()
        lApp = GManager.Instance().getData().app
        
        lTitleBar = GWidget.Create("titlebar")
        lAddressBar = GWidget.Create("addressbar")
        lAddressKey = GWidget.Create("addresskey")
        lWorkspace = QStackedWidget()
        
        lMainLayout = QVBoxLayout()
        lMainLayout.addWidget(lTitleBar)
        lMainLayout.addWidget(lAddressBar)
        lMainLayout.addWidget(lAddressKey)
        lMainLayout.addWidget(lWorkspace, 1)
        lMainLayout.setContentsMargins(0, 0, 0, 0)
        lMainLayout.setSpacing(0)
        
        self.setLayout(lMainLayout)        
#================================================
from .GManager import GManager
#================================================
