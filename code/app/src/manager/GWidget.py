#================================================
from PyQt5.QtWidgets import *
#================================================
class GWidget(QFrame):
    #================================================
    def __init__(self): 
        pass
    #================================================
    @staticmethod 
    def Create(key):
        # widget
        if key == "widget" : return GWidget()
        if key == "titlebar" : return GTitleBar()
        # default
        return GWidget()
    #================================================
    def run(self):
        print("GWidget")
#================================================
from .GTitleBar import GTitleBar
from .GAddressBar import GAddressBar
from .GAddressKey import GAddressKey
from .GWindow import GWindow
#================================================
