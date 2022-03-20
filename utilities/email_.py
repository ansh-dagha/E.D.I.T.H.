from utilities.speech_functions import * 
from utilities.confirm import *
import smtplib

contacts = {
    'ansh':"anshdagha@gmail.com",
    'mihir':"mihir.rh.19@gmail.com",
}

def SEND_EMAIL(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587) # create a SMTP object for connection with server
    server.ehlo()
    server.starttls() #TLS connection required by gmail
    server.login('testassisstant@gmail.com','maggi000')
    server.sendmail('testassisstant@gmail.com',to,content) # from, to, content

def sendEmail():
    try:
        speak("To whom should I send an email?")
        print("\nTo whom should I send an email?",end='')
        to = listen()
        to = contacts[to] or to.replace(" ", "").replace("dot",".").replace("at","@")
        print("\nTo:",to)
        speak("What should i email?")
        print("\nWhat should i email?")
        content = listen()
        print("\nText:",content)
        speak("Email is ready to be sent.")
        print("\nEmail is ready to be sent.")
        if confirm("Do you want me to proceed?", abort_txt="Okay. Email Discarded."):
            SEND_EMAIL(to,content)
            speak("Email has been sent")
            print("Email has been sent")
        
    except Exception as e:
        print(e)
        speak("Sorry Unable to send the email at the moment Try again later")