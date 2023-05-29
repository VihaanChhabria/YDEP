from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import win32com.client
import configparser
import os

def __init():
    config = configparser.ConfigParser()
    config.read_file(open(r'VideoMaker\SeleniumUpload\UploadConfig.ini'))

    global VIEW
    VIEW = config.get('USER CHANGEABLE', 'VIEW')

    global USERNAME
    USERNAME = config.get('USER CHANGEABLE', 'USERNAME')
    global PASSWORD
    PASSWORD = config.get('USER CHANGEABLE', 'PASSWORD')

    global YOUTUBE_LOGIN_USERNAME_XPATH
    YOUTUBE_LOGIN_USERNAME_XPATH = config.get('PATHS', 'YOUTUBE_LOGIN_USERNAME_XPATH')
    global YOUTUBE_LOGIN_PASSWORD_XPATH
    YOUTUBE_LOGIN_PASSWORD_XPATH = config.get('PATHS', 'YOUTUBE_LOGIN_PASSWORD_XPATH')
    global YOUTUBE_LOGIN_NEXT_XPATH
    YOUTUBE_LOGIN_NEXT_XPATH = config.get('PATHS', 'YOUTUBE_LOGIN_NEXT_XPATH')

    global YOUTUBE_LOGIN_WEBSITE
    YOUTUBE_LOGIN_WEBSITE = config.get('PATHS', 'YOUTUBE_LOGIN_WEBSITE')
    global YOUTUBE_UPLOAD_WEBSITE
    YOUTUBE_UPLOAD_WEBSITE = config.get('PATHS', 'YOUTUBE_UPLOAD_WEBSITE')

    global SELECT_FILE_ID
    SELECT_FILE_ID = config.get('PATHS', 'SELECT_FILE_ID')
    global NEXT_BUTTON
    NEXT_BUTTON = config.get('PATHS', 'NEXT_BUTTON')

    global TITLE_XPATH
    TITLE_XPATH = config.get('PATHS', 'TITLE_XPATH')
    global DESCRIPTION_XPATH
    DESCRIPTION_XPATH = config.get('PATHS', 'DESCRIPTION_XPATH')
    global VIEW_XPATH
    VIEW_XPATH = config.get('PATHS', 'VIEW_XPATH').format(VIEW)

    global CHROMEDRIVER_PATH
    CHROMEDRIVER_PATH = config.get('PATHS', 'CHROMEDRIVER_PATH')

    global DESCRIPTION
    DESCRIPTION = config.get('USER CHANGEABLE', 'DESCRIPTION')

    global driver
    driver = webdriver.Chrome(CHROMEDRIVER_PATH)

def __ClickElement(byInput, valueInput):
    try:
        element = driver.find_element(by=byInput, value=valueInput)
        time.sleep(1)
        element.click()
    except:
        time.sleep(2)
        __FillElement(byInput, valueInput, valueInput)

def __FillElement(byInput, valueInput, keyInput):
    try:
        element = driver.find_element(by=byInput, value=valueInput)
        element.clear()
        time.sleep(1)
        element.send_keys(keyInput)
    except:
        time.sleep(2)
        __FillElement(byInput, valueInput, keyInput)

def __Login():
    
    driver.get(str(YOUTUBE_LOGIN_WEBSITE))

    time.sleep(3)

    __FillElement(By.XPATH, YOUTUBE_LOGIN_USERNAME_XPATH, USERNAME)

    __ClickElement(By.XPATH, YOUTUBE_LOGIN_NEXT_XPATH)

    __FillElement(By.XPATH, YOUTUBE_LOGIN_PASSWORD_XPATH, PASSWORD)

    __ClickElement(By.XPATH, YOUTUBE_LOGIN_NEXT_XPATH)

def __StartWeb(website):
    try:
        driver.get(website)
    except:
        time.sleep(3)
        __StartWeb(website)

def __FillVideoInfo(title):
    __FillElement(By.XPATH, TITLE_XPATH, title)
    __FillElement(By.XPATH, DESCRIPTION_XPATH, DESCRIPTION)

def __InputVideo(UPLOAD_VIDEO_PATH):
    try:
        shell = win32com.client.Dispatch("WScript.Shell")   
        shell.Sendkeys(UPLOAD_VIDEO_PATH)  
        shell.Sendkeys("~")
    except:
        time.sleep(3)
        __InputVideo()


def Upload_Video(UPLOAD_VIDEO_PATH, TITLE):
    print(UPLOAD_VIDEO_PATH)
    UPLOAD_VIDEO_PATH = os.path.abspath(UPLOAD_VIDEO_PATH)
    print(UPLOAD_VIDEO_PATH)

    __init()

    __Login()

    driver.get(YOUTUBE_UPLOAD_WEBSITE)

    time.sleep(10)

    __ClickElement(By.ID, SELECT_FILE_ID)

    time.sleep(3)

    __InputVideo(UPLOAD_VIDEO_PATH)

    time.sleep(10)

    __FillVideoInfo(TITLE)

    for button_pressed in range(3):
        print("in")
        time.sleep(0.5)
        __ClickElement(By.ID, NEXT_BUTTON)

    __ClickElement(By.XPATH, VIEW_XPATH)

    __ClickElement(By.ID, "done-button")

    time.sleep(5)

    driver.quit()
