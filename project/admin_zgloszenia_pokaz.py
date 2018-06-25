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

class Table_sprzet(QTableWidget):
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
        self.show_sprzet()


    def show_sprzet(self):
        headers = ['ulicy', 'data', 'klient']

        list_orders = self.db.get_all_orders()
        self.widget = Table_sprzet(len(list_orders), 3)
        self.widget.setHorizontalHeaderLabels(headers)

        i = 0
        for order in list_orders:
            item_ulicy = QTableWidgetItem(order.order_description)
            item_data = QTableWidgetItem(str(order.order_date))
            item_klient = QTableWidgetItem(str(order.klient_username))
            self.widget.setItem(i,0, item_ulicy)
            self.widget.setItem(i,1, item_data)
            self.widget.setItem(i,2, item_klient)

            i+=1

        self.setCentralWidget(self.widget)
        self.resize(350,300)
        self.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sheet = Sheet()
    sys.exit(app.exec_())


