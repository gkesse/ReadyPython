#================================================
import sys
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
        lKey = "test"
        if len(sys.argv) > 1 : lKey = sys.argv[1]
        if lKey == "test" : self.runTest() ; return
        if lKey == "ui" : self.runUi() ; return
        self.runTest()
    #================================================
    def runTest(self):
        print("Bonjour tout le monde")
    #================================================
    def runUi(self):
        GProcessUi.Instance().run()
#================================================
from .GProcessUi import GProcessUi
from .GSQLite import GSQLite
from .GManager import GManager
#================================================
