#================================================
from PyQt5.QtWidgets import *
#================================================
class GWidget(QFrame):
    #================================================
    def __init__(self): 
        super().__init__()
    #================================================
    @staticmethod 
    def Create(key):
        # widget
        if key == "widget" : return GWidget()
        if key == "titlebar" : return GTitleBar()
        if key == "addressbar" : return GAddressBar()
        if key == "addresskey" : return GAddressKey()
        if key == "listbox" : return GListBox()
        # page
        if key == "window" : return GWindow()
        if key == "home" : return GHome()
        # default
        return GWidget()
    #================================================
    def run(self):
        print("GWidget")
#================================================
# widget
from .GTitleBar import GTitleBar
from .GAddressBar import GAddressBar
from .GAddressKey import GAddressKey
from .GListBox import GListBox
# page
from .GWindow import GWindow
from .GHome import GHome
#================================================
