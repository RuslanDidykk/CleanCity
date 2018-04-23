# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminpracownikmenu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import adminRegistrationUser
import adminEditUser
import adminpracownikusun


class Ui_MainWindow(object):

    def showDodajWindow(self):
        self.adminRegistration = QtWidgets.QMainWindow()
        self.ui = adminRegistrationUser.Ui_MainWindow()
        self.ui.setupUi(self.adminRegistration)
        self.adminRegistration.show()
        self.MainWindow.close()

    def showEditWindow(self):
        self.adminEditUser = QtWidgets.QMainWindow()
        self.ui = adminEditUser.Ui_MainWindow()
        self.ui.setupUi(self.adminEditUser)
        self.adminEditUser.show()
        self.MainWindow.close()

    def showDeleteWindow(self):
        self.adminPracownikUsun = QtWidgets.QMainWindow()
        self.ui = adminpracownikusun.Ui_MainWindow()
        self.ui.setupUi(self.adminPracownikUsun)
        self.adminPracownikUsun.show()
        self.MainWindow.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(374, 238)
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
        self.pushButton.clicked.connect(self.showDodajWindow)
        #################################################
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        ############### Button Event ####################
        self.pushButton_3.clicked.connect(self.showEditWindow)
        #################################################
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        ############### Button Event ####################
        self.pushButton_4.clicked.connect(self.showDeleteWindow)
        #################################################
        self.verticalLayout.addWidget(self.pushButton_4)
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
        self.pushButton.setText(_translate("MainWindow", "Dodaj pracownika"))
        self.pushButton_3.setText(_translate("MainWindow", "Edytuj pracownika"))
        self.pushButton_2.setText(_translate("MainWindow", "Pokaż pracowników"))
        self.pushButton_4.setText(_translate("MainWindow", "Usuń Pracownika"))
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

