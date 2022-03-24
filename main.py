import datetime
import webbrowser
import requests
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

    if "hello edith" in statement or 'hey' in statement or 'hello' in statement:
        speak('Oh Hello sir')

    elif 'time' in statement:
        strTime = datetime.datetime.now().strftime("%I:%M:%p")
        speak(f"It\'s {strTime} right now")

    elif 'email' in statement:
        sendEmail()
    
    elif 'search' in statement:
        param = statement.replace("search", "")
        search_for(param)

    elif 'snapshot' or 'capture' or 'snap' or 'snip' in statement:
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
        param = statement.replace("play on youtube ", "")
        youtube(param)

    elif "weather" in statement:
        api_key = "8ef61edcf1c576d65d836254e11ea420"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        speak("Which city sir?")
        city_name = listen()
        complete_url = base_url+"appid="+api_key+"&q="+city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            temperature = y["temp"] - 273.15
            temperature = round(temperature)
            humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"].capitalize()
            print(f'Temperature = {temperature} C \nHumidity = {humidity}% \nDescription: {weather_description}')
            speak(f'It\'s {temperature} degree celsius and {weather_description} \n Humidity is {humidity}%')

        else:
            speak("Sorry City Not Found!")

    # elif 'bye' or 'goodbye' in statement:
    #     speak('See you soon Sir!')
    #     break