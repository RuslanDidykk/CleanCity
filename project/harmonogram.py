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
        headers = ['klient', 'ulica', 'pracownik','pojazd',
                   'date','sprzet', 'sprzet_ilosc']

        list_harmonograms = self.db.get_all_actual_harmonogram()
        self.widget = Table_users(len(list_harmonograms), len(headers))
        self.widget.setHorizontalHeaderLabels(headers)

        i = 0
        for harmonograms in list_harmonograms:
            klient_nazwa = QTableWidgetItem(harmonograms.klient_nazwa)
            ulica = QTableWidgetItem(harmonograms.ulica)
            pracownik = QTableWidgetItem(harmonograms.pracownik)
            pojazd = QTableWidgetItem(harmonograms.pojazd)
            date = QTableWidgetItem(str(harmonograms.date))
            sprzet = QTableWidgetItem(str(harmonograms.sprzet))
            sprzet_ilosc = QTableWidgetItem(str(harmonograms.sprzet_ilosc))

            # if (harmonograms.active == 1):
            #     active = QTableWidgetItem('Active')
            # elif (harmonograms.active == 0):
            #     active = QTableWidgetItem('Inactive')
            # else:
            #     active = QTableWidgetItem('Else')


            self.widget.setItem(i, 0, klient_nazwa)
            self.widget.setItem(i, 1, ulica)
            self.widget.setItem(i, 2, pracownik)
            self.widget.setItem(i, 3, pojazd)
            self.widget.setItem(i, 4, date)
            self.widget.setItem(i, 5, sprzet)
            self.widget.setItem(i, 6, sprzet_ilosc)

            i+=1

        self.setCentralWidget(self.widget)
        self.resize(600, 300)
        self.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sheet = Sheet()
    sys.exit(app.exec_())


