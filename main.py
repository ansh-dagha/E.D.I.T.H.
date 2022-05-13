import datetime
from utilities.speech_functions import *
from utilities.email_ import *
from utilities.powerOptions import *
from utilities.confirm import *
# from utilities.capture import *
from Model.Respond import assis_response
from UI import login 

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


# login_ = login.LoginScreen()
# login_.show()
# login.logs()
# login_.close()
WAKE = "hello"
greet(addressee[2])
while True:
    # print('hello')
    statement = listen()
    if statement.count(WAKE) > 0:
        stat = statement.replace('hello','')
        assis_response(statement)
        # res = assis_response(statement)
        # print(res)
        # speak(res)
    