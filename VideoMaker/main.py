from DownloadClip.DownloadClip import (Download_Video, 
                                       Get_Downloaded_Videos, 
                                       Get_Downloaded_Videos_Titles)
from EditYoutubeClip.CombineClipTest import (EditClip, 
                                             Get_Cut_Clips)
from SeleniumUpload.Youtube_Upload import Upload_Video
from threading import Thread

from time import sleep
import os

listvideoThread = []

downloaded_clips = os.path.abspath("VideoMaker\DownloadClip\Downloaded")
cut_clips = os.path.abspath("VideoMaker\EditYoutubeClip\OutputClips")

def DeleteFilesInPath(dir):
    for file in os.scandir(dir):
        os.remove(file.path)

def main():
    DeleteFilesInPath(cut_clips)
    DeleteFilesInPath(downloaded_clips)

    sleep(5)

    Download_Video()

    downloaded_videos_list = Get_Downloaded_Videos()
    downloaded_videos_count = len(downloaded_videos_list)

    for downloaded_video in range(downloaded_videos_count):
        listvideoThread.append(Thread(target = EditClip, args = (downloaded_videos_list[downloaded_video], downloaded_video)))
        listvideoThread[downloaded_video].start()

    for downloaded_video in range(downloaded_videos_count):
        listvideoThread[downloaded_video].join()

    cut_clips_list = Get_Cut_Clips()
    downloaded_clips_titles = Get_Downloaded_Videos_Titles()

    for title_number in range(len(downloaded_clips_titles)):
        for cut_clip_info in cut_clips_list:
            if cut_clip_info[0] == title_number:
                Upload_Video(cut_clip_info[1], f"{downloaded_clips_titles[cut_clip_info[0]]} - Part {cut_clip_info[2]+1}")

    #for cut_clip_info in range(len(cut_clips_list)):
    #    Upload_Video(cut_clips_list[cut_clip_info][1], f"{Get_Downloaded_Videos_Titles()[cut_clip_info][0]} - Part {cut_clip_info[1]}")

    print("done")

    sleep(20)

    try:
        DeleteFilesInPath(cut_clips)
        DeleteFilesInPath(downloaded_clips)
    except:
        DeleteFilesInPath(cut_clips)
        DeleteFilesInPath(downloaded_clips)

if __name__ == "__main__":
    main()

