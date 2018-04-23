# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminEditUser.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from database.DatabaseManager import DataBaseManager
from dbmanagers.CheckManager import CheckManager
from managers.WarningManger import WarningManager
from managers.EmailNotifications import EmailNotifications
from helpers.Helpers import Helpers

class Ui_MainWindow(object):

    USER_NAME = ''

    def __init__(self):
        self.db = DataBaseManager()
        self.check_manager = CheckManager()
        self.warning_manager = WarningManager()
        self.email_notifications = EmailNotifications()
        self.helpers = Helpers()

    def radioIsChecked(self):
        if self.radio_User.isChecked():
            self.account_type = 'user'
        elif self.radio_Admin.isChecked():
            self.account_type = 'admin'
        elif self.radio_Klient_2.isChecked():
            self.account_type = 'klient'
        else:
            return False

    def check_type_of_account(self, account_type):
        if account_type == 'user':
            self.radio_User.click()
        elif account_type == 'admin':
            self.radio_Admin.click()
        elif account_type == 'klient':
            self.radio_Klient_2.click()


    def clear_all_lines(self):
        self.lineEdit_imie.clear()
        self.lineEdit_nazwisko.clear()
        self.lineEdit_telefon.clear()
        self.lineEdit_email.clear()
        self.lineEdit_Adres.clear()
        self.lineEdit_kod_pocztowy.clear()
        self.lineEdit_PESEL.clear()
        self.lineEdit_haslo.clear()

    def get_info_about_user(self):
        self.clear_all_lines()
        self.USER_NAME = self.lineEdit_login.text()
        self.user_data_obj = self.db.getUserData(self.USER_NAME)
        if self.user_data_obj is None:
            self.warning_manager.showWarningBox('error', 'incorrect user_name')
            return None

        self.lineEdit_imie.insert(self.user_data_obj.imie)
        self.lineEdit_nazwisko.insert(self.user_data_obj.nazwisko)
        self.lineEdit_telefon.insert(str(self.user_data_obj.telefon))
        self.lineEdit_email.insert(self.user_data_obj.mail)
        self.lineEdit_Adres.insert(self.user_data_obj.adres)
        self.lineEdit_kod_pocztowy.insert(self.user_data_obj.kod_pocztowy)
        self.lineEdit_PESEL.insert(str(self.user_data_obj.PESEL))
        self.lineEdit_haslo.insert(self.user_data_obj.password)

        account_type = self.user_data_obj.account_type
        self.check_type_of_account(account_type)


    def editUser(self):
        password = self.lineEdit_haslo.text()
        self.account_type = ''
        mail = self.lineEdit_email.text()
        imie = self.lineEdit_imie.text()
        nazwisko = self.lineEdit_nazwisko.text()
        telefon = self.lineEdit_telefon.text()
        adres = self.lineEdit_Adres.text()
        kod_pocztowy = self.lineEdit_kod_pocztowy.text()
        pesel = self.lineEdit_PESEL.text()

        self.user_data_obj = self.db.getUserData(self.USER_NAME)
        if self.user_data_obj is None:
            self.warning_manager.showWarningBox('error', 'incorrect user_name')
            return None

        if not self.helpers.checkCorrectionMail(mail):
            self.warning_manager.showWarningBox('error', 'incorrect mail!!!')
            return None

        correction_logindata = self.check_manager.checkCorrectionLoginData(self.USER_NAME,password)
        if not correction_logindata:
            self.warning_manager.showWarningBox('error', 'incorrect login data')
            return None

        if self.radioIsChecked():
            self.warning_manager.showWarningBox('error', 'please check an account type')
            return None

        data = {}
        data['username'] = self.USER_NAME
        data['password'] = password
        data['account_type'] = self.account_type
        data['mail'] = mail
        data['imie'] = imie
        data['nazwisko'] = nazwisko
        data['telefon'] = telefon
        data['adres'] = adres
        data['kod_pocztowy'] = kod_pocztowy
        data['pesel'] = pesel

        check_exception = self.db.editUser(data)
        if check_exception:
            self.warning_manager.showWarningBox('Error', str(check_exception))
            return None

        # check_exception = self.email_notifications.sendUserRegistered(mail,self.USER_NAME,password)
        # if check_exception:
        #     self.warning_manager.showWarningBox('Error', str(check_exception))
        #     return None

        self.MainWindow.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(429, 516)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lineEdit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_login.setMinimumSize(QtCore.QSize(280, 0))
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.horizontalLayout_3.addWidget(self.lineEdit_login)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        ############### Button Event ####################
        self.pushButton.clicked.connect(self.get_info_about_user)
        #################################################
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.lineEdit_imie = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_imie.setMinimumSize(QtCore.QSize(280, 0))
        self.lineEdit_imie.setMaximumSize(QtCore.QSize(900, 16777215))
        self.lineEdit_imie.setObjectName("lineEdit_imie")
        self.horizontalLayout_10.addWidget(self.lineEdit_imie)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.lineEdit_nazwisko = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nazwisko.setMinimumSize(QtCore.QSize(280, 0))
        self.lineEdit_nazwisko.setObjectName("lineEdit_nazwisko")
        self.horizontalLayout_9.addWidget(self.lineEdit_nazwisko)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        # self.label_4 = QtWidgets.QLabel(self.centralwidget)
        # self.label_4.setObjectName("label_4")
        # self.horizontalLayout_8.addWidget(self.label_4)
        # spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_8.addItem(spacerItem3)
        # self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit_id.setMinimumSize(QtCore.QSize(280, 0))
        # self.lineEdit_id.setObjectName("lineEdit_id")
        # self.horizontalLayout_8.addWidget(self.lineEdit_id)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.lineEdit_telefon = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_telefon.setMinimumSize(QtCore.QSize(280, 0))
        self.lineEdit_telefon.setObjectName("lineEdit_telefon")
        self.horizontalLayout_7.addWidget(self.lineEdit_telefon)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setMinimumSize(QtCore.QSize(280, 0))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.horizontalLayout_6.addWidget(self.lineEdit_email)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.lineEdit_Adres = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Adres.setMinimumSize(QtCore.QSize(280, 0))
        self.lineEdit_Adres.setObjectName("lineEdit_Adres")
        self.horizontalLayout_5.addWidget(self.lineEdit_Adres)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.lineEdit_kod_pocztowy = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_kod_pocztowy.setMinimumSize(QtCore.QSize(280, 0))
        self.lineEdit_kod_pocztowy.setObjectName("lineEdit_kod_pocztowy")
        self.horizontalLayout_2.addWidget(self.lineEdit_kod_pocztowy)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.lineEdit_PESEL = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_PESEL.setMinimumSize(QtCore.QSize(280, 0))
        self.lineEdit_PESEL.setObjectName("lineEdit_PESEL")
        self.horizontalLayout_4.addWidget(self.lineEdit_PESEL)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.lineEdit_haslo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_haslo.setMinimumSize(QtCore.QSize(280, 0))
        self.lineEdit_haslo.setObjectName("lineEdit_haslo")
        self.horizontalLayout.addWidget(self.lineEdit_haslo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.radio_User = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_User.setObjectName("radio_User")
        self.verticalLayout.addWidget(self.radio_User)
        self.radio_Admin = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_Admin.setObjectName("radio_Admin")
        self.verticalLayout.addWidget(self.radio_Admin)
        self.radio_Klient_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_Klient_2.setObjectName("radio_Klient_2")
        self.verticalLayout.addWidget(self.radio_Klient_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.btn_edit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edit.setObjectName("btn_edit")
        ############### Button Event ####################
        self.btn_edit.clicked.connect(self.editUser)
        #################################################
        self.horizontalLayout_11.addWidget(self.btn_edit)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Edycja konta"))
        self.label_9.setText(_translate("MainWindow", "Login: "))
        self.pushButton.setText(_translate("MainWindow", "get info about user"))
        self.label.setText(_translate("MainWindow", "Imie:"))
        self.label_3.setText(_translate("MainWindow", "Nazwisko: "))
        # self.label_4.setText(_translate("MainWindow", "ID: "))
        self.label_5.setText(_translate("MainWindow", "Telefon: "))
        self.label_6.setText(_translate("MainWindow", "Adres email: "))
        self.label_7.setText(_translate("MainWindow", "Adres: "))
        self.label_11.setText(_translate("MainWindow", "Kod pocztowy:"))
        self.label_8.setText(_translate("MainWindow", "PESEL: "))
        self.label_10.setText(_translate("MainWindow", "Haslo: "))
        self.radio_User.setText(_translate("MainWindow", "User"))
        self.radio_Admin.setText(_translate("MainWindow", "Admin"))
        self.radio_Klient_2.setText(_translate("MainWindow", "Klient"))
        self.btn_edit.setText(_translate("MainWindow", "Edytuj"))

        ####################################

        self.MainWindow = MainWindow


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

