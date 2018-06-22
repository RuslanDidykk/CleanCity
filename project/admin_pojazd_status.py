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


    def get_list_pojzdow(self):
        list_db_pojazd = self.db.get_all_pojazd()
        for pojazd in list_db_pojazd:
            self.comboBox_pojazd.addItem(str(pojazd.nazwa)+' : '+str(pojazd.numer))

    def insert_pojazd(self):
        pojazd = self.comboBox_pojazd.currentText().split(':')[1].strip()
        status = self.comboBox_status.currentText()

        data = {}

        data['pojazd'] = pojazd
        data['status'] = status


        check_exception = self.db.edit_status_pojazd(data)
        if check_exception:
            self.warning_manager.showWarningBox('Error', str(check_exception))
            return None

        self.warning_manager.showWarningBox('', 'Dodano')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(448, 269)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(80, 50))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.comboBox_pojazd = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_pojazd.setObjectName("comboBox_pojazd")
        self.horizontalLayout_4.addWidget(self.comboBox_pojazd)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(80, 60))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.comboBox_status = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_status.setObjectName("comboBox_status")
        self.comboBox_status.addItem('Active')
        self.comboBox_status.addItem('W naprawie')
        self.comboBox_status.addItem('Not Active')
        self.horizontalLayout_5.addWidget(self.comboBox_status)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")

        ############### Button Event ####################
        self.pushButton.clicked.connect(self.insert_pojazd)
        #################################################

        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pojazd Status"))
        self.label.setText(_translate("MainWindow", "Pojazd:"))
        self.label_2.setText(_translate("MainWindow", "Status:"))
        self.pushButton.setText(_translate("MainWindow", "Edit"))

        self.get_list_pojzdow()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

