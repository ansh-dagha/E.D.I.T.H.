
from operator import le
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
import random
import datetime
import webbrowser
import requests
from utilities.speech_functions import *
from utilities.websearch import search_for,youtube,checkconn
from utilities.email_ import *
from utilities.powerOptions import *
from utilities.confirm import *
from utilities.conversational_util import *
from utilities.weather import *
from utilities.news import *
from utilities.songs import *
# from utilities.capture import *
import billboard
import time
import settings as settings

from keras.models import load_model
model = load_model('Model/chatbot_model.h5')
import json
import random
intents = json.loads(open('Model/intents.json').read())
words = pickle.load(open('Model/words.pkl','rb'))
classes = pickle.load(open('Model/classes.pkl','rb'))
history = False


act_dict={'datetime':date(),
'google':search_for(),
'youtube':youtube(),
'email':sendEmail(),
'chat':chatting(),
'remember':learn(),
'song':songs(),
'news':news(),
'weather':weather()
}

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
    if len(return_list) == 0:
        tag = 'noanswer'
    else:
        tag = return_list[0]['intent']

    list_of_intents= intents_json['intents']    
    for i in list_of_intents:
        if tag==i['tag']:
            result = random.choice(i['responses'])
    speak(result)
    print(result)

    if tag in act_dict.keys():
        act_dict[tag]

    # if tag=='datetime':        
    #     date()

    # if tag=='email':
    #     if checkconn():
    #         sendEmail()

    # if tag == 'youtube':
    #     youtube()

    # if tag=='google':
    #     search_for()
    
    # if tag=='weather':
    #     weather()        

    # if tag == 'news':
    #     news()
    
    # if tag=='song':
    #     songs()
    
    # if tag=='remember':
    #     print(settings.profile)
    #     # learn(settings.profile)

    # if tag=='chat':
        

def assis_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res


def learn(profile):
    print('Help me Learn?')
    speak('Please tell me the general category of your question')
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


def chatting():
    while True:
            statement=listen()
            if not history:
                output, chat_history = converse(statement)
                history = True
                print(output)
                speak(output)
                continue
            
            output, chat_history = converse(statement, chat_history)
            print(output)
            speak(output)
            if statement in ['Stop','Bye','End','Quit']:
                break

def date():
    strTime = datetime.datetime.now().strftime("%I:%M:%p")
    print(f"It\'s {strTime} right now")
    speak(f"It\'s {strTime} right now")