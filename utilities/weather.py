from utilities.websearch import checkconn
from utilities.speech_functions import *
import requests

def weather():
    if checkconn():
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