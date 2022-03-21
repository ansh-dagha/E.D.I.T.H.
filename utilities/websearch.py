import webbrowser
from utilities.speech_functions import * 
import urllib
import requests
from requests_html import HTMLSession

def parse_results(response):    
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".IsZvec"
    
    results = response.html.find(css_identifier_result)
    # print(results)

    output = []
    
    for result in results:
        # print('in for')

        item = {
            'title': result.find(css_identifier_title, first=True).text,
            'link': result.find(css_identifier_link, first=True).attrs['href']             
        }
        try: 
            result.find(css_identifier_text, first=True).text
            item['text']=result.find(css_identifier_text, first=True).text
        except:
            item['text']=''
        
        output.append(item)
        
    return output

def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def get_results(query):
    
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)
    
    return response

def google_search(query):
    response = get_results(query)
    return parse_results(response)

def search_for(query):
    results = google_search(query)
    j=''
    # print(results)
    for a in results:
        desc= a['text']
        if not(desc==''):
            if len(desc) > 100:
                text = desc.partition('.')[0] + '.'
                result = "According to"+a['title'].split('-')[1]+" : "+text
                j=a['link']
                break;

    print(result)
    speak(result)
    speak('Do you want to open the site?')
    # ch = input('Do you want to open the site?(y/n)')
    while True:
        stat = listen()
        if stat == None:
            continue
        if 'yes' in stat:
            webbrowser.open_new_tab(j)
            return
        if 'no' in stat:
            return



