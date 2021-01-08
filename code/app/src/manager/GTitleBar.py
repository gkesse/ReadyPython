#================================================
from PyQt5.QtWidgets import *
#================================================
from .GWidget import GWidget
#================================================
class GTitleBar(GWidget):
    #================================================
    def __init__(self):
        lLogo = QPushButton()
        lLogo.setText("logo")
        
        lMainLayout = QHBoxLayout()
        lMainLayout.addWidget(lLogo)
        
        self.setLayout(lMainLayout)
    #================================================
    def run(self):
        print("GTitleBar")
#================================================
