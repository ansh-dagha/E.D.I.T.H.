from utilities.speech_functions import * 

def confirm():
    speak("Are you sure")
    confirmation = listen()
    if confirmation in ["yes", 'yep', 'ya', "yup", "do it", "send it", "proceed"]:
        return True
    elif confirmation in ["No","abort","cancel"]:
        speak("Task Aborted")
    else:
        speak("I could not recognize what you just said")
    return False