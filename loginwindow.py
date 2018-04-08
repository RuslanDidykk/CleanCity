# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QCoreApplication
from config import admin, user
from database.DatabaseManager import DataBaseManager
from dbmanagers.CheckManager import CheckManager
from managers.WarningManger import WarningManager

import adminmainmenu
import usermainmenu

class Ui_MainWindow(object):

    def __init__(self):
        self.check_manager = CheckManager()
        self.db = DataBaseManager()
        self.warning_manager = WarningManager()

    def loginCheck(self):
        username = self.line_user_name.text()
        password = self.line_password.text()

        correction_logindata = self.check_manager.checkCorrectionLoginData(username,password)
        if correction_logindata:
            pass
        else:
            self.warning_manager.showWarningBox('testtitle', 'incorrect login data')
            return None

        userData = self.db.getUserData(username=username)
        if userData:
            try:
                userData.password
            except:
                self.warning_manager.showWarningBox('testtitle', 'incorrect password')
                return None
        else:
            self.warning_manager.showWarningBox('testtitle', 'incorrect incorrect password')
            return None

        status = self.check_manager.checkLoginData(password=password,userData=userData)
        if status is not True:
            self.warning_manager.showWarningBox('testtitle', 'user is not exist')
            return None

        if userData.account_type == admin:
            self.adminMainWindow = QtWidgets.QMainWindow()
            self.ui = adminmainmenu.Ui_MainWindow()
            self.ui.setupUi(self.adminMainWindow)
            self.adminMainWindow.show()
            self.MainWindow.close()

        elif userData.account_type == user:
            self.userMainWindow = QtWidgets.QMainWindow()
            self.ui = usermainmenu.Ui_MainWindow()
            self.ui.setupUi(self.userMainWindow)
            self.userMainWindow.show()
            self.MainWindow.close()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(379, 295)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setMinimumSize(QtCore.QSize(60, 20))
        self.label.setMaximumSize(QtCore.QSize(60, 20))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.line_user_name = QtWidgets.QLineEdit(self.centralWidget)
        self.line_user_name.setObjectName("line_user_name")
        self.horizontalLayout_2.addWidget(self.line_user_name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setMaximumSize(QtCore.QSize(50, 20))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.line_password = QtWidgets.QLineEdit(self.centralWidget)
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setObjectName("line_password")
        self.horizontalLayout.addWidget(self.line_password)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.btn_login = QtWidgets.QPushButton(self.centralWidget)
        self.btn_login.setObjectName("btn_login")
        ############### Button Event ####################
        self.btn_login.clicked.connect(self.loginCheck)
        # ###############################################
        self.verticalLayout_2.addWidget(self.btn_login)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.btn_login.setText(_translate("MainWindow", "Zaloguj"))

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
