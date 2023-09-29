#   Quote+...

from polygon import RESTClient


client = RESTClient(api_key="4pgWU0VnA3pVrog6dpqVnkSz9Y0RWa56")


import os
import subprocess
import sys
import time
import serial

basedir = os.path.dirname(__file__)

global ticker_holder
ticker_holder = "NULL"


#   Necessary components...

from pathlib import Path

from PyQt6.QtCore import QObject, QRunnable, QSize, Qt, QThreadPool
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
                             QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget)


#   Qt app...

app = QApplication([])


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        logo = QLabel("Broker's App")
        logo.setPixmap(QPixmap(os.path.join(basedir, "_header.png")))
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)


#   User input

        global quote_query
        quote_query = QLineEdit()
        quote_query.setPlaceholderText("AAPL, F...")
        quote_query.textChanged.connect(self.decouple_quote)        


#   Controls

        global launchBtn
        launchBtn = QPushButton("Launch")
        launchBtn.setFixedHeight(30)
        launchBtn.clicked.connect(self.get_results)

        
        resetBtn = QPushButton()
        resetBtn.setIcon(QIcon(os.path.join(basedir, "resetIcon.png")))
        resetBtn.setFixedSize(30, 30)
        resetBtn.clicked.connect(reset)    


#   Results

        global query_results
        query_results = QLabel("")
        query_results.setFixedHeight(250)
        query_results.setFixedWidth(1000)
        query_results.setObjectName("quoteNFO")


#   Layout

        layout = QVBoxLayout()
        controls = QHBoxLayout()


    #   Logo

        layout.addWidget(logo)
        layout.addWidget(quote_query)
    
    
    #   Controls

        layout.addLayout(controls)
        controls.addWidget(launchBtn)
        controls.addWidget(resetBtn)


    #   Results

        layout.addWidget(query_results)


#   App Container

        app_container = QWidget()
        app_container.setLayout(layout)

        self.setCentralWidget(app_container)


#   Helpers...

# Get Last Quote from Polygon.io

    def decouple_quote(self, text):
        ticker_holder = text
        if ticker_holder != "NULL":
            query_results.setText("Quote : " + ticker_holder)
            query_results.setText("Quote : " + ticker_holder)
        else:
            pass
        

    def get_results(self, quote_query):
        if ticker_holder != "NULL":
            quote = client.get_last_quote(ticker = ticker_holder)
            query_results.setText("quote")
        else:
            query_results.setText("Need a quote?")


def reset():
    quote_query.setText("")
    query_results.setText("")



#   Launch Quote+ App

window = MainWindow()
window.show()


app.setStyleSheet(Path(os.path.join(basedir, 'Quote+.qss')).read_text())
app.exec()


#   Quote+...