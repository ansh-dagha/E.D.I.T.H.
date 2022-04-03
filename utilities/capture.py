import pyautogui
import os
from utilities.speech_functions import * 

def snapshot():
    if not os.path.exists('captures'):
        os.makedirs('captures')
        filename = 'capture'
    else:
        path, dirs, files = next(os.walk("./captures"))
        file_count = len(files)
        filename='capture'+ str(file_count + 1)

    speak('Screenshot saved')

    screenshot = pyautogui.screenshot()
    screenshot.save(r'captures/'+ filename +'.png')