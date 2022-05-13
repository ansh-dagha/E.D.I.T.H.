from utilities.websearch import checkconn
from utilities.speech_functions import *
import billboard

def songs():
    if checkconn(): 
        chart=billboard.ChartData('hot-100')
        print('The top 10 songs at the moment are:')
        for i in range(10):
            song=chart[i]
            print(song.title,'- ',song.artist)