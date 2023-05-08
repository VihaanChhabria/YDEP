from configparser import ConfigParser
from getpass import getpass

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

def save_file(path, config):
    with open(path, 'w') as configfile:
        config.write(configfile)

colorama_init()

Download_Config_Path = r"VideoMaker\DownloadClip\DownloadConfig.ini"
Download_Config_Elements = [["AMOUNT_VIDEO"]]
Upload_Config_Path = r"VideoMaker\SeleniumUpload\UploadConfig.ini"
Upload_Config_Elements = [["DESCRIPTION"], ["VIEW"], ["USERNAME"], ["PASSWORD"]]

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


for ConfigFileNumber in range(len(Config_Files)):
    for element in Config_Elements[ConfigFileNumber]:
        element.append(Config_Files[ConfigFileNumber]["USER CHANGEABLE"][element[0]])
        print(f"\n{element[1]}")
        edit_confirmation = str(input(f"{element[0]} above. Edit {element[0]}? (y/n) "))
        if edit_confirmation.lower() == "y":
            if element[0] == "PASSWORD":
                print("in")
                edit_change = getpass(f"What would you like {element[0]} to be changed to?" )
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