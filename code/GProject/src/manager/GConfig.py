#================================================
class GConfig:
    #================================================
    m_instance = None
    m_dataMap = {}
    #================================================
    def __init__(self):
        pass
    #================================================
    @staticmethod 
    def Instance():
        if GConfig.m_instance == None:
            GConfig.m_instance = GConfig()
        return GConfig.m_instance
    #================================================
    def setData(self, key, value):
        self.m_dataMap[key] = value
    #================================================
    def getData(self, key):
        return self.m_dataMap.get(key, "")
    #================================================
    def saveData(self, key):
        lValue = self.m_dataMap[key]
    #================================================
    def checkData(self, key):
        lValue = self.m_dataMap[key]
#================================================
