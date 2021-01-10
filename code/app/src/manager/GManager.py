#================================================
import os
import qtawesome
#================================================
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#================================================
class GManager:
    #================================================
    m_instance = None
    mgr = None
    #================================================
    def __init__(self):
        # manager
        self.mgr = sGManager()
        # app
        self.mgr.app = sGApp()
        self.mgr.app.app_name = "ReadyApp"
        self.mgr.app.title_map = {}
        self.mgr.app.sqlite_db_path = self.getEnv("GSQLITE_DB_PATH")
        self.mgr.app.audio_path = self.getEnv("GAUDIO_PATH")
        self.mgr.app.video_path = self.getEnv("GVIDEO_PATH")
        self.mgr.app.separator = self.getEnv("GSEPARATOR")
        self.mgr.app.page_id = {}
        self.mgr.app.address_url = "home"
        self.mgr.app.address_new = self.mgr.app.address_url
        self.mgr.app.qta = qtawesome
        self.mgr.app.qta_color = "#ffffff"
        self.mgr.app.qta_size = 16
        self.mgr.app.style_path = self.getEnv("GSTYLE_PATH")
        self.mgr.app.font_path = self.getEnv("GFONT_PATH")
        self.mgr.app.img_path = self.getEnv("GIMG_PATH")
        self.mgr.app.img_map = {}
    #================================================
    @staticmethod 
    def Instance():
        if GManager.m_instance == None:
            GManager.m_instance = GManager()
        return GManager.m_instance
    #================================================
    # data
    #================================================
    def getData(self):
        return self.mgr
    #================================================
    # env
    #================================================
    def getEnv(self, key):
        return os.getenv(key)
    #================================================
    # string
    #================================================
    def getWidth(self, widthMap, index, defaultWidth):
        lWidthMap = widthMap.split(";")
        lLength = len(lWidthMap)
        if index >= lLength : return defaultWidth
        lWidthId = lWidthMap[index]
        if not lWidthId.isdigit() : return defaultWidth
        lWidth = int(lWidthId)
        return lWidth
    #================================================
    # path
    #================================================
    def validPath(self, path):
        lReplace = "\/:*?\"<>|"
        for lChar in lReplace :
            path = path.replace(lChar, "")
        return path
    #================================================
    # page
    #================================================
    def setPage(self, address):
        lPageId = self.mgr.app.page_id.get(address, -1)
        if lPageId == -1: self.mgr.app.address.setText(self.mgr.app.address_url); return
        lPage = self.mgr.app.page_map.widget(lPageId)
        self.mgr.app.address_new = address;
        if lPage.loadPage() == 0: self.mgr.app.address.setText(self.mgr.app.address_url); return
        self.mgr.app.page_map.setCurrentIndex(lPageId);
        self.mgr.app.address.setText(address);
        self.mgr.app.address_url = address;
        self.mgr.app.address_key.setContent(address);
        self.mgr.app.title.setText(self.mgr.app.title_map[address]);
    #================================================
    # layout
    #================================================
    def clearLayout(self, layout):
        if layout != 0:
            while layout.count() > 0:
                lItem = layout.takeAt(0)
                lWidget = lItem.widget()
                if lWidget != 0: 
                    layout.removeWidget(lWidget)
                    lWidget.setParent(None)
    #================================================
    # style
    #================================================
    def loadStyle(self):
        lStyleSheet = open(self.mgr.app.style_path).read()
        self.mgr.app.qapp.setStyleSheet(lStyleSheet)
    #================================================
    # font
    #================================================
    def loadFont(self):
        for lPath, lSubDirs, lFiles in os.walk(self.mgr.app.font_path):
            for lName in lFiles:
                lFile = os.path.join(lPath, lName)
                QFontDatabase.addApplicationFont(lFile)
    #================================================
    # img
    #================================================
    def loadImg(self):
        for lPath, lSubDirs, lFiles in os.walk(self.mgr.app.img_path):
            for lName in lFiles:
                lFile = os.path.join(lPath, lName)
                lKey = QFileInfo(lFile).fileName()
                self.mgr.app.img_map[lKey] = lFile
#================================================
# struct
#================================================
class sGManager:
    app = None
#================================================
class sGApp:
    # app
    qapp = None
    app_name = None
    # title
    title = None
    title_map = None
    # sqlite
    sqlite_db_path = None
    # audio
    audio_path = None
    # video
    video_path = None
    # separator
    separator = None
    # page
    page_map = None
    page_id = None
    # address
    address = None
    address_key = None
    address_url = None
    address_new = None
    # qta
    qta = None
    qta_color = None
    qta_size = None
    # widget
    widget_id = None
    # debug
    debug = None
    # style
    style_path = None
    # font
    font_path = None
    # img
    img_path = None
    img_map = None
#================================================
