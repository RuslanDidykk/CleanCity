# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usermainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from project import klient_zgloszenia_add


class Ui_MainWindow(object):

    def __init__(self, user_name):
        self.USER_NAME = user_name

    def showDodanieWindow(self):
        self.adminDodanieSprzetu = QtWidgets.QMainWindow()
        self.ui = klient_zgloszenia_add.Ui_MainWindow(self.USER_NAME)
        self.ui.setupUi(self.adminDodanieSprzetu)
        self.adminDodanieSprzetu.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(317, 268)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(130, 30))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.btn_zgloszenie = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zgloszenie.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_zgloszenie.setObjectName("pushButton_3")

        ############### Button Event ####################
        self.btn_zgloszenie.clicked.connect(self.showDodanieWindow)
        #################################################

        self.verticalLayout.addWidget(self.btn_zgloszenie)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pracownik"))
        self.label.setText(_translate("MainWindow", "Profil pracownika"))
        self.pushButton.setText(_translate("MainWindow", "Profil"))
        self.btn_zgloszenie.setText(_translate("MainWindow", "Zgloszenie"))
        self.pushButton_2.setText(_translate("MainWindow", "Harmonogram"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

