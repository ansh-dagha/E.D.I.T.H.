from utilities.speech_functions import * 

def confirm(speech="Are you sure", abort_txt="Okay task aborted"):
    speak(speech)
    while True:
        confirmation = listen()
        if confirmation in ["yes", 'yep', 'ya', "yup", "do it", "send it", "proceed"]:
            return True
        elif confirmation in ["no","abort","cancel","nope"]:
            speak(abort_txt)
            return False
        else:
            speak("I could not recognize what you just said")