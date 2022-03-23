import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPalette, QBrush

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Welcome')
        self.resize(480, 720)

        # Background Image
        background = QImage("images/loginBackground.png")
        scaled_background = background.scaled(QSize(480 ,720))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled_background))                        
        self.setPalette(palette)

        layout = QGridLayout()

        # Stylesheets
        label_style = "padding-left: 20px; font-size: 20px; color: white;"
        input_style = "padding: 5px; font-size: 19px; margin-right: 20px; color: white; background: #00000000; \
         border: none; border-bottom: 1px solid white;"
        button_style = "margin: 0 20px; padding: 10px; font-size: 18px; background-color: #ffffff;"

        # Username
        label_username = QLabel('Username')
        label_username.setStyleSheet(label_style)

        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setStyleSheet(input_style)
        layout.addWidget(label_username, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        # Password
        label_password = QLabel('Password')
        label_password.setStyleSheet(label_style)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setStyleSheet(input_style)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        # Login button
        button_login = QPushButton('Login')
        button_login.setStyleSheet(button_style)
        layout.addWidget(button_login, 2, 0, 1, 2)
        # layout.setRowStretch(4, 1)

        self.setLayout(layout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = LoginForm()
	form.show()
	sys.exit(app.exec_())