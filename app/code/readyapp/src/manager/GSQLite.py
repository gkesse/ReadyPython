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
        sys.stdout.write("+-")
        for i in range(lColCount) :
            if i != 0 : sys.stdout.write("-+-")
            lWidth = GManager.Instance().getWidth(widthMap, i, defaultWidth)
            for j in range(lWidth) : sys.stdout.write("-")
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
        sys.stdout.write("+-")
        for i in range(lColCount) :
            if i != 0 : sys.stdout.write("-+-")
            lWidth = GManager.Instance().getWidth(widthMap, i, defaultWidth)
            for j in range(lWidth) : sys.stdout.write("-")
        sys.stdout.write("-+")
        sys.stdout.write("\n")
        # data
        for lDataRow in lCursor :
            sys.stdout.write("| ")
            for i in range(lColCount) :
                if i != 0 : sys.stdout.write(" | ")
                lData = lDataRow[i]
                lWidth = GManager.Instance().getWidth(widthMap, i, defaultWidth)
                sys.stdout.write("%*s" %(-lWidth, lData))
            sys.stdout.write(" |")
            sys.stdout.write("\n")
        # sep
        sys.stdout.write("+-")
        for i in range(lColCount) :
            if i != 0 : sys.stdout.write("-+-")
            lWidth = GManager.Instance().getWidth(widthMap, i, defaultWidth)
            for j in range(lWidth) : sys.stdout.write("-")
        sys.stdout.write("-+")
        sys.stdout.write("\n")
        # close
        lConnect.close()
    #================================================
    def queryValue(self, sql):
        lConnect = self.open()
        lCursor = lConnect.execute(sql)
        lData = ""
        for lDataRow in lCursor :
            lData = lDataRow[0]
            break
        lConnect.close()
        return lData
    #================================================
    def queryCol(self, sql):
        lConnect = self.open()
        lCursor = lConnect.execute(sql)
        lDataMap = []
        for lDataRow in lCursor :
            lData = lDataRow[0]
            lDataMap.append(lData)
        lConnect.close()
        return lDataMap
    #================================================
    def queryRow(self, sql):
        lConnect = self.open()
        lCursor = lConnect.execute(sql)
        lColCount = len(lCursor.description)
        lDataMap = []
        for lDataRow in lCursor :
            for i in range(lColCount) :
                lData = lDataRow[i]
                lDataMap.append(lData)
            break
        lConnect.close()
        return lDataMap
    #================================================
    def queryMap(self, sql):
        lConnect = self.open()
        lCursor = lConnect.execute(sql)
        lColCount = len(lCursor.description)
        lDataMap = []
        for lDataRow in lCursor :
            lDataCol = []
            for i in range(lColCount) :
                lData = lDataRow[i]
                lDataCol.append(lData)
            lDataMap.append(lDataCol)
        lConnect.close()
        return lDataMap
#================================================
from .GManager import GManager
#================================================
