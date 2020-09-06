#================================================
from manager.GProcess import GProcess
from manager.GSQLite import GSQLite
#================================================
def GMain():
    #GSQLite.Instance().test()
    GProcess.Instance().run()
#================================================
GMain()
#================================================
