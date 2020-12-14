#================================================
class GProcessUi:
    #================================================
    m_instance = None
    #================================================
    def __init__(self): 
        pass
    #================================================
    @staticmethod 
    def Instance():
        if GProcessUi.m_instance == None:
            GProcessUi.m_instance = GProcessUi()
        return GProcessUi.m_instance
    #================================================
    def run(self):
        self.G_STATE = "S_INIT"
        while True:
            if self.G_STATE == "S_INIT" : self.run_INIT()
            elif self.G_STATE == "S_METHOD" : self.run_METHOD()
            elif self.G_STATE == "S_CHOICE" : self.run_CHOICE()
            elif self.G_STATE == "S_YOUTUBE" : self.run_YOUTUBE()
            elif self.G_STATE == "S_SQLITE" : self.run_SQLITE()
            elif self.G_STATE == "S_SAVE" : self.run_SAVE()
            elif self.G_STATE == "S_LOAD" : self.run_LOAD()
            else : break
    #================================================
    def run_INIT(self):
        print("")
        print("PYTHON_ADMIN !!!")
        print("\t%-2s : %s" % ("-q", "quitter l'application"))
        print("")
        self.G_STATE = "S_LOAD"
    #================================================
    def run_METHOD(self):
        print("PYTHON_ADMIN :")
        print("\t%-2s : %s" % ("1", "S_YOUTUBE"))
        print("\t%-2s : %s" % ("2", "S_SQLITE"))
        print("")
        self.G_STATE = "S_CHOICE"
    #================================================
    def run_CHOICE(self):
        lLast = GConfig.Instance().getData("G_ADMIN_ID")
        lAnswer = input("PYTHON_ADMIN (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "1" : self.G_STATE = "S_YOUTUBE" ; GConfig.Instance().setData("G_ADMIN_ID", lAnswer)
        elif lAnswer == "2" : self.G_STATE = "S_SQLITE" ; GConfig.Instance().setData("G_ADMIN_ID", lAnswer)
    #================================================
    def run_YOUTUBE(self):
        print("")
        GYouTubeUi.Instance().run()
        self.G_STATE = "S_SAVE"
    #================================================
    def run_SQLITE(self):
        print("")
        GSQLiteUi.Instance().run()
        self.G_STATE = "S_SAVE"
    #================================================
    def run_SAVE(self):
        GConfig.Instance().saveData("G_ADMIN_ID")
        self.G_STATE = "S_END"
    #================================================
    def run_LOAD(self):
        GConfig.Instance().loadData("G_ADMIN_ID")
        self.G_STATE = "S_METHOD"
#================================================
from .GConfig import GConfig
from .GYouTubeUi import GYouTubeUi
from .GSQLiteUi import GSQLiteUi
#================================================
