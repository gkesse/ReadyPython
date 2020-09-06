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
        lSql = """
        select CONFIG_VALUE from CONFIG_PYTHON 
        where CONFIG_KEY='{0}'
        """.format(key)
        lValue = GSQLite.Instance().queryValue(lSql)
        self.setData(key, lValue)
    #================================================
    def checkData(self, key):
        lSql = """
        select count(*) from CONFIG_PYTHON 
        where CONFIG_KEY='{0}'
        """.format(key)
        lCount = GSQLite.Instance().queryValue(lSql)
        return lCount
    #================================================
    def insertData(self, key):
        lValue = self.getData(key)
        lSql = """
        insert into CONFIG_PYTHON (CONFIG_KEY, CONFIG_VALUE)
        values ('{0}', '{1}')
        """.format(key, lValue)
        GSQLite.Instance().queryWrite(lSql)
    #================================================
    def updateData(self, key):
        lValue = self.getData(key)
        lSql = """
        update CONFIG_PYTHON 
        set CONFIG_VALUE = '{1}'
        where CONFIG_KEY = '{0}'
        """.format(key, lValue)
        GSQLite.Instance().queryWrite(lSql)
#================================================
from .GSQLite import GSQLite
#================================================
