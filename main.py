

import  mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets

from signup import  Ui_secondWindow
from products import  Ui_threeWindow
class Ui_MainWindow(object):
    def open_win(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_secondWindow()
        self.ui.setupUi(self.window,MainWindow)
        self.window.show()
    def open_win_products(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_threeWindow()
        self.ui.setupUi(self.window,MainWindow)
        self.ui.user_lbl.setText(f'Hi {self.username_en.text()}')
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 579)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Asus/Desktop/Type-online-app-master/src/img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #fff; border-radius: 5px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(130, 20, 241, 211))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("image/edit-user-256.ico"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(460, 10, 30, 30))
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setStyleSheet("background:none;")
        self.btn_close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Asus/Desktop/Type-online-app-master/src/img/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QtCore.QSize(20, 20))
        self.btn_close.setObjectName("btn_close")
        self.btn_minimze = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minimze.setGeometry(QtCore.QRect(430, 10, 30, 30))
        self.btn_minimze.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimze.setStyleSheet("background:none;")
        self.btn_minimze.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Asus/Desktop/Type-online-app-master/src/img/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimze.setIcon(icon2)
        self.btn_minimze.setIconSize(QtCore.QSize(20, 20))
        self.btn_minimze.setObjectName("btn_minimze")
        self.btn_changemood = QtWidgets.QPushButton(self.centralwidget)
        self.btn_changemood.setGeometry(QtCore.QRect(400, 13, 30, 30))
        self.btn_changemood.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_changemood.setStyleSheet("background:none;")
        self.btn_changemood.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/Asus/Desktop/Type-online-app-master/src/img/change-theme.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_changemood.setIcon(icon3)
        self.btn_changemood.setIconSize(QtCore.QSize(20, 20))
        self.btn_changemood.setObjectName("btn_changemood")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 270, 500, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color:  #600080;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.usernamelb = QtWidgets.QLabel(self.centralwidget)
        self.usernamelb.setGeometry(QtCore.QRect(80, 340, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.usernamelb.setFont(font)
        self.usernamelb.setStyleSheet("color: #010A1A;")
        self.usernamelb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.usernamelb.setObjectName("usernamelb")
        self.passlb = QtWidgets.QLabel(self.centralwidget)
        self.passlb.setGeometry(QtCore.QRect(80, 390, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.passlb.setFont(font)
        self.passlb.setStyleSheet("color: #010A1A;")
        self.passlb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passlb.setObjectName("passlb")
        self.username_en = QtWidgets.QLineEdit(self.centralwidget)
        self.username_en.setGeometry(QtCore.QRect(180, 340, 230, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.username_en.setFont(font)
        self.username_en.setStyleSheet("background-color: #DEDEDE; color: #010A1A;\n"
"border-radius: 8px;")
        self.username_en.setObjectName("username_en")
        self.password_en = QtWidgets.QLineEdit(self.centralwidget)
        self.password_en.setGeometry(QtCore.QRect(180, 390, 230, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.password_en.setFont(font)
        self.password_en.setStyleSheet("background-color: #DEDEDE; color: #010A1A;\n"
"border-radius: 8px;")
        self.password_en.setObjectName("password_en")
        self.password_en.setEchoMode( QtWidgets.QLineEdit.Password)
        self.btn_login = QtWidgets.QPushButton(self.centralwidget,clicked = lambda :self. login_users())
        self.btn_login.setGeometry(QtCore.QRect(80, 460, 330, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setStyleSheet("border-radius: 8px;\n"
"background-color:#600080 ;\n"
"color: #ffffff;")
        self.btn_login.setObjectName("btn_login")
        self.acountlb = QtWidgets.QLabel(self.centralwidget)
        self.acountlb.setGeometry(QtCore.QRect(150, 510, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.acountlb.setFont(font)
        self.acountlb.setStyleSheet("color: #010A1A;")
        self.acountlb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.acountlb.setObjectName("acountlb")
        self.btn_signup = QtWidgets.QPushButton(self.centralwidget,clicked = lambda :self.open_win())
        self.btn_signup.setGeometry(QtCore.QRect(275, 510, 61, 31))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_signup.setFont(font)
        self.btn_signup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_signup.setStyleSheet("QPushButton{\n"
"background: none; color: #600080;  text-decoration: none;\n"
"}\n"
"QPushButton:hover{\n"
" text-decoration: underline;\n"
"}")
        self.btn_signup.setObjectName("btn_signup")
        self.alarmlb = QtWidgets.QLabel(self.centralwidget)
        self.alarmlb.setGeometry(QtCore.QRect(80, 430, 330, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.alarmlb.setFont(font)
        self.alarmlb.setStyleSheet("color: #d1131f;")
        self.alarmlb.setText("")
        self.alarmlb.setAlignment(QtCore.Qt.AlignCenter)
        self.alarmlb.setObjectName("alarmlb")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_close.clicked.connect(MainWindow.close) # type: ignore
        self.btn_minimze.clicked.connect(MainWindow.showMinimized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","Login"))
        self.title.setText(_translate("MainWindow", "LOG IN"))
        self.usernamelb.setText(_translate("MainWindow", "Username:"))
        self.passlb.setText(_translate("MainWindow", "Password:"))
        self.btn_login.setText(_translate("MainWindow", "Log in"))
        self.acountlb.setText(_translate("MainWindow", "Don\'t have acount?"))
        self.btn_signup.setText(_translate("MainWindow", "Sign up"))
        self.mydb = mysql.connector.connect(host='localhost',
                                            user='root',
                                            password='A2980305014',
                                            database='products_managements')
        self.my_cursor = self.mydb.cursor()
        #     # self.my_cursor.execute("CREATE DATABASE products_management")
        self.my_cursor.execute(
            "CREATE TABLE IF NOT EXISTS users(username varchar(255), password varchar(255), email varchar(255) )")

    def clear_field(self):
        self.username_en.clear()
        self.password_en.clear()

    def login_users(self):

        if (self.username_en.text().strip() == '' ) or (self.password_en.text().strip() == '' ) :
            self.alarmlb.setText('Fill all the blanks')
        else:
            self.my_cursor.execute("SELECT * FROM users")
            records = self.my_cursor.fetchall()
            self.alarmlb.setText('')
            if records != '':
                for record in records:
                    if (record[0] != self.username_en.text()) or (record[1] != self.password_en.text()):
                        self.alarmlb.setText('Username or password is not correct!')
                    else:
                        self.alarmlb.setText('')
                        self.open_win_products()
                        self.clear_field()
            else:
                self.alarmlb.setText('You must register first.')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
