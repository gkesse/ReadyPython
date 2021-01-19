#================================================
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#================================================
from .GWidget import GWidget
#================================================
class GOpenCVQt(GWidget):
    #================================================
    def __init__(self): 
        super().__init__()
        self.setObjectName("GOpenCVQt");
        lApp = GManager.Instance().getData().app
        
        lLabel = QLabel()
        lLabel.setText("GOpenCVQt")
        lLabel.setAlignment(Qt.AlignCenter)

        lMainLayout = QVBoxLayout()
        lMainLayout.addWidget(lLabel)
        lMainLayout.setContentsMargins(0, 0, 0, 0)
        lMainLayout.setSpacing(0)
        
        self.setLayout(lMainLayout)        
#================================================
from .GManager import GManager
#================================================
