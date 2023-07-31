from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineSettings


class window(QtWidgets.QWidget):
    def __init__(self, parent=QtWidgets.QWidget):
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled,True)
        super(window,self).__init__(parent)

        self.webview=QtWebEngineWidgets.QWebEngineView(self)
        self.webview.setUrl(QUrl("https://edu.ssafy.com/"))
        self.webview.setGeometry(0,0,1920,1080)
        self.show() 

    # @pyqtSlot(str)
    # def setVidUrl(self, url):
    #     self.vidUrl = url+"?autoplay=1"
    #     print('url:',url)
    #     self.webview.setUrl(QUrl(self.vidUrl))