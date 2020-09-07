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
        print("%-30s : %s" % ("url", url))
        print("%-30s : %s" % ("lVideo.title", lVideo.title))
        print("%-30s : %s" % ("lVideo.rating", lVideo.rating))
        print("%-30s : %s" % ("lVideo.viewcount", lVideo.viewcount))
        print("%-30s : %s" % ("lVideo.author", lVideo.author))
        print("%-30s : %s" % ("lVideo.length", lVideo.length))
        print("%-30s : %s" % ("lVideo.duration", lVideo.duration))
        print("%-30s : %s" % ("lVideo.likes", lVideo.likes))
        print("%-30s : %s" % ("lVideo.dislikes", lVideo.dislikes))
        print("")

        lBestVideo = lVideo.getbest()
        print("%-30s : %s" % ("lBestVideo.resolution", lBestVideo.resolution))       
        print("%-30s : %s" % ("lBestVideo.extension", lBestVideo.extension))       
        print("%-30s : %s" % ("lBestVideo.get_filesize()", lBestVideo.get_filesize()))       
        print("%-30s : %s" % ("lBestVideo.url", lBestVideo.url))       
        print("")
        
        lBestAudio = lVideo.getbestaudio()
        print("%-30s : %s" % ("lBestAudio.bitrate", lBestAudio.bitrate))       
        print("%-30s : %s" % ("lBestAudio.extension", lBestAudio.extension))       
        print("%-30s : %s" % ("lBestAudio.get_filesize()", lBestAudio.get_filesize()))       
        print("")
    #================================================
    def videoLoad(self, url, path):
        lVideo = pafy.new(url)
        lTitle = lVideo.title
        lBestVideo = lVideo.getbest()
        lExtension = lBestVideo.extension
        lFilename = "{0}/{1}.{2}".format(path, lTitle, lExtension)
        lBestVideo.download(filepath=lFilename)    
    #================================================
    def videoOnly(self, url, path):
        lVideo = pafy.new(url)
        lTitle = lVideo.title
        lBestVideo = lVideo.getbestvideo()
        print(lBestVideo)
        lExtension = lBestVideo.extension
        lFilename = "{0}/{1}.{2}".format(path, lTitle, lExtension)
        lBestVideo.download(filepath=lFilename)    
    #================================================
    def audioOnly(self, url, path):
        lVideo = pafy.new(url)
        lTitle = lVideo.title
        lBestAudio = lVideo.getbestaudio()
        lExtension = lBestAudio.extension
        lFilename = "{0}/{1}.{2}".format(path, lTitle, lExtension)
        lBestAudio.download(filepath=lFilename)    
#================================================
