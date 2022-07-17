from pytube import YouTube
from sys import argv

link = argv[1]

def YouTubeVideo(link):
    print("-------- YOUTUBE DOWNLOAD VIDEO -------- \n")
    print("=> Title:", yt.title)
    print("=> Views:", "{:,}".format(yt.views), "views")
    print("=> Autor:", yt.author, "\n")

    print(f"=> Downloading video of {yt.author}")
    yd = yt.streams.get_highest_resolution()
    yd.download()
    if(yd.is_progressive):
        print(f"=> Video download successfully")

try:
    yt = YouTube(link)
    YouTubeVideo(link)
except:
    print("-------- YOUTUBE DOWNLOAD VIDEO -------- \n")
    print("=> Something went wrong, Try again later")

