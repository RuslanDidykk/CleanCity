# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_add_harmonogram.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import dateparser as dateparser
import datetime
from PyQt5.QtWidgets import QTableWidget, QMainWindow, QTableWidgetItem
from database.DatabaseManager import DataBaseManager
from dbmanagers.CheckManager import CheckManager
from managers.WarningManger import WarningManager
from managers.EmailNotifications import EmailNotifications
from helpers.Helpers import Helpers


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.db = DataBaseManager()
        self.check_manager = CheckManager()
        self.warning_manager = WarningManager()
        self.email_notifications = EmailNotifications()
        self.helpers = Helpers()

    def get_list_klientow(self):
        list_db_klient = self.db.get_all_klientow()
        for user in list_db_klient:
            self.comboBox_klient.addItem(user.user_name)

    def get_list_pracownik(self):
        list_db_users = self.db.get_all_pracownikow()
        for user in list_db_users:
            self.comboBox_pracownik.addItem(user.user_name)

    def get_list_pojzdow(self):
        list_db_pojazd = self.db.get_all_active_pojazd()
        for pojazd in list_db_pojazd:
            self.comboBox_pojazd.addItem(str(pojazd.nazwa)+' : '+str(pojazd.numer))

    def get_list_sprzet(self):
        list_db_sprzet = self.db.get_all_sprzet()
        for sprzet in list_db_sprzet:
            self.comboBox_sprzet.addItem(str(sprzet.sprzet)+' : '+str(sprzet.ilosc))

    def set_date(self, date):
        self.date = date.toString()

    def insert_to_harmonogram(self):
        klient_nazwa = self.comboBox_klient.currentText()
        pracownik = self.comboBox_pracownik.currentText()
        pojazd = self.comboBox_pojazd.currentText().split(':')[1].strip()
        ulica = self.lineEdit_ulica.text()
        sprzet = self.comboBox_sprzet.currentText().split(':')[0].strip()
        try:
            sprzet_ilosc = int(self.lineEdit.text())
        except:
            sprzet_ilosc = 0
        try:
            date = dateparser.parse(self.date)
        except:
            self.warning_manager.showWarningBox('Error', 'Wybierz date')
            return None

        sprzet_db_ilosc = int(self.comboBox_sprzet.currentText().split(':')[1].strip())
        if sprzet_db_ilosc < sprzet_ilosc:
            self.warning_manager.showWarningBox('Error', 'Wybrales wiecej sprzetu niz istnieje')
            return None

        data = {}

        data['klient_nazwa'] = klient_nazwa
        data['pracownik'] = pracownik
        data['pojazd'] = pojazd
        data['ulica'] = ulica
        data['date'] = date
        data['sprzet'] = sprzet
        data['sprzet_ilosc'] = sprzet_ilosc

        check_exception = self.db.check_person_in_harmonogram(pracownik,date)
        if check_exception is not None:
            self.warning_manager.showWarningBox('Error', 'Juz istnieje')
            return None

        check_exception = self.db.check_ilosc_pracownikow_na_pojazdzie(pojazd, date)
        print(len(check_exception))
        if len(check_exception) >= 3:
            self.warning_manager.showWarningBox('Error', 'Limit pracownikow dla jednego pojazdu')
            return None

        check_exception = self.db.add_item_to_harmongram(data)
        if check_exception:
            self.warning_manager.showWarningBox('Error', str(check_exception))
            # return None

        self.warning_manager.showWarningBox('', 'Dodano')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(100, 50))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.comboBox_klient = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_klient.setObjectName("comboBox_2")
        self.horizontalLayout_5.addWidget(self.comboBox_klient)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(100, 50))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_pracownik = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_pracownik.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox_pracownik)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(100, 50))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_pojazd = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_pojazd.setObjectName("comboBox_3")
        self.horizontalLayout.addWidget(self.comboBox_pojazd)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(60, 50))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.comboBox_sprzet = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_sprzet.setObjectName("comboBox_sprzet")
        self.horizontalLayout_4.addWidget(self.comboBox_sprzet)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEdit_ulica = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ulica.setObjectName("lineEdit_ulica")
        self.horizontalLayout_6.addWidget(self.lineEdit_ulica)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_2.addWidget(self.calendarWidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        ##########################################################
        self.pushButton.clicked.connect(self.insert_to_harmonogram)
        ###########################################################
        ##############
        self.calendarWidget.clicked.connect(self.set_date)
        ##############
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Dodaj klienta:"))
        self.label_2.setText(_translate("MainWindow", "Dodaj pracownika:"))
        self.label.setText(_translate("MainWindow", "Doadj pojazd:"))
        self.comboBox_pojazd.setItemText(0, _translate("MainWindow", "dsadas"))
        self.comboBox_pojazd.setItemText(1, _translate("MainWindow", "dsa"))
        self.comboBox_pojazd.setItemText(2, _translate("MainWindow", "aaaa"))
        self.comboBox_pojazd.setItemText(3, _translate("MainWindow", "dasdas"))
        self.label_6.setText(_translate("MainWindow", "Sprzet: "))
        self.label_5.setText(_translate("MainWindow", "Ulica:"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

        self.get_list_pracownik()
        self.get_list_klientow()
        self.get_list_pojzdow()
        self.get_list_sprzet()

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
