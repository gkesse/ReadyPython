#================================================
from PyQt5.QtWidgets import *
#================================================
from .GWidget import GWidget
#================================================
class GHome(GWidget):
    #================================================
    def __init__(self): 
        super().__init__()
        lApp = GManager.Instance().getData().app
        
        lListBox = GWidget.Create("listbox")
        lListBox.addItem("home/login", "Connexion")
        lListBox.addItem("home/sqlite", "SQLite")
        lListBox.addItem("home/opencv", "OpenCV")
        lListBox.addItem("home/debug", "Debug")
        
        lMainLayout = QVBoxLayout()
        lMainLayout.addWidget(lListBox)
        lMainLayout.setContentsMargins(0, 0, 0, 0)
        lMainLayout.setSpacing(0)
        
        self.setLayout(lMainLayout)
        
        lListBox.emitItemClcik.connect(self.slotItemClick)
    #================================================
    # callback
    #================================================
    def slotItemClick(self):
        lApp = GManager.Instance().getData().app
        GManager.Instance().setPage(lApp.widget_id);
#================================================
from .GManager import GManager
#================================================
