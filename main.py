# coding=utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore 

import sys
# Импортируем наш интерфейс из файла
from loginwindow import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # mainWindow = Ui_MainWindow()

        # Здесь прописываем событие нажатия на кнопку        
        # self.ui.btn_login.clicked.connect(self.loginCheck)
        # self.ui.pushButton.clicked.connect(self.MyFunction)
        # self.btn_login.clicked.connect(self.loginCheck)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку                  
    # def loginCheck(self):
    #    self.adminMainWindow = QtGui.Qadminmainpanel()
    #    self.ui = Ui_MainWindow()
    #    self.setupUi(self.adminmainpanel)
    #    self.adminmainpanel.show()



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())

