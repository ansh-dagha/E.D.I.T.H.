from capture import snapshot
from Email import sendEmail
from listen import listen
from processConfirmation import confirm
import powerOptions

if __name__ == "__main__":
    while(True):  # run infinite loop
        query = listen().lower()
        if 'email' in query:
            sendEmail()
        elif 'snapshot' in query:
            snapshot()
        elif 'log off' in query:
            if confirm():
                powerOptions.execute("shutdown /l")
        elif 'shutdown' in query:
            if confirm():
                powerOptions.execute("shutdown /s")
        elif 'shutdown' in query:
            if confirm():
                powerOptions.execute("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


# Take a snapshot
# Log Off
# ShutDown
# 
# Email
# email id
# body
# confirmation