import datetime
import webbrowser
from utilities.websearch import search_for,youtube
from utilities.speech_functions import *
from utilities.email_ import *
from utilities.powerOptions import *
from utilities.confirm import *
from utilities.capture import *

gender = ['Female', 'Male']
addressee = ['Sir', 'Miss', 'Boss']

def greet(addressee):
    
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak(f'Good Morning {addressee}')
    elif hour >= 12 and hour < 18:
        speak(f'Good Afternoon {addressee}')
    else:
        speak(f'Good Evening {addressee}')

greet(addressee[2])


while True:
    
    statement = listen()
    if statement == None:
        continue

    if "hello friday" in statement or 'hey' in statement or 'hello' in statement:
        speak('Oh Hello sir')

    elif 'time' in statement:
        strTime = datetime.datetime.now().strftime("%I:%M:%p")
        speak(f"It\'s {strTime} right now")

    if 'email' in statement:
        sendEmail()
    
    if 'search' in statement:
        param = statement.replace("search", "")
        search_for(param)

    elif 'snapshot' in statement:
        snapshot()
    
    elif 'log off' in statement:
        if confirm():
            execute("shutdown /l")
    
    elif 'shutdown' in statement:
        if confirm():
            execute("shutdown /s")
    
    elif 'sleep' in statement:
        if confirm():
            execute("rundll32.exe powrprof.dll,SetSuspendState Sleep")

    elif 'open youtube' in statement:
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("Youtube is open now")
    elif 'play on youtube' in statement:
        param = statement.replace("play on youtube", "")
        youtube(param)