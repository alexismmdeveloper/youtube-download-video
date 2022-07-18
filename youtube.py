from pytube import YouTube
from sys import argv
import os

# variable path
path_folder = "C:/Users/*/Desktop"
# variable folder name
folder_name = "YT-DOWNLOAD"
path = f"{path_folder}\{folder_name}"

def DownloadVideo(link):
    yt = YouTube(link)
    print(f"=> Downloading video of {yt.author}")
    Folder()
    video = yt.streams.get_highest_resolution()
    print(f"=> Video download successfully")
    video.download(path)

def DownloadMusic(link):
    yt = YouTube(link)
    print(f"=> Downloading music of {yt.author}")
    Folder()
    music = yt.streams.get_audio_only()
    music.download(path)
    print(f"=> Music download successfully")

def InfVideo(link):
    yt = YouTube(link)
    print("=> Title:", yt.title)
    print("=> Views:", "{:,}".format(yt.views), "views")
    print("=> Autor:", yt.author, "\n")

def Help():
    print("HELP YOUTUBE DOWNLOAD \n")
    print(f"Enter Path => youtube.py 'option' 'url-youtube' \n")
    print("-h => Help commands")
    print("-v => Download Video")
    print("-m => Download Music")
    print("-i => Download Video and Information")

def Folder():
    folder_list = os.listdir(path_folder)
    if folder_name in folder_list: pass
    else: os.makedirs(path)

def OpenFolder():
    os.startfile(path)

def OptionsSistem(argv):
    if len(argv) == 3:
        options = argv[1]
        link = argv[2]
        
        if options == "-v": DownloadVideo(link)
        elif options == "-m": DownloadMusic(link)
        elif options == "-i": InfVideo(link)
        else: Help()

    elif len(argv) == 2:
        options = argv[1]
        if options == "-f": OpenFolder()
        else: Help()
    else:
        Help()

try:
    OptionsSistem(argv)
except:
    print("=> Something went wrong, Try again later")