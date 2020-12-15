#================================================
import sys
import sqlite3
#================================================
class GSQLite:
    #================================================
    m_instance = None
    #================================================
    def __init__(self):
        # config_data
        self.queryWrite("""
        create table if not exists config_data ( 
        config_key text,
        config_value text
        )""")
        # config_data
        self.queryShow("""
        select name from sqlite_master 
        where type='table'
        """)
    #================================================
    @staticmethod 
    def Instance():
        if GSQLite.m_instance == None:
            GSQLite.m_instance = GSQLite()
        return GSQLite.m_instance
    #================================================
    def open(self):
        lApp = GManager.Instance().getData().app
        lConnect = sqlite3.connect(lApp.sqlite_db_path)
        return lConnect
    #================================================
    def queryCreate(self, sql):
        lConnect = self.open()
        lConnect.execute(sql)
        lConnect.close()
    #================================================
    def queryWrite(self, sql):
        lConnect = self.open()
        lConnect.execute(sql)
        lConnect.commit()
        lConnect.close()
    #================================================
    def queryShow(self, sql):
        lConnect = self.open()
        lDataMap = lConnect.execute(sql)
        for lData in lDataMap :
            print(lData)
        lConnect.close()
    #================================================
    def queryValue(self, sql):
        lConnect = self.open()
        lDataMap = lConnect.execute(sql)
        lValue = ""
        for lData in lDataMap :
            lValue = lData[0]
        lSqlite.close()
        return lValue
#================================================
from .GManager import GManager
#================================================
