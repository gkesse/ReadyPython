#================================================
from PyQt5.QtWidgets import *
#================================================
from .GWidget import GWidget
#================================================
class GAddressBar(GWidget):
    #================================================
    def __init__(self): 
        super().__init__()
        lApp = GManager.Instance().getData().app
        
        lIcon = QPushButton()
        lIcon.setObjectName("icon")
        lIcon.setText("icon")
        
        lAddress = QLineEdit()
        lApp.address = lAddress
        lAddress.setObjectName("edit")
        
        lGoTo = QPushButton()
        lGoTo.setObjectName("goto")
        lGoTo.setText("goto")
        
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
