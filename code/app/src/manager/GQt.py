#================================================
import sys
from PyQt5.QtWidgets import *
#================================================
class GQt:
    #================================================
    m_instance = None
    #================================================
    def __init__(self): 
        pass
    #================================================
    @staticmethod 
    def Instance():
        if GQt.m_instance == None:
            GQt.m_instance = GQt()
        return GQt.m_instance
    #================================================
    def run(self):
        app = QApplication(sys.argv)
        lWindow = GWidget.Create("window")
        lWindow.show()
        app.exec_()
#================================================
from .GWidget import GWidget
from .GManager import GManager
#================================================
