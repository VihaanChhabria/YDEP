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
        st = playlist.videos[video].streams.get_highest_resolution()
        
        name = r"FullVideo{}.mp4".format(video)
        st.download(DOWNLOAD_PATH, name)

        downloaded_videos.append(DOWNLOAD_PATH + name)

        #sleep(7)

        downloaded_videos_titles.append(playlist.videos[video].title)


def Download_Video():
    __init()
        
    videoNumber = AMOUNT_VIDEO

    playlist = Playlist(PLAYLIST_LINK)

    video = 0

    while video < videoNumber:
        try:
            Get_Video(playlist, video)
        except:
            continue
        video = video + 1

def Get_Downloaded_Videos():
    return downloaded_videos

def Get_Downloaded_Videos_Titles():
    return downloaded_videos_titles

