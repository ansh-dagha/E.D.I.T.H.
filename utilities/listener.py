import datetime
import settings
from Model.Respond import assis_response
from utilities.speech_functions import *
import asyncio

def greet(addressee):
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak(f'Good Morning {addressee}')
    elif hour >= 12 and hour < 18:
        speak(f'Good Afternoon {addressee}')
    else:
        speak(f'Good Evening {addressee}')

def start_service(homeObj, loop):
    asyncio.set_event_loop(loop)
    WAKE = "assistant"
    greet(settings.addressee)

    while settings.exitFlag == False:
        statement = listen_in_background()
        if statement.count(WAKE) > 0:
            stat = statement.replace(WAKE,'')
            res = assis_response(stat, settings.username)
            print("Response: ", res)
    print("Terminating Listener Service...")