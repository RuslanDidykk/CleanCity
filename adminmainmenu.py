# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminmainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import admindodaniesprzetu
import adminpracownikmenu
import adminsprzet

class Ui_MainWindow(object):


    def showPracownikWindow(self):
        self.adminPracownikMenu = QtWidgets.QMainWindow()
        self.ui = adminpracownikmenu.Ui_MainWindow()
        self.ui.setupUi(self.adminPracownikMenu)
        self.adminPracownikMenu.show()

    def showDodanieSprzetuWindow(self):
        self.adminDodanieSprzetu = QtWidgets.QMainWindow()
        self.ui = adminsprzet.Ui_MainWindow()
        self.ui.setupUi(self.adminDodanieSprzetu)
        self.adminDodanieSprzetu.show()

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
        self.verticalLayout.addWidget(self.btn_profil)
        self.btn_komunikator = QtWidgets.QPushButton(self.centralwidget)
        self.btn_komunikator.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_komunikator.setObjectName("btn_komunikator")
        self.verticalLayout.addWidget(self.btn_komunikator)
        self.btn_klient = QtWidgets.QPushButton(self.centralwidget)
        self.btn_klient.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_klient.setObjectName("btn_klient")
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
        self.btn_karta.setText(_translate("MainWindow", "Karta"))
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