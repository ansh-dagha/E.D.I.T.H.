import os
from utilities.speech_functions import * 

def execute(command):
    try:
        os.system(command)
    except:
        speak("Cannot execute the command")