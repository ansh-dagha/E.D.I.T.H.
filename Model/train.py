# nltk.download('all')

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import nltk
from nltk.stem import WordNetLemmatizer

import random
import json
import pickle
import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout

import tensorflow as tf
from tensorflow.keras.optimizers import SGD

words=[]
classes = []
documents = []
ignore_words = ['?', '!']
data_file = open('Model/intents.json').read()
intents = json.loads(data_file)

for intent in intents['intents']:
    for pattern in intent['patterns']:

        # Take each word and tokenize it
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        
        # Adding documents
        documents.append((w, intent['tag']))

        # Adding classes to our class list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

lemmatizer = WordNetLemmatizer()

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

pickle.dump(words,open('Model/words.pkl','wb'))
pickle.dump(classes,open('Model/classes.pkl','wb'))

# Initializing training data
training = []
output_empty = [0] * len(classes)

for doc in documents:
    
    bag = [] # initializing bag of words
    
    pattern_words = doc[0] # list of tokenized words for the pattern
    
    # Lemmatize each word - create base word, in attempt to represent related words
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    
    # Create our bag of words array with 1, if word match found in current pattern
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag (for each pattern)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# Shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training, dtype=object)

# Create train and test lists. X - patterns, Y - intents
train_x = list(training[:,0])
train_y = list(training[:,1])


# Create model - 3 layers:
# 1st layer - 128 neurons, 
# 2nd layer - 64 neurons,
# 3rd output layer - contains number of neurons equal to number of intents to predict output intent with softmax

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile model. 
# Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Fitting and saving the model
model_ = model.fit(np.array(train_x), np.array(train_y), epochs=40, batch_size=5, verbose=0)
model.save('Model/chatbot_model.h5', model_)