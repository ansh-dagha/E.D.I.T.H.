import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen interactively
def listen():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print('\nListening...')
            r.adjust_for_ambient_noise(source, duration = 0.2)
            audio = r.listen(source)
            
            try:
                query = r.recognize_google(audio, language = 'en-in')
                print("\nThis is what I heard:", query)
                return query.lower()
            except Exception:
                speak('Sorry... I didn\'t get you')

# Listen pasively
def listen_in_background():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 0.2)
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language = 'en-in')
            return query.lower()
        except Exception:
            return ''