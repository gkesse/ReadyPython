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
        print("\t%-2s : %s" % ("2", "afficher les donnees CONFIG_DATA"))
        print("")
        self.G_STATE = "S_CHOICE"
    #================================================
    def run_CHOICE(self):
        lLast = GConfig.Instance().getData("PYTHON_SQLITE_ID")
        lAnswer = input("PYTHON_SQLITE (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        #
        elif lAnswer == "1" : self.G_STATE = "S_TABLES_SHOW" ; GConfig.Instance().setData("PYTHON_SQLITE_ID", lAnswer)
        elif lAnswer == "2" : self.G_STATE = "S_CONFIG_DATA_SHOW" ; GConfig.Instance().setData("PYTHON_SQLITE_ID", lAnswer)
    #================================================
    def run_TABLES_SHOW(self):
        print("")
        GSQLite.Instance().queryShow("""
        select name from sqlite_master 
        where type='table'
        """)
        self.G_STATE = "S_SAVE"
    #================================================
    def run_CONFIG_DATA_SHOW(self):
        print("")
        GSQLite.Instance().queryShow("""
        select * from CONFIG_DATA
        order by CONFIG_KEY
        """)
        self.G_STATE = "S_SAVE"
    #================================================
    def run_SAVE(self):
        self.G_STATE = "S_QUIT"
    #================================================
    def run_LOAD(self):
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
