import subprocess
import sys

libraries = ['configparser', 'getpass4', 'wget', 'selenium', 'pywin32', 'moviepy', 'yt-dlp']

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
if (input("Download Libraries? (y/n) ") == "y"):
    for library in libraries:
        install(library)


from configparser import ConfigParser
from getpass4 import getpass
import os
from wget import download

def save_file(path, config):
    with open(path, 'w') as configfile:
        config.write(configfile)

Download_Config_Path = r"VideoMaker\DownloadClip\DownloadConfig.ini"
Download_Config_Elements = [["AMOUNT_VIDEO"]]
Upload_Config_Path = r"VideoMaker\SeleniumUpload\UploadConfig.ini"
Upload_Config_Elements = [["DESCRIPTION"], ["VIEW"], ["USERNAME"], ["PASSWORD"]]

Edit_Clip_Config_Path = r"VideoMaker\EditYoutubeClip\EditClipConfig.ini"

Config_Paths = [Download_Config_Path, Upload_Config_Path]

Config_Elements = []
Config_Elements.append(Download_Config_Elements)
Config_Elements.append(Upload_Config_Elements)

Config_Files = []

Download_Config = ConfigParser()
Download_Config.read(Download_Config_Path)
Config_Files.append(Download_Config)

Upload_Config = ConfigParser()
Upload_Config.read(Upload_Config_Path)
Config_Files.append(Upload_Config)

Edit_Clip_Config = ConfigParser()
Edit_Clip_Config.read(Edit_Clip_Config_Path)

if not (Edit_Clip_Config.getboolean("PATHS", "CLIP_BACK_DOWNLOADED")):
    print("Downloading Background Video...")
    
    download('https://www.googleapis.com/drive/v3/files/1-itLfmBfVW18XaIj0h5GWc5X-n478h9k?alt=media&key=AIzaSyAA9ERw-9LZVEohRYtCWka_TQc6oXmvcVU&supportsAllDrives=True')
    os.rename(os.path.abspath("1-itLfmBfVW18XaIj0h5GWc5X-n478h9k"), "VideoMaker\EditYoutubeClip\BackgroundVideo.mp4")
    
    Edit_Clip_Config["PATHS"]["CLIP_BACK_DOWNLOADED"] = "True"
    save_file(Edit_Clip_Config_Path, Edit_Clip_Config)
    print("Done Downloading Background Video.")


for ConfigFileNumber in range(len(Config_Files)):
    for element in Config_Elements[ConfigFileNumber]:
        element.append(Config_Files[ConfigFileNumber]["USER CHANGEABLE"][element[0]])
        print(f"\n{element[1]}")
        edit_confirmation = str(input(f"{element[0]} above. Edit {element[0]}? (y/n) "))
        if edit_confirmation.lower() == "y":
            if element[0] == "PASSWORD":
                print("in")
                edit_change = getpass(f"What would you like {element[0]} to be changed to? (GetPass) " )
            else:
                edit_change = input(f"What would you like {element[0]} to be changed to? ")
            print("Saving...")

            element[1] = edit_change
            Config_Files[ConfigFileNumber]["USER CHANGEABLE"][element[0]] = element[1]
            
            print("Done.")

print("\nFinal Edits:")
for ConfigFileNumber in range(len(Config_Files)):
    save_file(Config_Paths[ConfigFileNumber], Config_Files[ConfigFileNumber])
    for element in Config_Elements[ConfigFileNumber]:
        print(f"{element[0]} = {element[1]}")

