import subprocess
import configparser

def __init(config):

    global PLAYLIST_LINK
    PLAYLIST_LINK = config.get('PATHS', 'PLAYLIST_LINK')

    global AMOUNT_VIDEO
    AMOUNT_VIDEO = int(config.get('USER CHANGEABLE', 'AMOUNT_VIDEO'))

    global ROUND
    ROUND = int(config.get('USER CHANGEABLE', 'ROUND'))

    global DOWNLOAD_PATH
    DOWNLOAD_PATH = config.get('PATHS', 'DOWNLOAD_PATH')

    global PLAYLISTURL_FILE
    PLAYLISTURL_FILE = config.get('PATHS', 'PLAYLISTURL_PATH')

    global downloaded_videos
    downloaded_videos = []

    global downloaded_videos_titles
    downloaded_videos_titles = []

    subprocess.run(f'yt-dlp --flat-playlist -i --print-to-file url {PLAYLISTURL_FILE} "{PLAYLIST_LINK}"')
    global playlist
    playlist = open(PLAYLISTURL_FILE).readlines()
    f = open(PLAYLISTURL_FILE, 'w').close()

def Get_Video(playlist, video):
        
        separator = ' ['

        #yt-dlp https://www.youtube.com/watch?v=1PmJeP-TphM -P home:C:\Users\vihaa\YDEP\VideoMaker\DownloadClip\Downloaded\ -o "test video.%(ext)s"

        name = r"FullVideo{}".format(video)

        subprocess.run(f'yt-dlp {playlist[video]} -P home:{DOWNLOAD_PATH} -o "{name}.%(ext)s"')

        downloaded_videos.append(DOWNLOAD_PATH + name + ".mp4")

        downloaded_videos_titles.append((subprocess.getoutput(f'yt-dlp --print filename {playlist[video]}')).split(separator, 1)[0])


def Download_Video():

    config = configparser.ConfigParser()
    config.read_file(open('VideoMaker\DownloadClip\DownloadConfig.ini'))
    
    __init(config)

    video = 0 + (AMOUNT_VIDEO*ROUND)
    tryed = 0

    while video < AMOUNT_VIDEO + (AMOUNT_VIDEO*ROUND):
        try:
            Get_Video(playlist, video)
        except:
            print(f"failed, tried {tryed} times, video {video}")
            tryed = tryed + 1
            continue
        video = video + 1



    config['USER CHANGEABLE']['ROUND'] = str(ROUND+1)

    with open('VideoMaker\DownloadClip\DownloadConfig.ini', 'w') as configfile:
        config.write(configfile)

def Get_Downloaded_Videos():
    return downloaded_videos

def Get_Downloaded_Videos_Titles():
    return downloaded_videos_titles

#Download_Video()