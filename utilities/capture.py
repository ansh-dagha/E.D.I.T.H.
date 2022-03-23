import pyautogui
import os
from utilities.speech_functions import * 

def snapshot():
    if not os.path.exists('images'):
        os.makedirs('captures')
        filename = 'capture'
    else:
        path, dirs, files = next(os.walk("./images"))
        file_count = len(files)
        filename='capture'+ str(file_count + 1)

    speak('Screenshot saved')

    screenshot = pyautogui.screenshot()
    screenshot.save(r'images/'+ filename +'.png')