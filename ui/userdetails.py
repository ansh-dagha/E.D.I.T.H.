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
    def __init__(self):
        super(UserDetails, self).__init__()
        details_ui_path = os.path.join(os.path.dirname(sys.path[0]),'ui\\userdetails.ui')
        loadUi(details_ui_path, self)

        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)

        self.radioButtonM.clicked.connect(lambda: self.playfunction(0))
        self.radioButtonF.clicked.connect(lambda: self.playfunction(1))
        self.playButton.clicked.connect(self.play)

    def playfunction(self, voice):
        speak('Hello Sir, My name is EDITH.', voice)
    
    def play(self):
        voice = 0
        if self.radioButtonF.isChecked():
            voice = 1
        speak('Hello Sir, My name is EDITH.', voice)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    userDetailsForm = UserDetails()
    userDetailsForm.show()
    sys.exit(app.exec_())