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
        sys.stdout.write("\n")
        sys.stdout.write("PYTHON_YOUTUBE !!!\n")
        sys.stdout.write("\t%-2s : %s\n" % ("-q", "quitter l'application"))
        sys.stdout.write("\t%-2s : %s\n" % ("-i", "reinitialiser l'application"))
        sys.stdout.write("\t%-2s : %s\n" % ("-a", "redemarrer l'application"))
        sys.stdout.write("\t%-2s : %s\n" % ("-v", "valider les configurations"))
        sys.stdout.write("\n")
        self.G_STATE = "S_LOAD"
    #================================================
    def run_METHOD(self):
        sys.stdout.write("PYTHON_YOUTUBE :\n")
        sys.stdout.write("\t%-2s : %s\n" % ("1", "afficher les infos sur une video"))
        sys.stdout.write("\t%-2s : %s\n" % ("2", "telecharger une video"))
        sys.stdout.write("\t%-2s : %s\n" % ("3", "telecharger le son audio seule"))
        sys.stdout.write("\n")
        self.G_STATE = "S_CHOICE"
    #================================================
    def run_CHOICE(self):
        lLast = GConfig.Instance().getData("G_YOUTUBE_ID")
        lAnswer = raw_input("PYTHON_YOUTUBE (%s) ? " % (lLast))
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
        lAnswer = raw_input("G_VIDEO_URL (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        elif lAnswer == "-v" : self.G_STATE = "S_VIDEO_INFO"
        elif lAnswer != "" : self.G_STATE = "S_VIDEO_INFO" ; GConfig.Instance().setData("G_VIDEO_URL", lAnswer)
    #================================================
    def run_VIDEO_INFO(self):
        sys.stdout.write("\n")
        lUrl = GConfig.Instance().getData("G_VIDEO_URL");
        GPafy.Instance().videoInfo(lUrl)
        self.G_STATE = "S_SAVE"
    #================================================
    def run_VIDEO_LOAD_VIDEO_URL(self):
        lLast = GConfig.Instance().getData("G_VIDEO_URL")
        lAnswer = raw_input("G_VIDEO_URL (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        elif lAnswer == "-v" : self.G_STATE = "S_VIDEO_LOAD"
        elif lAnswer != "" : self.G_STATE = "S_VIDEO_LOAD_VIDEO_PATH" ; GConfig.Instance().setData("G_VIDEO_URL", lAnswer)
    #================================================
    def run_VIDEO_LOAD_VIDEO_PATH(self):
        lLast = GConfig.Instance().getData("G_VIDEO_PATH")
        lAnswer = raw_input("G_VIDEO_PATH (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        elif lAnswer == "-v" : self.G_STATE = "S_VIDEO_LOAD"
        elif lAnswer != "" : self.G_STATE = "S_VIDEO_LOAD" ; GConfig.Instance().setData("G_VIDEO_PATH", lAnswer)
    #================================================
    def run_VIDEO_LOAD(self):
        sys.stdout.write("\n")
        lUrl = GConfig.Instance().getData("G_VIDEO_URL");
        lPath = GConfig.Instance().getData("G_VIDEO_PATH");
        GPafy.Instance().videoLoad(lUrl, lPath)
        self.G_STATE = "S_SAVE"
    #================================================
    def run_AUDIO_ONLY_LOAD_VIDEO_URL(self):
        lLast = GConfig.Instance().getData("G_VIDEO_URL")
        lAnswer = raw_input("G_VIDEO_URL (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        elif lAnswer == "-v" : self.G_STATE = "S_AUDIO_ONLY_LOAD"
        elif lAnswer != "" : self.G_STATE = "S_AUDIO_ONLY_LOAD_AUDIO_PATH" ; GConfig.Instance().setData("G_VIDEO_URL", lAnswer)
    #================================================
    def run_AUDIO_ONLY_LOAD_AUDIO_PATH(self):
        lLast = GConfig.Instance().getData("G_AUDIO_PATH")
        lAnswer = raw_input("G_AUDIO_PATH (%s) ? " % (lLast))
        if lAnswer == "" : lAnswer = lLast
        if lAnswer == "-q" : self.G_STATE = "S_END"
        elif lAnswer == "-i" : self.G_STATE = "S_INIT"
        elif lAnswer == "-a" : self.G_STATE = "S_ADMIN"
        elif lAnswer == "-v" : self.G_STATE = "S_AUDIO_ONLY_LOAD"
        elif lAnswer != "" : self.G_STATE = "S_AUDIO_ONLY_LOAD" ; GConfig.Instance().setData("G_AUDIO_PATH", lAnswer)
    #================================================
    def run_AUDIO_ONLY_LOAD(self):
        sys.stdout.write("\n")
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
        sys.stdout.write("\n")
        lAnswer = raw_input("PYTHON_QUIT (Oui/[N]on) ? ")
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
