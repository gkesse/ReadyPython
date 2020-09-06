#================================================
class GYouTube:
    #================================================
    m_instance = None
    #================================================
    def __init__(self):
        pass
    #================================================
    @staticmethod 
    def Instance():
        if GYouTube.m_instance == None:
            GYouTube.m_instance = GYouTube()
        return GYouTube.m_instance
    #================================================
    def run(self):
        self.G_STATE = "S_INIT"
        while True:
            if self.G_STATE == "S_ADMIN" : self.run_ADMIN()
            elif self.G_STATE == "S_INIT" : self.run_INIT()
            elif self.G_STATE == "S_METHOD" : self.run_METHOD()
            elif self.G_STATE == "S_CHOICE" : self.run_CHOICE()
            elif self.G_STATE == "S_VIDEO_LOAD" : self.run_VIDEO_LOAD()
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
        print("PYTHON_YOUTUBE !!!")
        print("\t%-2s : %s" % ("-q", "quitter l'application"))
        print("\t%-2s : %s" % ("-i", "reinitialiser l'application"))
        print("\t%-2s : %s" % ("-a", "redemarrer l'application"))
        print("\t%-2s : %s" % ("-v", "valider les configurations"))
        print("")
        self.G_STATE = "S_LOAD"
    #================================================
    def run_METHOD(self):
        print("PYTHON_YOUTUBE :")
        print("\t%-2s : %s" % ("1", "S_VIDEO_LOAD"))
        print("")
        self.G_STATE = "S_CHOICE"
    #================================================
    def run_CHOICE(self):
        lAnswer = input("PYTHON_YOUTUBE ? ")
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "S_VIDEO_LOAD" : self.G_STATE = "S_VIDEO_LOAD"
    #================================================
    def run_VIDEO_LOAD(self):
        print("")
        print("run_VIDEO_LOAD")
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
        lAnswer = input("PYTHON_QUIT ? ")
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "o" : self.G_STATE = "S_END"
        elif lAnswer == "n" : self.G_STATE = "S_INIT"
        elif lAnswer == "" : self.G_STATE = "S_INIT"
#================================================
