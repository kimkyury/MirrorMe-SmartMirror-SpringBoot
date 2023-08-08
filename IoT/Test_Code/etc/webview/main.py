import sys
import webview
from PyQt5 import QtWidgets
import mainpage
import webview

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = webview.Ui_MainWindow()
    ui.setupUi(MainWindow)

    mainpage.window(ui.main_page)
    MainWindow.show()
    # MainWindow.showMaximized()
    sys.exit(app.exec_())