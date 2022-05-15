import importlib
import sys
import threading
from turtle import goto
from PyQt5.QtWidgets import QApplication
from UI import login, signup, ui_home
from utilities import notify
import settings

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

    # username = 'anshdagha'

    app = QApplication(sys.argv)
    home_ = ui_home.MainWindow()
    home_.show()
    print("Starting notification service")
    notification_thread = threading.Thread(target=notify.start_service, args=(settings.username,))
    notification_thread.start()
    app.exec_()
    notification_thread.join()
