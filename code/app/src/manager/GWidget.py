#================================================
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#================================================
class GWidget(QFrame):
    #================================================
    emitItemClcik = pyqtSignal()
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
        if key == "debug" : return GDebug()
        # default
        return GWidget()
    #================================================
    # method
    #================================================
    def addItem(self, key, text): pass
    def addPage(self, key, title, widget, isDefault = 0): pass
    def loadPage(self): pass
    def setContent(self, text): pass
    #================================================
    # callback
    #================================================
    def slotItemClick(self): pass
#================================================
# widget
from .GTitleBar import GTitleBar
from .GAddressBar import GAddressBar
from .GAddressKey import GAddressKey
from .GListBox import GListBox
# page
from .GWindow import GWindow
from .GHome import GHome
from .GDebug import GDebug
#================================================
