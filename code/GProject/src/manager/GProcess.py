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
            if self.G_STATE == "S_ADMIN" : self.run_ADMIN()
            elif self.G_STATE == "S_INIT" : self.run_INIT()
            elif self.G_STATE == "S_METHOD" : self.run_METHOD()
            elif self.G_STATE == "S_CHOICE" : self.run_CHOICE()
            elif self.G_STATE == "S_SQLITE" : self.run_SQLITE()
            elif self.G_STATE == "S_SAVE" : self.run_SAVE()
            elif self.G_STATE == "S_LOAD" : self.run_LOAD()
            elif self.G_STATE == "S_QUIT" : self.run_QUIT()
            else : break
    #================================================
    def run_ADMIN(self):
        print("run_ADMIN")
        self.G_STATE = "S_END"
    #================================================
    def run_INIT(self):
        print("run_INIT")
        self.G_STATE = "S_LOAD"
    #================================================
    def run_METHOD(self):
        print("run_METHOD")
        self.G_STATE = "S_CHOICE"
    #================================================
    def run_CHOICE(self):
        print("run_CHOICE")
        self.G_STATE = "S_SQLITE"
    #================================================
    def run_SQLITE(self):
        print("run_SQLITE")
        self.G_STATE = "S_SAVE"
    #================================================
    def run_SAVE(self):
        print("run_SAVE")
        self.G_STATE = "S_QUIT"
    #================================================
    def run_LOAD(self):
        print("run_LOAD")
        self.G_STATE = "S_METHOD"
    #================================================
    def run_QUIT(self):
        print("run_QUIT")
        self.G_STATE = "S_END"
#================================================
