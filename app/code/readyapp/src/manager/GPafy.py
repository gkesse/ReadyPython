#================================================
import sys
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
    # video
    #================================================
    def showInfo(self, url):
        lVideo = pafy.new(url)
        sys.stdout.write("%-30s : %s\n" % ("url", url))
        sys.stdout.write("%-30s : %s\n" % ("lVideo.title", lVideo.title))
        sys.stdout.write("%-30s : %s\n" % ("lVideo.rating", lVideo.rating))
        sys.stdout.write("%-30s : %s\n" % ("lVideo.viewcount", lVideo.viewcount))
        sys.stdout.write("%-30s : %s\n" % ("lVideo.author", lVideo.author))
        sys.stdout.write("%-30s : %s\n" % ("lVideo.length", lVideo.length))
        sys.stdout.write("%-30s : %s\n" % ("lVideo.duration", lVideo.duration))
        sys.stdout.write("%-30s : %s\n" % ("lVideo.likes", lVideo.likes))
        sys.stdout.write("%-30s : %s\n" % ("lVideo.dislikes", lVideo.dislikes))
        sys.stdout.write("\n")

        lBestVideo = lVideo.getbest()
        sys.stdout.write("%-30s : %s\n" % ("lBestVideo.resolution", lBestVideo.resolution))       
        sys.stdout.write("%-30s : %s\n" % ("lBestVideo.extension", lBestVideo.extension))       
        sys.stdout.write("%-30s : %s\n" % ("lBestVideo.get_filesize()", lBestVideo.get_filesize()))       
        sys.stdout.write("%-30s : %s\n" % ("lBestVideo.url", lBestVideo.url))       
        sys.stdout.write("\n")
        
        lBestAudio = lVideo.getbestaudio()
        sys.stdout.write("%-30s : %s\n" % ("lBestAudio.bitrate", lBestAudio.bitrate))       
        sys.stdout.write("%-30s : %s\n" % ("lBestAudio.extension", lBestAudio.extension))       
        sys.stdout.write("%-30s : %s\n" % ("lBestAudio.get_filesize()", lBestAudio.get_filesize()))       
        sys.stdout.write("\n")
    #================================================
    def loadVideo(self, url):
        lApp = GManager.Instance().getData().app
        lVideo = pafy.new(url)
        lTitle = lVideo.title
        lBestVideo = lVideo.getbest()
        lExtension = lBestVideo.extension
        lTitle = GManager.Instance().validPath(lTitle)
        lFilename = "%s%s%s.%s" % (lApp.video_path, lApp.separator, lTitle, lExtension)
        lBestVideo.download(filepath=lFilename)
        sys.stdout.write("%s\n" % (lFilename))
#================================================
from .GManager import GManager
#================================================
