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
        print(GManager.Instance().getWidth("10;20", 1, 50))
        GSQLite.Instance()
    #================================================
    def runUi(self):
        GProcessUi.Instance().run()
#================================================
from .GProcessUi import GProcessUi
from .GSQLite import GSQLite
from .GManager import GManager
#================================================
