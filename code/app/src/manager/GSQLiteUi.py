#================================================
import sys
#================================================
class GSQLiteUi:
    #================================================
    m_instance = None
    #================================================
    def __init__(self):
        pass
    #================================================
    @staticmethod 
    def Instance():
        if GSQLiteUi.m_instance == None:
            GSQLiteUi.m_instance = GSQLiteUi()
        return GSQLiteUi.m_instance
    #================================================
    def run(self):
        self.G_STATE = "S_INIT"
        while True:
            if self.G_STATE == "S_ADMIN" : self.run_ADMIN()
            elif self.G_STATE == "S_INIT" : self.run_INIT()
            elif self.G_STATE == "S_METHOD" : self.run_METHOD()
            elif self.G_STATE == "S_CHOICE" : self.run_CHOICE()
            #
            elif self.G_STATE == "S_TABLES_SHOW" : self.run_TABLES_SHOW()
            elif self.G_STATE == "S_CONFIG_DATA_SHOW" : self.run_CONFIG_DATA_SHOW()
            elif self.G_STATE == "S_CONFIG_DATA_CREATE" : self.run_CONFIG_DATA_CREATE()
            elif self.G_STATE == "S_CONFIG_DATA_DROP" : self.run_CONFIG_DATA_DROP()
            #
            elif self.G_STATE == "S_CONFIG_DATA_DELETE_KEY_NAME" : self.run_CONFIG_DATA_DELETE_KEY_NAME()
            elif self.G_STATE == "S_CONFIG_DATA_DELETE" : self.run_CONFIG_DATA_DELETE()
            #
            elif self.G_STATE == "S_SAVE" : self.run_SAVE()
            elif self.G_STATE == "S_LOAD" : self.run_LOAD()
            elif self.G_STATE == "S_QUIT" : self.run_QUIT()
            else : break
    #================================================
    def run_ADMIN(self):
        GProcess.Instance().run()
        self.G_STATE = "S_END"
    #================================================
    def run_INIT(self):
        sys.stdout.write("\n")
        sys.stdout.write("PYTHON_SQLITE !!!\n")
        sys.stdout.write("\t%-2s : %s\n" % ("-q", "quitter l'application"))
        sys.stdout.write("\t%-2s : %s\n" % ("-i", "reinitialiser l'application"))
        sys.stdout.write("\t%-2s : %s\n" % ("-a", "redemarrer l'application"))
        sys.stdout.write("\t%-2s : %s\n" % ("-v", "valider les configurations"))
        sys.stdout.write("\n")
        self.G_STATE = "S_LOAD"
    #================================================
    def run_METHOD(self):
        sys.stdout.write("PYTHON_SQLITE :\n")
        sys.stdout.write("\t%-2s : %s\n" % ("1", "afficher les tables"))
        sys.stdout.write("\t%-2s : %s\n" % ("2", "afficher les donnees CONFIG_DATA"))
        sys.stdout.write("\t%-2s : %s\n" % ("3", "creer la table CONFIG_DATA"))
        sys.stdout.write("\t%-2s : %s\n" % ("4", "supprimer la table CONFIG_DATA"))
        sys.stdout.write("\t%-2s : %s\n" % ("5", "supprimer une donnee CONFIG_DATA"))
        sys.stdout.write("\n")
        self.G_STATE = "S_CHOICE"
    #================================================
    def run_CHOICE(self):
        lLast = GConfig.Instance().getData("G_SQLITE_ID")
        lAnswer = raw_input("PYTHON_SQLITE (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        #
        elif lAnswer == "1" : self.G_STATE = "S_TABLES_SHOW" ; GConfig.Instance().setData("G_SQLITE_ID", lAnswer)
        elif lAnswer == "2" : self.G_STATE = "S_CONFIG_DATA_SHOW" ; GConfig.Instance().setData("G_SQLITE_ID", lAnswer)
        elif lAnswer == "3" : self.G_STATE = "S_CONFIG_DATA_CREATE" ; GConfig.Instance().setData("G_SQLITE_ID", lAnswer)
        elif lAnswer == "4" : self.G_STATE = "S_CONFIG_DATA_DROP" ; GConfig.Instance().setData("G_SQLITE_ID", lAnswer)
        elif lAnswer == "5" : self.G_STATE = "S_CONFIG_DATA_DELETE_KEY_NAME" ; GConfig.Instance().setData("G_SQLITE_ID", lAnswer)
    #================================================
    def run_CONFIG_DATA_DELETE_KEY_NAME(self):
        lLast = GConfig.Instance().getData("G_KEY_NAME")
        lAnswer = raw_input("G_KEY_NAME (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        elif lAnswer == "-v" : self.G_STATE = "S_CONFIG_DATA_DELETE"
        elif lAnswer != "" : self.G_STATE = "S_CONFIG_DATA_DELETE" ; GConfig.Instance().setData("G_KEY_NAME", lAnswer)
    #================================================
    def run_TABLES_SHOW(self):
        sys.stdout.write("\n")
        GSQLite.Instance().queryShow("""
        select name from sqlite_master 
        where type='table'
        """, "30", 20)
        self.G_STATE = "S_SAVE"
    #================================================
    def run_CONFIG_DATA_SHOW(self):
        sys.stdout.write("\n")
        GSQLite.Instance().queryShow("""
        select * from config_data
        order by config_key
        """, "20;50", 20)
        self.G_STATE = "S_SAVE"
    #================================================
    def run_CONFIG_DATA_CREATE(self):
        sys.stdout.write("\n")
        GSQLite.Instance().queryWrite("""
        create table if not exists config_data (
        config_key text,
        config_value text
        )""")
        self.G_STATE = "S_SAVE"
    #================================================
    def run_CONFIG_DATA_DROP(self):
        sys.stdout.write("\n")
        GSQLite.Instance().queryWrite("""
        drop table if exists config_data
        """)
        self.G_STATE = "S_SAVE"
    #================================================
    def run_CONFIG_DATA_DELETE(self):
        lKey = GConfig.Instance().getData("G_KEY_NAME");
        GSQLite.Instance().queryWrite("""
        delete from config_data
        where config_key = '%s'
        """ % (lKey))
        self.run_CONFIG_DATA_SHOW()
        self.G_STATE = "S_SAVE"
    #================================================
    def run_SAVE(self):
        GConfig.Instance().saveData("G_SQLITE_ID")
        GConfig.Instance().saveData("G_KEY_NAME")
        self.G_STATE = "S_QUIT"
    #================================================
    def run_LOAD(self):
        GConfig.Instance().loadData("G_SQLITE_ID")
        GConfig.Instance().loadData("G_KEY_NAME")
        self.G_STATE = "S_METHOD"
    #================================================
    def run_QUIT(self):
        sys.stdout.write("\n")
        lAnswer = raw_input("PYTHON_QUIT (Oui/[N]on) ? ")
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        elif lAnswer == "o" : self.G_STATE = "S_END"
        elif lAnswer == "n" : self.G_STATE = "S_INIT"
        elif lAnswer == "" : self.G_STATE = "S_INIT"
#================================================
from .GProcess import GProcess
from .GConfig import GConfig
from .GSQLite import GSQLite
#================================================
