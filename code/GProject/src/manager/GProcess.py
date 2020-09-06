#================================================
class GProcess:
    #================================================
    m_instance = None
    #================================================
    def __init__(self):
        pass
    #================================================
    @staticmethod 
    def Instance():
        if GProcess.m_instance == None:
            GProcess.m_instance = GProcess()
        return GProcess.m_instance
    #================================================
    def run(self):
        self.G_STATE = "S_INIT"
        while True:
            if self.G_STATE == "S_INIT" : self.run_INIT()
            elif self.G_STATE == "S_METHOD" : self.run_METHOD()
            elif self.G_STATE == "S_CHOICE" : self.run_CHOICE()
            elif self.G_STATE == "S_YOUTUBE" : self.run_YOUTUBE()
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
        print("")
        self.G_STATE = "S_CHOICE"
    #================================================
    def run_CHOICE(self):
        lAnswer = input("PYTHON_ADMIN ? ")
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "1" : self.G_STATE = "S_YOUTUBE"
    #================================================
    def run_YOUTUBE(self):
        print("")
        print("run_YOUTUBE")
        self.G_STATE = "S_SAVE"
    #================================================
    def run_SAVE(self):
        self.G_STATE = "S_END"
    #================================================
    def run_LOAD(self):
        self.G_STATE = "S_METHOD"
#================================================
