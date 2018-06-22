# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_sprztet_pokaz.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QMainWindow, QTableWidgetItem
from database.DatabaseManager import DataBaseManager
from dbmanagers.CheckManager import CheckManager
from managers.WarningManger import WarningManager
from managers.EmailNotifications import EmailNotifications
from helpers.Helpers import Helpers

class Table_users(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)

        self.show()

class Sheet(QMainWindow):

    def __init__(self):
        super().__init__()
        self.db = DataBaseManager()
        self.check_manager = CheckManager()
        self.warning_manager = WarningManager()
        self.email_notifications = EmailNotifications()
        self.helpers = Helpers()
        self.show_users()


    def show_users(self):
        headers = ['user_name', 'password', 'account_type','mail',
                   'imie','nazwisko','telefon','adres','active']

        list_users = self.db.get_all_users()
        self.widget = Table_users(len(list_users), len(headers))
        self.widget.setHorizontalHeaderLabels(headers)

        i = 0
        for user in list_users:
            user_name = QTableWidgetItem(user.user_name)
            password = QTableWidgetItem(user.password)
            account_type = QTableWidgetItem(user.account_type)
            mail = QTableWidgetItem(user.mail)
            imie = QTableWidgetItem(user.imie)
            nazwisko = QTableWidgetItem(user.nazwisko)
            telefon = QTableWidgetItem(str(user.telefon))
            adres = QTableWidgetItem(user.adres)

            if (user.active == 1):
                active = QTableWidgetItem('Active')
            elif (user.active == 0):
                active = QTableWidgetItem('Inactive')
            else:
                active = QTableWidgetItem('Else')


            self.widget.setItem(i, 0, user_name)
            self.widget.setItem(i, 1, password)
            self.widget.setItem(i, 2, account_type)
            self.widget.setItem(i, 3, mail)
            self.widget.setItem(i, 4, imie)
            self.widget.setItem(i, 5, nazwisko)
            self.widget.setItem(i, 6, telefon)
            self.widget.setItem(i, 7, adres)
            self.widget.setItem(i, 8, active)

            i+=1

        self.setCentralWidget(self.widget)
        self.resize(901, 300)
        self.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sheet = Sheet()
    sys.exit(app.exec_())


