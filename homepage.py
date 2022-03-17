# # Import module
# from tkinter import *
# from tkinter.filedialog import Open
# from PIL import ImageTk, Image

# # Create object
# root = Tk()

# # Adjust size
# root.geometry("400x400")


# # Add image file
# bg = ImageTk.PhotoImage(Image.open("bg.jpg"))
# background_label = Label(root, image=bg)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
# root.iconbitmap('assistant.ico')

# name_label = Label(text = 'Edith',width = 300, bg = "black", fg="white", font = ("Calibri", 13))
# name_label.pack()

# microphone_photo = ImageTk.PhotoImage(Image.open("mic.jpg"))
# microphone_button = Button(image=microphone_photo)
# microphone_button.pack(padx = 10,pady=150)


# # Execute tkinter
# root.mainloop()
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
       QWidget.__init__(self)
       self.setGeometry(360,540,360,540)

       oImage = QImage("bg.jpg")
       sImage = oImage.scaled(QSize(300,200))                   # resize Image to widgets size
       palette = QPalette()
       palette.setBrush(QPalette.Window, QBrush(sImage))                        
       self.setPalette(palette)

       self.label = QLabel('Test', self)                        # test, if it's really backgroundimage
       self.label.setGeometry(50,50,200,50)
       self.label.setStyleSheet("color: white;")

    #    self.button = QPushButton('', self)
    #    self.button.clicked.connect(self.handleButton)
    #    self.button.setIcon(QIcon('mic.jpg'))
    #    self.button.setIconSize(QSize(24,24))
    #    layout = QVBoxLayout(self)
    #    layout.addWidget(self.button)

       self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())