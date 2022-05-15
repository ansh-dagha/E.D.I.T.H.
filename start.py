import sys
from PyQt5.QtWidgets import QApplication
from UI import login, signup, ui_home
import settings

login_ = login.LoginScreen()
signup_ = signup.SignupScreen()

while (settings.username == '') and (settings.exitFlag == False):

    login_.exec_()
    if settings.signUpFlag:
        signup_.exec_()

if settings.username == '':
    sys.exit()

print("SUCCESS! Welcome ",settings.username)

# username = 'anshdagha'

app = QApplication(sys.argv)
home_ = ui_home.MainWindow()
home_.show()
sys.exit(app.exec_())