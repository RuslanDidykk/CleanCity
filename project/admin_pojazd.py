# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminsprzet.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

from project import admin_add_pojazd, admin_pojazd_status


class Ui_MainWindow(object):

    def showPojazdDodaj(self):
        self.adminDodaniePojazdu = QtWidgets.QMainWindow()
        self.ui = admin_add_pojazd.Ui_MainWindow()
        self.ui.setupUi(self.adminDodaniePojazdu)
        self.adminDodaniePojazdu.show()
        # self.MainWindow.close()

    def showZmienStatus(self):
        self.adminPojazdSatus = QtWidgets.QMainWindow()
        self.ui = admin_pojazd_status.Ui_MainWindow()
        self.ui.setupUi(self.adminPojazdSatus)
        self.adminPojazdSatus.show()
        # self.MainWindow.close()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 308)
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
        self.pushButton.clicked.connect(self.showPojazdDodaj)
        #################################################
        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        ############### Button Event ####################
        self.pushButton_2.clicked.connect(self.showZmienStatus)
        #################################################
        self.verticalLayout.addWidget(self.pushButton_2)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Pojazd"))
        self.pushButton.setText(_translate("MainWindow", "Dodaj pojazd"))
        self.pushButton_2.setText(_translate("MainWindow", "Zmien status"))

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

