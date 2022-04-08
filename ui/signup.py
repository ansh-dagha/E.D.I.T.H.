import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
import image_rc
import login

sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'database'))
from db_functions import *
import hashlib
import re

# python -m PyQt5.pyrcc_main image.qrc -o image_rc.py

class SignupScreen(QDialog):
    def __init__(self):
        super(SignupScreen, self).__init__()
        signup_ui_path = os.path.join(os.path.dirname(sys.path[0]),'ui\\signup.ui')
        loadUi(signup_ui_path, self)
        self.signupButton.clicked.connect(self.signupfunction)
        self.loginButton.clicked.connect(self.loginfunction)

        self.setTabOrder(self.inputUsername, self.inputEmail)
        self.setTabOrder(self.inputEmail, self.inputPassword)
        self.setTabOrder(self.inputPassword, self.inputConfirmPassword)
        self.setTabOrder(self.inputConfirmPassword, self.signupButton)

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
            password_hash = hashlib.sha3_512(password.encode()).hexdigest()
            addDetails(username, email, password_hash)

    def loginfunction(self):
        self.login_ = login.LoginScreen()
        self.login_.show()
        self.close()
            
if __name__ == '__main__':
	app = QApplication(sys.argv)
	signupForm = SignupScreen()
	signupForm.show()
	sys.exit(app.exec_())