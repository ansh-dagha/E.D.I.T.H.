import datetime
import webbrowser
from speech_functions import *
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from googlesearch import search

addressee = ['Sir', 'Miss', 'Boss']

def greet(addressee):
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak_(f'Good Morning {addressee}')
    elif hour >= 12 and hour < 18:
        speak_(f'Good Afternoon {addressee}')
    else:
        speak_(f'Good Evening {addressee}')

# greet(addressee[0])
def searches(param):
    # param = 'project'

    for j in search(param, tld="co.in", num=1, stop=1):
        weburl = j

    soupti = BeautifulSoup(urlopen(weburl),features="html.parser")
    queryurl = "https://www.google.com/search?q="+param
    page = requests.get(queryurl).text
    soup = BeautifulSoup(page, "html.parser").select(".s3v9rd.AP7Wnd")
    ans = soup[0].getText(strip=True)
    if len(ans) > 100:
        text = ans.partition('.')[0] + '.'
    # displaying the title
    title = soupti.title.get_text().split('-')[1]
    result = "According to"+title+" : "+text
    speak_(result)
    speak_('Do you want to open the site?')
    # ch = input('Do you want to open the site?(y/n)')
    while True:
        stat = listen_()
        if stat == None:
            continue
        if 'yes' in stat:
            webbrowser.open_new_tab(j)
        if 'no' in stat:
            return

while True:
    
    statement = listen_()
    if statement == None:
        continue

    if "hello friday" in statement or 'hey' in statement or 'hello' in statement:
        speak_('Oh Hello sir')

    if 'search' in statement:
        param = statement.replace("search", "")
        searches(param)
    

    # if "hello friday" in statement or "ok bye" in statement or "stop" in statement:
    #     speak('your personal assistant G-one is shutting down,Good bye')
    #     print('your personal assistant G-one is shutting down,Good bye')
    #     break

    # if 'wikipedia' in statement:
    #     speak('Searching Wikipedia...')
    #     statement = statement.replace("wikipedia", "")
    #     results = wikipedia.summary(statement, sentences=3)
    #     speak("According to Wikipedia")
    #     print(results)
    #     speak(results)

    # elif 'open youtube' in statement:
    #     webbrowser.open_new_tab("https://www.youtube.com")
    #     speak("youtube is open now")
    #     time.sleep(5)

    # elif 'open google' in statement:
    #     webbrowser.open_new_tab("https://www.google.com")
    #     speak("Google chrome is open now")
    #     time.sleep(5)

    # elif 'open gmail' in statement:
    #     webbrowser.open_new_tab("gmail.com")
    #     speak("Google Mail open now")
    #     time.sleep(5)

    # elif "weather" in statement:
    #     api_key = "8ef61edcf1c576d65d836254e11ea420"
    #     base_url = "https://api.openweathermap.org/data/2.5/weather?"
    #     speak("whats the city name")
    #     city_name = takeCommand()
    #     complete_url = base_url+"appid="+api_key+"&q="+city_name
    #     response = requests.get(complete_url)
    #     x = response.json()
    #     if x["cod"] != "404":
    #         y = x["main"]
    #         current_temperature = y["temp"]
    #         current_humidiy = y["humidity"]
    #         z = x["weather"]
    #         weather_description = z[0]["description"]
    #         speak(" Temperature in kelvin unit is " +
    #               str(current_temperature) +
    #               "\n humidity in percentage is " +
    #               str(current_humidiy) +
    #               "\n description  " +
    #               str(weather_description))
    #         print(" Temperature in kelvin unit = " +
    #               str(current_temperature) +
    #               "\n humidity (in percentage) = " +
    #               str(current_humidiy) +
    #               "\n description = " +
    #               str(weather_description))

    #     else:
    #         speak(" City Not Found ")

    # elif 'time' in statement:
    #     strTime = datetime.datetime.now().strftime("%H:%M:%S")
    #     speak(f"the time is {strTime}")

    # elif 'who are you' in statement or 'what can you do' in statement:
    #     speak('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'
    #           'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
    #           'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

    # elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
    #     speak("I was built by Mirthula")
    #     print("I was built by Mirthula")

    # elif "open stackoverflow" in statement:
    #     webbrowser.open_new_tab("https://stackoverflow.com/login")
    #     speak("Here is stackoverflow")

    # elif 'news' in statement:
    #     news = webbrowser.open_new_tab(
    #         "https://timesofindia.indiatimes.com/home/headlines")
    #     speak('Here are some headlines from the Times of India,Happy reading')
    #     time.sleep(6)

    # elif 'search' in statement:
    #     statement = statement.replace("search", "")
    #     webbrowser.open_new_tab(statement)
    #     time.sleep(5)

    # elif "log off" in statement or "sign out" in statement:
    #     speak(
    #         "Ok , your pc will log off in 10 sec make sure you exit from all applications")
    #     subprocess.call(["shutdown", "/l"])
