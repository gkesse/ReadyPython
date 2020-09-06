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
            elif self.G_STATE == "S_CONFIG_SHOW" : self.run_CONFIG_SHOW()
            elif self.G_STATE == "S_CONFIG_CREATE" : self.run_CONFIG_CREATE()
            elif self.G_STATE == "S_CONFIG_DROP" : self.run_CONFIG_DROP()
            #
            elif self.G_STATE == "S_CONFIG_DELETE_KEY_NAME" : self.run_CONFIG_DELETE_KEY_NAME()
            elif self.G_STATE == "S_CONFIG_DELETE" : self.run_CONFIG_DELETE()
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
        print("")
        print("PYTHON_SQLITE !!!")
        print("\t%-2s : %s" % ("-q", "quitter l'application"))
        print("\t%-2s : %s" % ("-i", "reinitialiser l'application"))
        print("\t%-2s : %s" % ("-a", "redemarrer l'application"))
        print("\t%-2s : %s" % ("-v", "valider les configurations"))
        print("")
        self.G_STATE = "S_LOAD"
    #================================================
    def run_METHOD(self):
        print("PYTHON_SQLITE :")
        print("\t%-2s : %s" % ("1", "afficher les tables CONFIG_O"))
        print("\t%-2s : %s" % ("2", "afficher les donnees CONFIG_PYTHON"))
        print("\t%-2s : %s" % ("3", "creer la table CONFIG_PYTHON"))
        print("\t%-2s : %s" % ("4", "supprimer la table CONFIG_PYTHON"))
        print("\t%-2s : %s" % ("5", "supprimer une donnee CONFIG_PYTHON"))
        print("")
        self.G_STATE = "S_CHOICE"
    #================================================
    def run_CHOICE(self):
        lLast = GConfig.Instance().getData("G_SQLITE_ID")
        lAnswer = input("PYTHON_SQLITE (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        #
        elif lAnswer == "1" : self.G_STATE = "S_TABLES_SHOW" ; GConfig.Instance().setData("G_SQLITE_ID", lAnswer)
        elif lAnswer == "2" : self.G_STATE = "S_CONFIG_SHOW" ; GConfig.Instance().setData("G_SQLITE_ID", lAnswer)
        elif lAnswer == "3" : self.G_STATE = "S_CONFIG_CREATE" ; GConfig.Instance().setData("G_SQLITE_ID", lAnswer)
        elif lAnswer == "4" : self.G_STATE = "S_CONFIG_DROP" ; GConfig.Instance().setData("G_SQLITE_ID", lAnswer)
        elif lAnswer == "5" : self.G_STATE = "S_CONFIG_DELETE_KEY_NAME" ; GConfig.Instance().setData("G_SQLITE_ID", lAnswer)
    #================================================
    def run_CONFIG_DELETE_KEY_NAME(self):
        lLast = GConfig.Instance().getData("G_KEY_NAME")
        lAnswer = input("G_KEY_NAME (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        elif lAnswer == "-v" : self.G_STATE = "S_CONFIG_DELETE"
        elif lAnswer != "" : self.G_STATE = "S_CONFIG_DELETE" ; GConfig.Instance().setData("G_KEY_NAME", lAnswer)
    #================================================
    def run_CONFIG_DELETE(self):
        print("")
        GSQLite.Instance().queryCreate("""
        delete from CONFIG_PYTHON
        where CONFIG_KEY = {0}
        """.format())
        self.G_STATE = "S_SAVE"
    #================================================
    def run_CONFIG_DROP(self):
        print("")
        GSQLite.Instance().queryCreate("""
        drop table CONFIG_PYTHON
        """)
        self.G_STATE = "S_SAVE"
    #================================================
    def run_CONFIG_CREATE(self):
        print("")
        GSQLite.Instance().queryCreate("""
        create table CONFIG_PYTHON (
        CONFIG_KEY text unique not null,
        CONFIG_VALUE text
        )""")
        self.G_STATE = "S_SAVE"
    #================================================
    def run_TABLES_SHOW(self):
        print("")
        GSQLite.Instance().queryShow("""
        select name from sqlite_master 
        where type='table'
        """)
        self.G_STATE = "S_SAVE"
    #================================================
    def run_CONFIG_SHOW(self):
        print("")
        GSQLite.Instance().queryShow("""
        select * from CONFIG_DATA
        order by CONFIG_KEY
        """)
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
        print("")
        lAnswer = input("PYTHON_QUIT (Oui/[N]on) ? ")
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
