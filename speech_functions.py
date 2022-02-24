import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak_(text):
    engine.say(text)
    engine.runAndWait()


def listen_():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('\nListening...')
        r.adjust_for_ambient_noise(source, duration = 0.5)
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio)
            print(query)
            # speak_(query)

        except Exception:
            speak_('Sorry... I didn\'t get you')
            return None
    return query.lower()