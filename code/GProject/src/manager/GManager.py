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
# struct
#================================================
class sGManager:
    app = None
#================================================
class sGApp:
    # app
    app_name = None
#================================================
