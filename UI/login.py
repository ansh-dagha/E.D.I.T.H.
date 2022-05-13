import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QAction
from PyQt5.QtGui import QPixmap
import ui.image_rc

settings_dir = sys.path.append(os.path.join(os.path.dirname(sys.path[0]),''))
settings_dir = sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'database'))
from database.db_functions import *
import hashlib
import re
import settings

app = QApplication(sys.argv)

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        login_ui_path = os.path.join(os.path.dirname(sys.path[0]),'AI-Assistant\\ui\\login.ui')
        loadUi(login_ui_path, self)

        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, True)

        self.username = ''
        self.signupflag = False

        self.loginButton.clicked.connect(self.loginfunction)
        self.forgotPasswordButton.clicked.connect(self.forgotPassword)
        self.signupButton.clicked.connect(self.signupfunction)

        # Tab order
        self.setTabOrder(self.inputUsername, self.inputPassword)
        self.setTabOrder(self.inputPassword, self.loginButton)
        self.setTabOrder(self.loginButton, self.forgotPasswordButton)

        finish = QAction("Quit", self)
        finish.triggered.connect(self.closeEvent)

    def loginfunction(self):
        username = self.inputUsername.text()
        password = self.inputPassword.text()

        if len(username) == 0 or len(password) == 0:
            self.errorLabel.setText("Please input all fields.")

        elif not userExists(username):
            self.errorLabel.setText("Username doesn't exists! Kindly signup.")
            self.inputUsername.clear()
            self.inputPassword.clear()

        else:
            password_hash = hashlib.sha3_512(password.encode()).hexdigest()
            
            if checkPassword(username, password_hash):
                settings.init(username)
                print(settings.profile)
                print("Successfully logged In.")
                self.username = username
                self.signupflag = False
                self.close()
                
            else:
                self.errorLabel.setText('Incorrect password! Please try again.')
                self.inputPassword.clear()
            
    def forgotPassword(self):
        print('forgot password')

    def signupfunction(self):
        self.close()
        self.signupflag = True
    
    def output(self):
        return self.username, self.signupflag

    def closeEvent(self, event):
        self.signupflag = False
        self.username = '_'

    # def start():
    #     app = QApplication(sys.argv)
    #     login_ = login.LoginScreen()
    #     login_.show()
    #     sys.exit(app.exec_())


# if __name__ == '__main__':
#     loginForm = LoginScreen()
#     loginForm.show()
#     sys.exit(app.exec_())