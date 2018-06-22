# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminsprzet.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

from project import admin_add_harmonogram, harmonogram, admin_harmonogram_usun


class Ui_MainWindow(object):

    def showDodanieSprzetuWindow(self):
        self.adminDodanieHarmonogramu = QtWidgets.QMainWindow()
        self.ui = admin_add_harmonogram.Ui_MainWindow()
        self.ui.setupUi(self.adminDodanieHarmonogramu)
        self.adminDodanieHarmonogramu.show()

    def showUsunHarmongram(self):
        self.adminUsunHarmonogramu = QtWidgets.QMainWindow()
        self.ui = admin_harmonogram_usun.Ui_MainWindow()
        self.ui.setupUi(self.adminUsunHarmonogramu)
        self.adminUsunHarmonogramu.show()

    def showHarmonogram(self):
        self.adminPokazHarmonogram = QtWidgets.QMainWindow()
        self.ui = harmonogram.Sheet()

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

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        ############### Button Event ####################
        self.pushButton_3.clicked.connect(self.showHarmonogram)
        #################################################
        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_4.setObjectName("pushButton_3")
        ############### Button Event ####################
        self.pushButton_4.clicked.connect(self.showUsunHarmongram)
        #################################################
        self.verticalLayout.addWidget(self.pushButton_4)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Hramonogram"))
        self.pushButton.setText(_translate("MainWindow", "Dodaj wyjazd"))
        self.pushButton_3.setText(_translate("MainWindow", "Pokaz harmonogram"))
        self.pushButton_4.setText(_translate("MainWindow", "Usun harmonogram"))

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

