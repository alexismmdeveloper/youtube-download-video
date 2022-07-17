from pytube import YouTube
from sys import argv
from dotenv import load_dotenv
import os

load_dotenv()

link = argv[1]
path_folder = os.getenv("PATH-FOLDER")
folder_name = "VIDEOS-YOUTUBE"

def DownloadVideo(yt,path):
        video = yt.streams.get_highest_resolution()
        video.download(path)
        if(video.is_progressive):
            print(f"=> Video download successfully")


def YouTubeVideo(link, path_folder, folder_name):
    yt = YouTube(link)
    print("-------- YOUTUBE DOWNLOAD VIDEO -------- \n")
    print("=> Title:", yt.title)
    print("=> Views:", "{:,}".format(yt.views), "views")
    print("=> Autor:", yt.author, "\n")
    print(f"=> Downloading video of {yt.author}")

    path = f"{path_folder}\{folder_name}"

    folder_list = os.listdir(path_folder)
    if folder_name in folder_list:
        DownloadVideo(yt, path)
    else:
        os.makedirs(path)
        DownloadVideo(yt, path)

try:
    YouTubeVideo(link, path_folder, folder_name)
except:
    print("=> Something went wrong, Try again later")

