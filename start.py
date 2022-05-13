import sys
from PyQt5.QtWidgets import QApplication
from ui import login, signup

# app = QApplication(sys.argv)
login_ = login.LoginScreen()

signup_ = signup.SignupScreen()

username = ''

while not username:

    if not login_.exec():
        username, signupflag = login_.output()

    if signupflag:
        if not signup_.exec():
            username = signup_.output()

print(username)