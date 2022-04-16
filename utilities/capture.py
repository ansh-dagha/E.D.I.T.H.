import pyautogui
import sys
import os
from cv2 import VideoCapture, imwrite
from utilities.speech_functions import * 

screenshot_folder = 'captures\\screenshots\\'
camera_folder     = 'captures\\camera\\'
cam = VideoCapture(0)

if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)
if not os.path.exists(camera_folder):
    os.makedirs(camera_folder)

def snapshot():
    path, dirs, files = next(os.walk(screenshot_folder))
    file_count = len(files)

    filename='screenshot'+ str(file_count + 1)
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_folder + filename +'.jpg')

    speak('Screenshot saved')

def camera():

    path, dirs, files = next(os.walk(camera_folder))
    file_count = len(files)

    filename='capture'+ str(file_count + 1)
    speak("Capturing Image in 3")
    speak("2")
    speak("1")
    result, image = cam.read()
    if result:
        imwrite(camera_folder+filename+".jpg",image)
        print(camera_folder+filename+".jpg")
        speak('Image saved')
    else:
        speak("Unable to access camera at the moment")