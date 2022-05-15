import os, sys
from unittest import TestResult
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QAction
import UI.image_rc

sys.path.append(os.path.join(os.path.dirname(sys.path[0]),''))
from database.db_functions import *
import hashlib
import settings

app = QApplication(sys.argv)

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        login_ui_path = os.path.join(os.path.dirname(sys.path[0]),'AI-Assistant\\ui\\login.ui')
        loadUi(login_ui_path, self)

        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, True)

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
                settings.setUsername(username)
                settings.signUpFlag = False
                self.close()
                
            else:
                self.errorLabel.setText('Incorrect password! Please try again.')
                self.inputPassword.clear()
            
    def forgotPassword(self):
        print('forgot password')

    def signupfunction(self):
        self.close()
        settings.signUpFlag = True
        settings.exitFlag = False
    
    # def output(self):
    #     return self.signupflag

    def closeEvent(self, event):
        settings.signUpflag = False
        settings.exitFlag = True


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     login_ = login.LoginScreen()
#     login_.show()
#     sys.exit(app.exec_())