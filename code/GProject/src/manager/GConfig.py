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
        lCheck = self.checkData(key)
        if lCheck == 0 : self.insertData(key)
        else : self.updateData(key)
    #================================================
    def loadData(self, key):
        lValue = GSQLite.Instance().queryValue("""
        select CONFIG_VALUE from CONFIG_PYTHON 
        where CONFIG_KEY='{0}'
        """.format(key))
        self.setData(key, lValue)
    #================================================
    def checkData(self, key):
        lCount = GSQLite.Instance().queryValue("""
        select count(*) from CONFIG_PYTHON 
        where CONFIG_KEY='{0}'
        """.format(key))
        return lCount
    #================================================
    def insertData(self, key):
        lValue = self.getData(key)
        GSQLite.Instance().queryWrite("""
        insert into CONFIG_PYTHON (CONFIG_KEY, CONFIG_VALUE)
        values ('{0}', '{1}')
        """.format(key, lValue))
    #================================================
    def updateData(self, key):
        lValue = self.getData(key)
        GSQLite.Instance().queryWrite("""
        update CONFIG_PYTHON 
        set CONFIG_VALUE = '{1}'
        where CONFIG_KEY = '{0}'
        """.format(key, lValue))
#================================================
from .GSQLite import GSQLite
#================================================
