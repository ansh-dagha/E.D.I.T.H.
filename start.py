import importlib, sys, threading
from PyQt5.QtWidgets import QApplication
from UI import login, signup, ui_home
from utilities import notify, listener
import settings

app = QApplication(sys.argv)

while settings.exitFlag == False:

    importlib.reload(settings)
    login_ = login.LoginScreen()
    signup_ = signup.SignupScreen()

    while (settings.username == '') and (settings.exitFlag == False):
        login_.exec_()
        if settings.signUpFlag:
            signup_.exec_()

    print('Exit Flag is set to',settings.exitFlag)

    if settings.username == '':
        sys.exit()

    print("SUCCESS! Welcome ",settings.username)

    home_ = ui_home.MainWindow()
    notification_thread = threading.Thread(target=notify.start_service, args=(settings.username,))
    listener_thread = threading.Thread(target=listener.start_service, args=(home_,))
    
    home_.show()

    print("Starting Notification Service")
    notification_thread.start()

    print("Starting Listener Service")
    listener_thread.start()

    app.exec_()

    notification_thread.join()
    listener_thread.join()