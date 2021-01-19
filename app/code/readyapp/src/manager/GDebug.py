#================================================
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#================================================
from .GWidget import GWidget
#================================================
class GDebug(GWidget):
    #================================================
    def __init__(self): 
        super().__init__()
        self.setObjectName("GDebug");
        lApp = GManager.Instance().getData().app
        
        lTextEdit = QTextEdit()
        lApp.debug = lTextEdit
        lTextEdit.setObjectName("text");
        lTextEdit.setReadOnly(True)
        lTextEdit.append("Bonjour tout le monde")
        
        lMainLayout = QVBoxLayout()
        lMainLayout.addWidget(lTextEdit)
        lMainLayout.setContentsMargins(0, 0, 0, 0)
        lMainLayout.setSpacing(0)
        
        self.setLayout(lMainLayout)        
#================================================
from .GManager import GManager
#================================================
