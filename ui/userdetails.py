import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication
import image_rc

sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'database'))
from db_functions import *
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def speak(text, voice):
    engine.setProperty('voice', voices[voice].id)
    engine.say(text)
    engine.runAndWait()

class UserDetails(QDialog):
    def __init__(self, username = ''):
        super(UserDetails, self).__init__()
        details_ui_path = os.path.join(os.path.dirname(sys.path[0]),'ui\\userdetails.ui')
        loadUi(details_ui_path, self)

        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, True)
        # self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)

        self.username = username

        self.radioButtonM.setChecked(True)
        self.playButton.clicked.connect(self.playfunction)
        self.continueButton.clicked.connect(self.continuefunction)

    def playfunction(self, voice = 0):
        if self.radioButtonF.isChecked():
            voice = 1
        addressee = self.comboBox.currentText()
        speak(f'Hello {addressee}, My name is EDITH. I am your personal assistant', voice)

    def continuefunction(self):
        voice = 0 if self.radioButtonM.isChecked() else 1
        addressee = self.comboBox.currentText()
        updatePreference(voice, addressee, self.username)
        print('Successful')
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    userDetailsForm = UserDetails()
    userDetailsForm.show()
    sys.exit(app.exec_())