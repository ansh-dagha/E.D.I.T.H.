import os, sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QAction
import UI.image_rc
import UI.userdetails as usr

sys.path.append(os.path.join(os.path.dirname(sys.path[0]),''))
from database.db_functions import *
import hashlib
import re
import shutil
import settings
from utilities.modelfile import create_intents

app = QApplication(sys.argv)

# python -m PyQt5.pyrcc_main image.qrc -o image_rc.py

# if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

# if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class SignupScreen(QDialog):
    def __init__(self):
        super(SignupScreen, self).__init__()
        signup_ui_path = os.path.join(os.path.dirname(sys.path[0]),'AI-Assistant\\ui\\signup.ui')
        loadUi(signup_ui_path, self)

        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, True)
        # self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)

        self.signupButton.clicked.connect(self.signupfunction)
        self.loginButton.clicked.connect(self.loginfunction)
        
        self.setTabOrder(self.inputUsername, self.inputEmail)
        self.setTabOrder(self.inputEmail, self.inputPassword)
        self.setTabOrder(self.inputPassword, self.inputConfirmPassword)
        self.setTabOrder(self.inputConfirmPassword, self.signupButton)

        finish = QAction("Quit", self)
        finish.triggered.connect(self.closeEvent)

    def signupfunction(self):
        username = self.inputUsername.text()
        email = self.inputEmail.text()
        password = self.inputPassword.text()
        confirm_password = self.inputConfirmPassword.text()
        
        # Invalid cases
        if len(username) == 0 or len(password) == 0 or len(email) == 0 or len(confirm_password) == 0:
            self.errorLabel.setText("Please input all fields.")

        elif userExists(username):
            self.errorLabel.setText(f"Username '{username}' already exists.")
            self.inputUsername.clear()

        elif not bool(re.match("^[a-zA-Z0-9-_\.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$",email)):
            self.errorLabel.setText("Enter a valid email.")
            self.inputEmail.clear()

        elif password != confirm_password:
            self.errorLabel.setText("Passwords do not match.")
            self.inputPassword.clear()
            self.inputConfirmPassword.clear()

        else:
            settings.username = username
            settings.addressee = getUserDetails(username)[2]
            create_intents(settings.username)
            password_hash = hashlib.sha3_512(password.encode()).hexdigest()
            addDetails(username, email, password_hash)
            self.details = usr.UserDetails(username=username)
            self.close()
            settings.signUpFlag = False
            settings.exitFlag = False
            self.details.exec_()
            self.createDefaultProfilePic()

    def loginfunction(self):
        self.close()
        settings.signUpFlag = False
        settings.exitFlag = False
    
    def createDefaultProfilePic(self):
        try:
            src = str(os.path.join(os.path.dirname(sys.path[0]),f'AI-Assistant\\ui\\images\\defaultProfilePic.png'))
            dst = str(os.path.join(os.path.dirname(sys.path[0]),f'AI-Assistant\\ui\\images\\{settings.username}.png'))
            shutil.copy2(src, dst)

        except Exception as e:
            print(e)


    def closeEvent(self, event):
        settings.signUpFlag = False
        settings.exitFlag = True