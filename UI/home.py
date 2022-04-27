import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt

gifs_dir = os.path.join(os.path.dirname(sys.path[0]),'ui\\gifs\\')

class LoadingGif(object):

    def mainUI(self, FrontWindow):
        FrontWindow.setObjectName("FTwindow")
        FrontWindow.resize(450, 650)
        FrontWindow.setMinimumSize(QtCore.QSize(450, 650))
        FrontWindow.setMaximumSize(QtCore.QSize(450, 650))
        self.centralwidget = QtWidgets.QWidget(FrontWindow)
        self.centralwidget.setObjectName("main-widget")

        # Label Create
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 450, 650))
        self.label.setObjectName("lb1")
        self.label.setStyleSheet("""
                background-color: white;
        """)
        self.label.setAlignment(Qt.AlignCenter)
        FrontWindow.setCentralWidget(self.centralwidget)

        # Loading the GIF
        self.movie = QMovie(gifs_dir+"mic.gif")
        self.label.setMovie(self.movie)

        self.startAnimation()

    # Start Animation

    def startAnimation(self):
        self.movie.start()

    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
demo = LoadingGif()
demo.mainUI(window)
window.show()
sys.exit(app.exec_())
