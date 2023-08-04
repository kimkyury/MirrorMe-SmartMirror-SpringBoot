from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    widget_List = []
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.main_page = QtWidgets.QWidget(self.centralwidget)
        self.widget_List.append(self.main_page)
        self.main_page.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.main_page.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_page.setObjectName("main_page")
    
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        # self.retranslateUi(MainWindow)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def retranslateUi(self, MainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))