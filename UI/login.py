import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
import image_rc
import sqlite3
import hashlib

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi('login.ui',self)
        self.setStyleSheet("background-image: url(:/images/loginBackground.png);")
        self.loginButton.clicked.connect(self.loginfunction)
        self.forgotpasswordButton.clicked.connect(self.forgotPassword)
        self.signupButton.clicked.connect(self.signupfunction)

    def loginfunction(self):
        username = self.inputUsername.text()
        password = self.inputPassword.text()

        if len(username) == 0 or len(password) == 0:
            self.errorLabel.setText("Please input all fields.")

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

    def forgotPassword(self):
        print('forgot password')

    def signupfunction(self):
        print('signup')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	loginForm = LoginScreen()
	loginForm.show()
	sys.exit(app.exec_())