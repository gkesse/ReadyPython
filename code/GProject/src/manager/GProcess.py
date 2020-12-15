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
        if(len(sys.argv) > 1) : lKey = sys.argv[1]
        if(lKey == "test") : runTest() ; return
        if(lKey == "ui") : runUi() ; return
        runTest()
    #================================================
    def run(self):
        lKey = "test"
        if(len(sys.argv) > 1) : lKey = sys.argv[1]
        if(lKey == "test") : runTest() ; return
        if(lKey == "ui") : runUi() ; return
        runTest()
    #================================================
    def runTest(self):
        print(runTest())
    #================================================
    def runUi(self):
        print(runUi())
#================================================
