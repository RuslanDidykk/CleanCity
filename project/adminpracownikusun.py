# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminpracownikusun.ui'
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

    def __init__(self):
        self.db = DataBaseManager()
        self.check_manager = CheckManager()
        self.warning_manager = WarningManager()
        self.email_notifications = EmailNotifications()
        self.helpers = Helpers()

    def delete_user(self):
        USER_NAME = self.lineEdit.text()
        self.user_data_obj = self.db.getUserData(USER_NAME)
        if self.user_data_obj is None:
            self.warning_manager.showWarningBox('error', 'incorrect user_name')
            return None

        check_exc = self.db.insert_not_active_status(USER_NAME)
        if check_exc is not None:
            self.warning_manager.showWarningBox('error', 'incorrect user_name')
            return None

        self.MainWindow.close()
        return None


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 294)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        ############### Button Event ####################
        self.pushButton_2.clicked.connect(self.delete_user)
        #################################################
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 22))
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
        self.label.setText(_translate("MainWindow", "user_name:"))
        self.pushButton_2.setText(_translate("MainWindow", "Usun uzytkownika"))

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

