#================================================
from PyQt5.QtWidgets import *
#================================================
from .GWidget import GWidget
#================================================
class GDebug(GWidget):
    #================================================
    def __init__(self): 
        super().__init__()
        lApp = GManager.Instance().getData().app
        
        lTextEdit = QTextEdit()
        lApp.debug = lTextEdit
        lTextEdit.setReadOnly(True)
        lTextEdit.append("hello")
        
        lMainLayout = QVBoxLayout()
        lMainLayout.addWidget(lTextEdit)
        lMainLayout.setContentsMargins(0, 0, 0, 0)
        lMainLayout.setSpacing(0)
        
        self.setLayout(lMainLayout)        
#================================================
from .GManager import GManager
#================================================
