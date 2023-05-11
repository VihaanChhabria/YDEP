import subprocess
from pytube import Playlist
import configparser

def __init():
    config = configparser.ConfigParser()
    config.read_file(open('VideoMaker\DownloadClip\DownloadConfig.ini'))

    global PLAYLIST_LINK
    PLAYLIST_LINK = config.get('PATHS', 'PLAYLIST_LINK')

    global AMOUNT_VIDEO
    AMOUNT_VIDEO = int(config.get('USER CHANGEABLE', 'AMOUNT_VIDEO'))

    global DOWNLOAD_PATH
    DOWNLOAD_PATH = config.get('PATHS', 'DOWNLOAD_PATH')
    DOWNLOAD_PATH = r"{}".format(DOWNLOAD_PATH)

    global downloaded_videos
    downloaded_videos = []

    global downloaded_videos_titles
    downloaded_videos_titles = []

def Get_Video(playlist, video):
        
        separator = ' ['

        #yt-dlp https://www.youtube.com/watch?v=1PmJeP-TphM -P home:C:\Users\vihaa\YDEP\VideoMaker\DownloadClip\Downloaded\ -o "test video.%(ext)s"

        name = r"FullVideo{}".format(video)

        subprocess.run(f'yt-dlp {playlist[video]} -P home:{DOWNLOAD_PATH} -o "{name}.%(ext)s"')

        downloaded_videos.append(DOWNLOAD_PATH + name + ".mp4")

        downloaded_videos_titles.append((subprocess.getoutput(f'yt-dlp --print filename {playlist[video]}')).split(separator, 1)[0])


def Download_Video():
    __init()
        
    videoNumber = AMOUNT_VIDEO

    playlist = Playlist(PLAYLIST_LINK)

    video = 0
    tryed = 0

    while video < videoNumber:
        try:
            Get_Video(playlist, video)
        except:
            print(f"failed, tried {tryed} times, video {video}")
            tryed = tryed + 1
            continue
        video = video + 1

def Get_Downloaded_Videos():
    return downloaded_videos

def Get_Downloaded_Videos_Titles():
    return downloaded_videos_titles

