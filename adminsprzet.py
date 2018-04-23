# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminsprzet.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import admindodaniesprzetu
import adminsprzetzmienilosc

class Ui_MainWindow(object):


    def showDodanieSprzetuWindow(self):
        self.adminDodanieSprzetu = QtWidgets.QMainWindow()
        self.ui = admindodaniesprzetu.Ui_MainWindow()
        self.ui.setupUi(self.adminDodanieSprzetu)
        self.adminDodanieSprzetu.show()
        self.MainWindow.close()

    def showZmienIloscWindow(self):
        self.adminZmienIlosc= QtWidgets.QMainWindow()
        self.ui = adminsprzetzmienilosc.Ui_MainWindow()
        self.ui.setupUi(self.adminZmienIlosc)
        self.adminZmienIlosc.show()
        self.MainWindow.close()


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
        self.pushButton.clicked.connect(self.showDodanieSprzetuWindow)
        #################################################
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        ############### Button Event ####################
        self.pushButton_2.clicked.connect(self.showZmienIloscWindow)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Dodaj sprzet"))
        self.pushButton_2.setText(_translate("MainWindow", "Zmien Ilosc"))

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

