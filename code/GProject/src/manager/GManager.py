#================================================
import os
#================================================
class GManager:
    #================================================
    # property
    #================================================
    m_instance = None
    mgr = None
    #================================================
    # constructor
    #================================================
    def __init__(self):
        # manager
        self.mgr = sGManager()
        # app
        self.mgr.app = sGApp()
        self.mgr.app.app_name = "ReadyApp"
        self.mgr.app.sqlite_db_path = self.getEnv("GSQLITE_DB_PATH")
        self.mgr.app.audio_path = self.getEnv("GAUDIO_PATH")
        self.mgr.app.video_path = self.getEnv("GVIDEO_PATH")
        self.mgr.app.separator = self.getEnv("GSEPARATOR")
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
# struct
#================================================
class sGManager:
    app = None
#================================================
class sGApp:
    # app
    app_name = None
    # sqlite
    sqlite_db_path = None
    # audio
    audio_path = None
    # video
    video_path = None
    # separator
    separator = None
#================================================
