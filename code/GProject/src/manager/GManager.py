#================================================
class GManager:
    #================================================
    m_instance = None
    m_dataMap = {}
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
    def setData(self, key, value):
        self.m_dataMap[key] = value
    #================================================
    def getData(self, key):
        return self.m_dataMap.get(key, "")
#================================================
