#================================================
import sys
import sqlite3
#================================================
class GSQLite:
    #================================================
    m_instance = None
    #================================================
    def __init__(self):
        pass
    #================================================
    @staticmethod 
    def Instance():
        if GSQLite.m_instance == None:
            GSQLite.m_instance = GSQLite()
        return GSQLite.m_instance
    #================================================
    def test(self):
        self.queryShow("SELECT name FROM sqlite_master WHERE type='table'")
        sys.exit()
    #================================================
    def queryWrite(self, sql):
        lSqliteF = GManager.Instance().getData("sqlite.file")
        lSqlite = sqlite3.connect(lSqliteF)
        lSqlite.execute(sql)
        lSqlite.close()
    #================================================
    def queryInsert(self, sql):
        lSqliteF = GManager.Instance().getData("sqlite.file")
        lSqlite = sqlite3.connect(lSqliteF)
        lSqlite.execute(sql)
        lSqlite.commit()
        lSqlite.close()
    #================================================
    def queryShow(self, sql):
        lSqliteF = GManager.Instance().getData("sqlite.file")
        lSqlite = sqlite3.connect(lSqliteF)
        lDataMap = lSqlite.execute(sql)
        for lData in lDataMap :
            print(lData)
        lSqlite.close()
#================================================
from .GManager import GManager
#================================================
