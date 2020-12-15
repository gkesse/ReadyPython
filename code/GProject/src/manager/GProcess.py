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
        lApp = GManager.Instance().getData().app
        print(lApp.app_name)
        lApp.app_name = "ReadyDoc"
        lApp = GManager.Instance().getData().app
        print(lApp.app_name)
    #================================================
    def runUi(self):
        GProcessUi.Instance().run()
#================================================
from .GProcessUi import GProcessUi
from .GManager import GManager
#================================================
