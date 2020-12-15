#================================================
class GManager:
    #================================================
    # property
    #================================================
    m_instance = None
    m_dataMap = {}
    #================================================
    # constructor
    #================================================
    def __init__(self):
        # sqlite
        self.m_dataMap["sqlite.file"] = "/home/osboxes/Programs/ReadyBin/unix/.CONFIG_O.dat"
    #================================================
    @staticmethod 
    def Instance():
        if GManager.m_instance == None:
            GManager.m_instance = GManager()
        return GManager.m_instance
    #================================================
    # data
    #================================================
    def setData(self, key, value):
        self.m_dataMap[key] = value
    #================================================
    def getData(self, key):
        return self.m_dataMap.get(key, "")
    #================================================
    # env
    #================================================
    def getEnv(self, key):
        return os.getenv(key)
#================================================
# struct
#================================================
class sGManager:
    app = None
#================================================
class sGApp:
    # app
    app_name = None
#================================================
