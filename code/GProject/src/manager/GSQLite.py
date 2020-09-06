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
        self.queryShow("""
        select name from sqlite_master 
        where type='table'
        """)
        self.queryShow("""
        select count(*) from CONFIG_DATA 
        where CONFIG_KEY='G_TEST_PATH'
        """)
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
