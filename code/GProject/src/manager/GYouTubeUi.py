#================================================
class GYouTubeUi:
    #================================================
    m_instance = None
    #================================================
    def __init__(self):
        pass
    #================================================
    @staticmethod 
    def Instance():
        if GYouTubeUi.m_instance == None:
            GYouTubeUi.m_instance = GYouTubeUi()
        return GYouTubeUi.m_instance
    #================================================
    def run(self):
        self.G_STATE = "S_INIT"
        while True:
            if self.G_STATE == "S_ADMIN" : self.run_ADMIN()
            elif self.G_STATE == "S_INIT" : self.run_INIT()
            elif self.G_STATE == "S_METHOD" : self.run_METHOD()
            elif self.G_STATE == "S_CHOICE" : self.run_CHOICE()
            #
            elif self.G_STATE == "S_VIDEO_INFO_VIDEO_URL" : self.run_VIDEO_INFO_VIDEO_URL()
            elif self.G_STATE == "S_VIDEO_INFO" : self.run_VIDEO_INFO()
            #
            elif self.G_STATE == "S_VIDEO_LOAD_VIDEO_URL" : self.run_VIDEO_LOAD_VIDEO_URL()
            elif self.G_STATE == "S_VIDEO_LOAD_VIDEO_PATH" : self.run_VIDEO_LOAD_VIDEO_PATH()
            elif self.G_STATE == "S_VIDEO_LOAD" : self.run_VIDEO_LOAD()
            #
            elif self.G_STATE == "S_AUDIO_ONLY_LOAD_VIDEO_URL" : self.run_AUDIO_ONLY_LOAD_VIDEO_URL()
            elif self.G_STATE == "S_AUDIO_ONLY_LOAD_AUDIO_PATH" : self.run_AUDIO_ONLY_LOAD_AUDIO_PATH()
            elif self.G_STATE == "S_AUDIO_ONLY_LOAD" : self.run_AUDIO_ONLY_LOAD()
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
        print("\t%-2s : %s" % ("1", "afficher les infos sur une video"))
        print("\t%-2s : %s" % ("2", "telecharger une video"))
        print("\t%-2s : %s" % ("3", "telecharger le son audio seule"))
        print("")
        self.G_STATE = "S_CHOICE"
    #================================================
    def run_CHOICE(self):
        lLast = GConfig.Instance().getData("G_YOUTUBE_ID")
        lAnswer = input("PYTHON_YOUTUBE (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        #
        elif lAnswer == "1" : self.G_STATE = "S_VIDEO_INFO_VIDEO_URL" ; GConfig.Instance().setData("G_YOUTUBE_ID", lAnswer)
        elif lAnswer == "2" : self.G_STATE = "S_VIDEO_LOAD_VIDEO_URL" ; GConfig.Instance().setData("G_YOUTUBE_ID", lAnswer)
        elif lAnswer == "3" : self.G_STATE = "S_AUDIO_ONLY_LOAD_VIDEO_URL" ; GConfig.Instance().setData("G_YOUTUBE_ID", lAnswer)
        #
    #================================================
    def run_VIDEO_INFO_VIDEO_URL(self):
        lLast = GConfig.Instance().getData("G_VIDEO_URL")
        lAnswer = input("G_VIDEO_URL (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        elif lAnswer == "-v" : self.G_STATE = "S_VIDEO_INFO"
        elif lAnswer != "" : self.G_STATE = "S_VIDEO_INFO" ; GConfig.Instance().setData("G_VIDEO_URL", lAnswer)
    #================================================
    def run_VIDEO_INFO(self):
        print("")
        lUrl = GConfig.Instance().getData("G_VIDEO_URL");
        GPafy.Instance().videoInfo(lUrl)
        self.G_STATE = "S_SAVE"
    #================================================
    def run_VIDEO_LOAD_VIDEO_URL(self):
        lLast = GConfig.Instance().getData("G_VIDEO_URL")
        lAnswer = input("G_VIDEO_URL (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        elif lAnswer == "-v" : self.G_STATE = "S_VIDEO_LOAD"
        elif lAnswer != "" : self.G_STATE = "S_VIDEO_LOAD_VIDEO_PATH" ; GConfig.Instance().setData("G_VIDEO_URL", lAnswer)
    #================================================
    def run_VIDEO_LOAD_VIDEO_PATH(self):
        lLast = GConfig.Instance().getData("G_VIDEO_PATH")
        lAnswer = input("G_VIDEO_PATH (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        elif lAnswer == "-v" : self.G_STATE = "S_VIDEO_LOAD"
        elif lAnswer != "" : self.G_STATE = "S_VIDEO_LOAD" ; GConfig.Instance().setData("G_VIDEO_PATH", lAnswer)
    #================================================
    def run_VIDEO_LOAD(self):
        print("")
        lUrl = GConfig.Instance().getData("G_VIDEO_URL");
        lPath = GConfig.Instance().getData("G_VIDEO_PATH");
        GPafy.Instance().videoLoad(lUrl, lPath)
        self.G_STATE = "S_SAVE"
    #================================================
    def run_AUDIO_ONLY_LOAD_VIDEO_URL(self):
        lLast = GConfig.Instance().getData("G_VIDEO_URL")
        lAnswer = input("G_VIDEO_URL (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        elif lAnswer == "-v" : self.G_STATE = "S_AUDIO_ONLY_LOAD"
        elif lAnswer != "" : self.G_STATE = "S_AUDIO_ONLY_LOAD_AUDIO_PATH" ; GConfig.Instance().setData("G_VIDEO_URL", lAnswer)
    #================================================
    def run_AUDIO_ONLY_LOAD_AUDIO_PATH(self):
        lLast = GConfig.Instance().getData("G_AUDIO_PATH")
        lAnswer = input("G_AUDIO_PATH (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        elif lAnswer == "-v" : self.G_STATE = "S_AUDIO_ONLY_LOAD"
        elif lAnswer != "" : self.G_STATE = "S_AUDIO_ONLY_LOAD" ; GConfig.Instance().setData("G_AUDIO_PATH", lAnswer)
    #================================================
    def run_AUDIO_ONLY_LOAD(self):
        print("")
        lUrl = GConfig.Instance().getData("G_VIDEO_URL");
        lPath = GConfig.Instance().getData("G_VIDEO_PATH");
        GPafy.Instance().audioOnly(lUrl, lPath)
        self.G_STATE = "S_SAVE"
    #================================================
    def run_SAVE(self):
        GConfig.Instance().saveData("G_YOUTUBE_ID")
        GConfig.Instance().saveData("G_VIDEO_URL")
        GConfig.Instance().saveData("G_VIDEO_PATH")
        GConfig.Instance().saveData("G_AUDIO_PATH")
        self.G_STATE = "S_QUIT"
    #================================================
    def run_LOAD(self):
        GConfig.Instance().loadData("G_YOUTUBE_ID")
        GConfig.Instance().loadData("G_VIDEO_URL")
        GConfig.Instance().loadData("G_VIDEO_PATH")
        GConfig.Instance().loadData("G_AUDIO_PATH")
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
from .GConfig import GConfig
from .GProcess import GProcess
from .GPafy import GPafy
#================================================
