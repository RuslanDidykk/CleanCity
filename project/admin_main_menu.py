# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminmainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import QApplication, QComboBox

from project import adminpracownikmenu, admin_sprzet, admin_add_pojazd, admin_harmonogram, admin_pojazd, admin_profil, \
    admin_zgloszenia_pokaz


class Ui_MainWindow(object):


    def showPracownikWindow(self):
        self.adminPracownikMenu = QtWidgets.QMainWindow()
        self.ui = adminpracownikmenu.Ui_MainWindow()
        self.ui.setupUi(self.adminPracownikMenu)
        self.adminPracownikMenu.show()

    def showDodanieSprzetuWindow(self):
        self.adminDodanieSprzetu = QtWidgets.QMainWindow()
        self.ui = admin_sprzet.Ui_MainWindow()
        self.ui.setupUi(self.adminDodanieSprzetu)
        self.adminDodanieSprzetu.show()

    def showPojazdWindow(self):
        self.adminDodaniePojazdu = QtWidgets.QMainWindow()
        self.ui = admin_pojazd.Ui_MainWindow()
        self.ui.setupUi(self.adminDodaniePojazdu)
        self.adminDodaniePojazdu.show()

    def showHramonogramWindow(self):
        self.adminHramonogram = QtWidgets.QMainWindow()
        self.ui = admin_harmonogram.Ui_MainWindow()
        self.ui.setupUi(self.adminHramonogram)
        self.adminHramonogram.show()

    def showProfilWindow(self):
        self.adminProfil = QtWidgets.QMainWindow()
        self.ui = admin_profil.Ui_MainWindow()
        self.ui.setupUi(self.adminProfil)
        self.adminProfil.show()

    def showKlientWindow(self):
        self.adminPokazHarmonogram = QtWidgets.QMainWindow()
        self.ui = admin_zgloszenia_pokaz.Sheet()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 467)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_profil = QtWidgets.QPushButton(self.centralwidget)
        self.btn_profil.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_profil.setObjectName("btn_profil")

        ############### Button Event ####################
        self.btn_profil.clicked.connect(self.showProfilWindow)
        #################################################

        self.verticalLayout.addWidget(self.btn_profil)
        self.btn_komunikator = QtWidgets.QPushButton(self.centralwidget)
        self.btn_komunikator.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_komunikator.setObjectName("btn_komunikator")
        self.verticalLayout.addWidget(self.btn_komunikator)
        self.btn_klient = QtWidgets.QPushButton(self.centralwidget)
        self.btn_klient.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_klient.setObjectName("btn_klient")

        ############### Button Event ####################
        self.btn_klient.clicked.connect(self.showKlientWindow)
        #################################################

        self.verticalLayout.addWidget(self.btn_klient)
        self.btn_pracownik = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pracownik.setMinimumSize(QtCore.QSize(160, 50))
        self.btn_pracownik.setObjectName("btn_pracownik")
        self.verticalLayout.addWidget(self.btn_pracownik)
        ############### Button Event ####################
        self.btn_pracownik.clicked.connect(self.showPracownikWindow)
        #################################################

        self.btn_pojazdy = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pojazdy.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_pojazdy.setObjectName("btn_pojazdy")
        self.verticalLayout.addWidget(self.btn_pojazdy)
        ############### Button Event ####################
        self.btn_pojazdy.clicked.connect(self.showPojazdWindow)
        #################################################

        self.btn_sprzet = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sprzet.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_sprzet.setObjectName("btn_sprzet")
        self.verticalLayout.addWidget(self.btn_sprzet)
        ############### Button Event ####################
        self.btn_sprzet.clicked.connect(self.showDodanieSprzetuWindow)
        #################################################

        self.btn_karta = QtWidgets.QPushButton(self.centralwidget)
        self.btn_karta.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_karta.setObjectName("btn_karta")
        self.verticalLayout.addWidget(self.btn_karta)
        self.btn_ramonogram = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ramonogram.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_ramonogram.setObjectName("btn_ramonogram")
        self.verticalLayout.addWidget(self.btn_ramonogram)
        ############### Button Event ####################
        self.btn_ramonogram.clicked.connect(self.showHramonogramWindow)
        #################################################

        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Admin"))
        self.btn_profil.setText(_translate("MainWindow", "Profil"))
        self.btn_komunikator.setText(_translate("MainWindow", "Komunikator"))
        self.btn_klient.setText(_translate("MainWindow", "Klient"))
        self.btn_pracownik.setText(_translate("MainWindow", "Pracownik"))
        self.btn_pojazdy.setText(_translate("MainWindow", "Pojazdy"))
        self.btn_sprzet.setText(_translate("MainWindow", "Sprzet"))
        self.btn_karta.setText(_translate("MainWindow", "Mapa"))
        self.btn_ramonogram.setText(_translate("MainWindow", "Harmonogram"))

        ####################################
        # self.MainWindow = MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


