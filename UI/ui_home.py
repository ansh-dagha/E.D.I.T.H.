import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import image_rc
import test


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        home_ui_path = os.path.join(os.path.dirname(sys.path[0]),'ui\\home.ui')
        # home_ui_path = os.path.join(os.path.dirname(sys.path[0]),'AI-Assistant\\ui\\home.ui')
        loadUi(home_ui_path, self)

        username = 'anshdagha'
        self.profileButton.setStyleSheet("border-radius: 40px; \
            border-image: url(:/images/" + username + ".png) 0 0 0 0 stretch stretch;")

        self.optionsWidget.hide()
        self.tabWidget.hide()
        
        self.profileButton.clicked.connect(self.toggleOptions)
        self.cancelButton.clicked.connect(self.cancel)
        self.settingsButton.clicked.connect(self.openSettings)

    def toggleOptions(self):
        if self.optionsWidget.isVisible():
            self.optionsWidget.hide()
        else:
            self.optionsWidget.show()

    def openSettings(self):
        self.tabWidget.show()

    def cancel(self):
        self.tabWidget.close()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()