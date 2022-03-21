import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Welcome')
        self.resize(480, 720)

        background = QImage("D:/SEM VI/MP/AI-Assistant/ui/loginBackground.png")
        scaled_background = background.scaled(QSize(480 ,720))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled_background))                        
        self.setPalette(palette)

        """ background = QPixmap('loginBackground.png').scaledToWidth(480)
        self.image = QLabel()
        self.image.setPixmap(background)
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)  # prevents margins around layouts
        layout.addWidget(self.image) """

        layout = QGridLayout()

        # Stylesheets
        label_style = "padding-left: 20px; font-size: 20px; color: white;"
        input_style = "padding: 5px; font-size: 19px; margin-right: 20px; color: white; background: rgb(0, 0, 0, 0); \
         border: none; border-bottom: 1px solid white;"

        label_username = QLabel('Username')
        label_username.setStyleSheet(label_style)

        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setStyleSheet(input_style)
        layout.addWidget(label_username, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('Password')
        label_password.setStyleSheet(label_style)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setStyleSheet(input_style)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        # button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        # layout.setRowStretch(4, 1)

        self.setLayout(layout)

    # def check_password(self):
    #     msg = QMessageBox()

    #     if self.lineEdit_username.text() == 'Usernmae' and self.lineEdit_password.text() == '000':
    #         msg.setText('Success')
    #         msg.exec_()
    #         app.quit()
    #     else:
    #         msg.setText('Incorrect Password')
    #         msg.exec_()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = LoginForm()
	form.show()
	sys.exit(app.exec_())