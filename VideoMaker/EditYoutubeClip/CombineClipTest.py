from moviepy.editor import *
import math
from random import randint
import configparser

def __init():

    config = configparser.ConfigParser()
    config.read_file(open('VideoMaker\EditYoutubeClip\EditClipConfig.ini'))

    global DOWNLOAD_PATH
    DOWNLOAD_PATH = config.get('PATHS', 'DOWNLOAD_PATH')
    DOWNLOAD_PATH = r"{}".format(DOWNLOAD_PATH)

    global CLIP_BACK_PATH
    CLIP_BACK_PATH = config.get('PATHS', 'CLIP_BACK_PATH')

    global cut_clips
    cut_clips = []

def __BackgroundLengthSelector(BackClip, MainClip):
    BackClipDuration, MainClipDuration = int(BackClip.duration), int(MainClip.duration)
    BackClipDurationShort = BackClipDuration - (MainClipDuration + 20)
    StartSpot = randint(5, BackClipDurationShort)
    BackClipFinal = BackClip.subclip(StartSpot, StartSpot+MainClipDuration)
    return BackClipFinal

def EditClip(CLIP_MAIN_PATH, thread_number):

    __init()

    clipMain = VideoFileClip(CLIP_MAIN_PATH)
    clipBack = VideoFileClip(CLIP_BACK_PATH)

    clipMain = clipMain.subclip(2, math.floor(clipMain.duration))
    clipMain = clipMain.resize(.45)

    clipVideoDuration = math.floor(clipMain.duration)
    numberOfClips = math.ceil(clipVideoDuration/60)
    SingularClipDuration = clipVideoDuration/numberOfClips

    clipBack = __BackgroundLengthSelector(clipBack, clipMain)

    clipBack = clipBack.without_audio()


    print(clipVideoDuration)
    print(numberOfClips)
    print(SingularClipDuration)


    for clipsMade in range(numberOfClips):
        
        clipBack1 = clipBack.subclip(SingularClipDuration*(clipsMade), SingularClipDuration*(clipsMade+1))
        clipVideo1 = clipMain.subclip(SingularClipDuration*(clipsMade), SingularClipDuration*(clipsMade+1))

        final_clip = CompositeVideoClip([clipBack1.set_position((0,0)),clipVideo1.set_position((0,0))])

        clip_final_path = DOWNLOAD_PATH.format(thread_number, clipsMade)

        final_clip.write_videofile(clip_final_path)

        cut_clips.append([thread_number, clip_final_path, clipsMade])

def Get_Cut_Clips():
    cut_clips.sort()
    return cut_clips

