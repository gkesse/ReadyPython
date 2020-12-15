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
        """, "20", 20)
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
    def queryWrite(self, sql):
        lConnect = self.open()
        lConnect.execute(sql)
        lConnect.commit()
        lConnect.close()
    #================================================
    def queryShow(self, sql, widthMap, defaultWidth):
        lConnect = self.open()
        lCursor = lConnect.execute(sql)
        lNameMap = lCursor.description
        lColCount = len(lNameMap)
        # sep
        i = 0
        sys.stdout.write("+-")
        while i < lColCount :
            if i != 0 : sys.stdout.write("-+-")
            lWidth = GManager.Instance().getWidth(widthMap, i, defaultWidth)
            j = 0
            while j < lWidth : sys.stdout.write("-") ; j += 1
            i += 1
        sys.stdout.write("-+")
        sys.stdout.write("\n")
        # header
        i = 0
        sys.stdout.write("| ")
        for lNameRow in lNameMap :
            if i != 0 : sys.stdout.write(" | ")
            lName = lNameRow[0]
            lWidth = GManager.Instance().getWidth(widthMap, i, defaultWidth)
            sys.stdout.write("%*s" % (-lWidth, lName))
            i += 1
        sys.stdout.write(" |")
        sys.stdout.write("\n")
        # sep
        i = 0
        sys.stdout.write("+-")
        while i < lColCount :
            if i != 0 : sys.stdout.write("-+-")
            lWidth = GManager.Instance().getWidth(widthMap, i, defaultWidth)
            j = 0
            while j < lWidth : sys.stdout.write("-") ; j += 1
            i += 1
        sys.stdout.write("-+")
        sys.stdout.write("\n")
        # data
        for lDataRow in lCursor :
            sys.stdout.write("| ")
            i = 0
            while i < lColCount :
                if i != 0 : sys.stdout.write(" | ")
                lData = lDataRow[i]
                lWidth = GManager.Instance().getWidth(widthMap, i, defaultWidth)
                sys.stdout.write("%*s" %(-lWidth, lData))
                i += 1
            sys.stdout.write(" |")
            sys.stdout.write("\n")
        # sep
        i = 0
        sys.stdout.write("+-")
        while i < lColCount :
            if i != 0 : sys.stdout.write("-+-")
            lWidth = GManager.Instance().getWidth(widthMap, i, defaultWidth)
            j = 0
            while j < lWidth : sys.stdout.write("-") ; j += 1
            i += 1
        sys.stdout.write("-+")
        sys.stdout.write("\n")
        # close
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
