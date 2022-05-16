import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

sys.path.append(os.path.join(os.path.dirname(sys.path[0]),''))
from database.db_functions import *
import UI.image_rc
import settings
import hashlib
import shutil # pip install pytest-shutil
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def speak(text, voice):
    engine.setProperty('voice', voices[voice].id)
    engine.say(text)
    engine.runAndWait()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        home_ui_path = os.path.join(os.path.dirname(sys.path[0]),'AI-Assistant\\ui\\home.ui')
        loadUi(home_ui_path, self)

        self.username = settings.username

        self.optionsWidget.hide()
        self.tabWidget.hide()
        
        self.profileButton.clicked.connect(self.toggleOptions)
        self.cancelButton.clicked.connect(self.cancel)
        self.settingsButton.clicked.connect(self.openSettings)
        self.logoutButton.clicked.connect(self.logOut)

        self.setValues()
        self.setImages()
        
        self.saveButton.clicked.connect(self.saveAccountSettings)
        self.playButton.clicked.connect(self.playfunction)
        self.savePreferenceButton.clicked.connect(self.savePreferenceSettings)

        self.editProfilePhotoButton.clicked.connect(self.editProfilePhoto)
        self.editEmailButton.clicked.connect(self.editEmail)
        self.editPasswordButton.clicked.connect(self.editPassword)

        self.emailFlag = False
        self.passwordFlag = False

    def setValues(self):
        self.inputUsername.setText(self.username)
        self.email, self.voice, self.addressee = getUserDetails(self.username)
        self.inputEmail.setText(self.email)
        
        if self.voice == 0:
            self.radioButtonM.setChecked(True)
        else:
            self.radioButtonF.setChecked(True)

        self.comboBox.setCurrentText(self.addressee)

    def setImages(self):
        try:
            self.profileButton.setStyleSheet("border-radius: 40px; \
                border-image: url(:/images/" + self.username + ".png) 0 0 0 0 stretch stretch;")
            self.editProfilePhotoButton.setStyleSheet("border-radius: 40px; \
                border-image: url(:/images/" + self.username + ".png) 0 0 0 0 stretch stretch;")
        except Exception as e:
            print(e)
            pass

    def editProfilePhoto(self):
        try:
            file_filter = 'Image File (*.jpg; *.jpeg; *.gif; *.bmp)'
            response = QFileDialog.getOpenFileName(
                parent=self,
                caption='Select an Image',
                directory=os.getcwd(),
                filter=file_filter,
                initialFilter=file_filter,
            )
            src = response[0]
            dst = str(os.path.join(os.path.dirname(sys.path[0]),f'AI-Assistant\\ui\\images\\{self.username}.png'))
            shutil.copy2(src, dst)
            self.setImages()
        except Exception as e:
            print(e)

    def editEmail(self):
        self.inputEmail.setEnabled(True)
        self.emailFlag = True

    def editPassword(self):
        self.inputPassword.setEnabled(True)
        self.passwordFlag = True
        
    def saveAccountSettings(self):
        if self.emailFlag:
            newemail = self.inputEmail.text()
            updateEmail(newemail, self.username)
        
        if self.passwordFlag:
            password = self.inputPassword.text()
            password_hash = hashlib.sha3_512(password.encode()).hexdigest()
            updatePassword(password_hash, self.username)

        self.emailFlag = False
        self.passwordFlag = False

    def playfunction(self, voice = 0):
        if self.radioButtonF.isChecked():
            voice = 1
        addressee = self.comboBox.currentText()
        speak(f'Hello {addressee}, My name is EDITH. I am your personal assistant', voice)

    def savePreferenceSettings(self):
        voice = 0 if self.radioButtonM.isChecked() else 1
        addressee = self.comboBox.currentText()
        updatePreference(voice, addressee, self.username)
        print('Successful')

    def toggleOptions(self):
        if self.optionsWidget.isVisible():
            self.optionsWidget.hide()
        else:
            self.optionsWidget.show()

    def openSettings(self):
        self.tabWidget.show()

    def cancel(self):
        self.tabWidget.close()

    def logOut(self,event):
        self.close()
        settings.exitFlag = False

    def closeEvent(self,event):
        settings.stopNotifications = True
        settings.exitFlag = True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()