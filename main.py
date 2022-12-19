#Version 1 : Setting everything up in the global scope

"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first MainWindow App!")

button = QPushButton()
button.setText("Drücken")

window.setCentralWidget(button)

window.show()
app.exec()

"""
#Version Seting up a separate class

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class Buttonholder(QMainWindow)
    def __init__(self):
        super().__init__()