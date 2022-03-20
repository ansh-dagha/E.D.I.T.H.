import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('\nListening...')
        r.adjust_for_ambient_noise(source, duration = 0.2)
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language = 'en-in')
            print(query)
            speak(query)

        except Exception:
            speak('Sorry... I didn\'t get you')
            return None
    return query.lower()