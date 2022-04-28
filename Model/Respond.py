
from operator import le
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
import random
import datetime
# from googlesearch import *
import webbrowser
import requests
from utilities.speech_functions import *
from utilities.websearch import search_for,youtube,checkconn
from utilities.email_ import *
from utilities.powerOptions import *
from utilities.confirm import *
# from utilities.capture import *
import billboard
import time
import settings as settings
from pygame import mixer

from keras.models import load_model
model = load_model('Model/chatbot_model.h5')
import json
import random
intents = json.loads(open('Model/intents.json').read())
words = pickle.load(open('Model/words.pkl','rb'))
classes = pickle.load(open('Model/classes.pkl','rb'))


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(return_list, intents_json):
    list_of_intents= intents_json['intents']    
    for i in list_of_intents:
        if tag==i['tag']:
            result = random.choice(i['responses'])
    speak(result)
    print(result)
    if len(return_list) == 0:
        tag = 'noanswer'
    else:
        tag = return_list[0]['intent']
    
    if tag=='datetime':        
        strTime = datetime.datetime.now().strftime("%I:%M:%p")
        print(f"It\'s {strTime} right now")
        speak(f"It\'s {strTime} right now")

    if tag=='email':
        if checkconn():
            sendEmail()

    if tag == 'youtube':
        if checkconn():
            print("What should I play?")
            param = listen()
            youtube(param)

    if tag=='google':
        if checkconn():
            print("What should I search for?")
            speak("What should I search for?")
            statement = listen()
            param = statement.replace("search", "")
            search_for(param)
    
    if tag=='weather':
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

    if tag == 'news':
        main_url = " http://newsapi.org/v2/top-headlines?country=in&apiKey=bc88c2e1ddd440d1be2cb0788d027ae2"
        open_news_page = requests.get(main_url).json()
        article = open_news_page["articles"]
        results = [] 
          
        for ar in article: 
            results.append([ar["title"],ar["url"]]) 
          
        for i in range(10): 
            print(i + 1, results[i][0])
            print(results[i][1],'\n')
    
    if tag=='song':
        chart=billboard.ChartData('hot-100')
        print('The top 10 songs at the moment are:')
        for i in range(10):
            song=chart[i]
            print(song.title,'- ',song.artist)
    
    if tag=='timer':        
        mixer.init()
        speak('Minutes to timer..')
        x=listen()
        # x=input('Minutes to timer..')
        time.sleep(float(x)*60)
        mixer.music.load('Handbell-ringing-sound-effect.mp3')
        mixer.music.play()
    
    if tag=='remember':
        print(settings.profile)
        # learn(settings.profile)
        # word_update()

    
    # return result

def assis_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res


def word_update():
    words=[]
    classes = []
    documents = []
    ignore_words = ['?', '!']
    data_file = open('Model/intents.json').read()
    intents = json.loads(data_file)


    for intent in intents['intents']:
        for pattern in intent['patterns']:

            # take each word and tokenize it
            w = nltk.word_tokenize(pattern)
            words.extend(w)
            # adding documents
            documents.append((w, intent['tag']))

            # adding classes to our class list
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
    words = sorted(list(set(words)))

    classes = sorted(list(set(classes)))

    # print (len(documents), "documents")

    # print (len(classes), "classes", classes)

    # print (len(words), "unique lemmatized words", words)


    pickle.dump(words,open('Model/words.pkl','wb'))
    pickle.dump(classes,open('Model/classes.pkl','wb'))

def learn(profile):
    print('Help me Learn?')
    speak('Please tell me the general category of your question')
    # tag=input('Please enter general category of your question')
    tag=listen()
    speak('What sould I remember?')
    ms = listen()
    speak('What is your expected reply?')
    rep = listen()
    flag=-1
    for i in range(len(intents['intents'])):
        if tag.lower() in intents['intents'][i]['tag']:
            intents['intents'][i]['patterns'].append(ms)
            intents['intents'][i]['responses'].append(rep)        
            flag=1

    if flag==-1:
        
        intents['intents'].append (
            {'tag':tag,
            'patterns': [ms],
            'responses': [rep]})
        
    filename="Model/"+profile+"intents.json"
    with open(filename,'w') as outfile:
        outfile.write(json.dumps(intents,indent=4))
