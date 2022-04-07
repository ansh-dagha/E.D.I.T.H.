import sys
sys.path.append("..")

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from click import confirm
import image_rc

from database.db_functions import *
import sqlite3
import hashlib
import re

# python -m PyQt5.pyrcc_main image.qrc -o image_rc.py

class SignupScreen(QDialog):
    def __init__(self):
        super(SignupScreen, self).__init__()
        loadUi('signup.ui',self)
        self.setStyleSheet("background-image: url(:/images/loginBackground.png);")
        self.signupButton.clicked.connect(self.signupfunction)
        # self.loginButton.clicked.connect(self.loginfunction)

    def signupfunction(self):
        username = self.inputUsername.text()
        email = self.inputEmail.text()
        password = self.inputPassword.text()
        confirm_password = self.inputConfirmPassword.text()
        

        if len(username) == 0 or len(password) == 0 or len(email) == 0 or len(confirm_password) == 0:
            self.errorLabel.setText("Please input all fields.")

        elif userExists(username):
            self.errorLabel.setText(f"Username '{username}' already exists.")

        elif not bool(re.match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$",email)):
            self.errorLabel.setText("Enter a valid email.")

        elif password != confirm_password:
            self.errorLabel.setText("Passwords do not match.")

        else:
            password_hash = hashlib.sha3_512(password.encode()).hexdigest()

            conn = sqlite3.connect("assistant.db")
            c = conn.cursor()
        
            c.execute("SELECT password FROM users WHERE username = ?", (username,))
            result_pass = c.fetchone()

            if result_pass == None:
                print('Username doesn\'t exists')
                self.errorLabel.setText('Username doesn\'t exists! Kindly signup.')
                self.inputUsername.clear()
                self.inputPassword.clear()

            else:
                if result_pass[0] == password:
                    print("Successfully logged In.")
                else:
                    self.errorLabel.setText('Incorrect password! Please try again.')
                     

if __name__ == '__main__':
	app = QApplication(sys.argv)
	loginForm = SignupScreen()
	loginForm.show()
	sys.exit(app.exec_())