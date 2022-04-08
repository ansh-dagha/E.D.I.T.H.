import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
import image_rc

from database.db_functions import *
import hashlib
import re

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi('ui\login.ui',self)
        self.loginButton.clicked.connect(self.loginfunction)
        self.forgotPasswordButton.clicked.connect(self.forgotPassword)
        self.signupButton.clicked.connect(self.signupfunction)

        self.setTabOrder(self.inputUsername, self.inputPassword)
        self.setTabOrder(self.inputPassword, self.loginButton)
        self.setTabOrder(self.loginButton, self.forgotPasswordButton)

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
                print("Successfully logged In.")
            else:
                self.errorLabel.setText('Incorrect password! Please try again.')
                self.inputPassword.clear()
            
    def forgotPassword(self):
        print('forgot password')

    def signupfunction(self):
        print('signup')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	loginForm = LoginScreen()
	loginForm.show()
	sys.exit(app.exec_())