#================================================
from pafy import pafy
#================================================
class GPafy:
    #================================================
    m_instance = None
    #================================================
    def __init__(self):
        pass
    #================================================
    @staticmethod 
    def Instance():
        if GPafy.m_instance == None:
            GPafy.m_instance = GPafy()
        return GPafy.m_instance
    #================================================
    def setData(self, key, value):
        self.m_dataMap[key] = value
    #================================================
    def videoInfo(self, url):
        lVideo = pafy.new(url)
        print("%-20s : %s" % ("url", url))
        print("%-20s : %s" % ("lVideo.title", lVideo.title))
        print("%-20s : %s" % ("lVideo.rating", lVideo.rating))
        print("%-20s : %s" % ("lVideo.viewcount", lVideo.viewcount))
        print("%-20s : %s" % ("lVideo.author", lVideo.author))
        print("%-20s : %s" % ("lVideo.length", lVideo.length))
        print("%-20s : %s" % ("lVideo.duration", lVideo.duration))
        print("%-20s : %s" % ("lVideo.likes", lVideo.likes))
        print("%-20s : %s" % ("lVideo.dislikes", lVideo.dislikes))
        print("")
        lStreams = lVideo.streams
        lStream = ""
        for lStream in lStreams :
            break
        print("%-20s : %s" % ("lStream.resolution", lStream.resolution))
        print("%-20s : %s" % ("lStream.extension", lStream.extension))
        print("%-20s : %s" % ("lStream.get_filesize()", lStream.get_filesize()))
        print("%-20s : %s" % ("lStream.url", lStream.url))
        print("")
        lBest = lVideo.getbest()
        print("%-20s : %s" % ("lBest.resolution", lBest.resolution))       
        print("%-20s : %s" % ("lBest.extension", lBest.extension))       
        print("%-20s : %s" % ("lBest.get_filesize()", lBest.get_filesize()))       
        print("%-20s : %s" % ("lBest.url", lBest.url))       
    #================================================
    def videoLoad(self, url, path):
        lVideo = pafy.new(url)
        lTitle = lVideo.title
        lBest = lVideo.getbest()
        lExtension = lBest.extension
        lFilename = "{0}/{1}.{2}".format(path, lTitle, lExtension)
        lBest.download(filepath=lFilename)    
#================================================
