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
        lCheck = self.countData(key)
        if lCheck == 0 : self.insertData(key)
        else : self.updateData(key)
    #================================================
    def loadData(self, key):
        lValue = GSQLite.Instance().queryValue("""
        select config_value from config_data 
        where config_key='%s'
        """ % (key))
        self.setData(key, lValue)
    #================================================
    def countData(self, key):
        lCount = GSQLite.Instance().queryValue("""
        select count(*) from config_data 
        where config_key='%s'
        """ % (key))
        return lCount
    #================================================
    def insertData(self, key):
        lValue = self.getData(key)
        GSQLite.Instance().queryWrite("""
        insert into config_data (config_key, config_value)
        values ('%s', '%s')
        """ % (key, lValue))
    #================================================
    def updateData(self, key):
        lValue = self.getData(key)
        GSQLite.Instance().queryWrite("""
        update config_data 
        set config_value = '%s'
        where config_key = '%s'
        """ % (lValue, key))
#================================================
from .GSQLite import GSQLite
#================================================
