# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminsprzet.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

from database.DatabaseManager import DataBaseManager
from dbmanagers.CheckManager import CheckManager
from helpers.Helpers import Helpers
from managers.EmailNotifications import EmailNotifications
from managers.WarningManger import WarningManager
from managers.GenerateCSV import saveCSV


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.save_to_csv = saveCSV
        self.db = DataBaseManager()
        self.check_manager = CheckManager()
        self.warning_manager = WarningManager()
        self.email_notifications = EmailNotifications()
        self.helpers = Helpers()

    def generujRaport(self):
        list_harmonograms = self.db.get_all_actual_harmonogram()
        self.save_to_csv(list_harmonograms)
        self.warning_manager.showWarningBox('Error', 'Wygenerowano')
        return None


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setObjectName("pushButton")
        ############### Button Event ####################
        self.pushButton.clicked.connect(self.generujRaport)
        #################################################
        self.verticalLayout.addWidget(self.pushButton)

        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Generuj Raport"))

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

