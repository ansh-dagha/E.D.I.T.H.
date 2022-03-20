import webbrowser
import requests
from utilities.speech_functions import * 
from bs4 import BeautifulSoup
from urllib.request import urlopen
from googlesearch import search

def search_for(param):

    for j in search(param, tld="com", num=1, stop=1, pause=2):
        print(j)
        weburl = j

    soupti = BeautifulSoup(urlopen(weburl),features="html.parser")
    queryurl = "https://www.google.com/search?q="+param
    page = requests.get(queryurl).text
    soup = BeautifulSoup(page, "html.parser").select(".s3v9rd.AP7Wnd")
    ans = soup[0].getText(strip=True)
    if len(ans) > 100:
        text = ans.partition('.')[0] + '.'
    
    # Displaying the title
    title = soupti.title.get_text().split('-')[1]
    result = "According to"+title+" : "+text
    speak(result)
    speak('Do you want to open the site? ')
    # ch = input('Do you want to open the site?(y/n)')
    while True:
        stat = listen()
        if stat == None:
            continue
        if 'yes' in stat:
            webbrowser.open_new_tab(j)
        if 'no' in stat:
            return