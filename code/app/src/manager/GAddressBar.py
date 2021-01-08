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
        
        lLabel = QLabel()
        lLabel.setText("GAddressBar")
        
        lMainLayout = QVBoxLayout()
        lMainLayout.addWidget(lLabel)
        lMainLayout.setContentsMargins(0, 0, 0, 0)
        lMainLayout.setSpacing(0)
        
        self.setLayout(lMainLayout)        
#================================================
from .GManager import GManager
#================================================
