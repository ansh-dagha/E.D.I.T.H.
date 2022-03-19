from utilities.speech_functions import * 
import smtplib

contacts = {
    'ansh':"anshdagha@gmail.com",
    'mihir':"mihir.rh.19@gmail.com",
}

def SEND_EMAIL(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587) # create a SMTP object for connection with server
    server.ehlo()
    server.starttls() #TLS connection required by gmail
    server.login('testassisstant@gmail.com','maggi')
    server.sendmail('testassisstant@gmail.com',to,content) # from, to, content

def sendEmail():
    try:
        print("\nTo whom should I send an email?")
        speak("To whom should I send an email?")
        to = listen()
        to = contacts[to] or to.replace(" ", "").replace("dot",".").replace("at","@")
        print("\nTo:",to)
        speak("what should i say")
        content = listen()
        if content == "abort":
            speak("Task Aborted")
            return
        print("\nText:",content)
        # to = dict[name]
        print("\nEmail is ready to be sent. Do you want me to proceed?")
        speak("Email is ready to be sent. Do you want me to proceed?")
        while True:
            confirmation = listen()
            if confirmation in ["Yes", "do it", "send it","proceed"]:
                SEND_EMAIL(to,content)
                speak("Email has been sent")
                print("Email has been sent")
                break
            elif confirmation in ["No","abort","cancel"]:
                speak("Task Aborted")
                break
            else:
                speak("I could not recognize what you just said")

    except Exception as e:
        print(e)
        speak("Sorry Unable to send the email at the moment Try again")