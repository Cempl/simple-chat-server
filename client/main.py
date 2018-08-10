import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.button = QPushButton('SEND', self)
        self.textInput = QLineEdit(self)
        self.textView = QLineEdit(self)
        self.title = "Let's talk"
        self.left = 10
        self.top = 10
        self.width = 550
        self.height = 550
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Send button
        self.button.resize(75, 75)
        self.button.move(475, 480)
        self.button.clicked.connect(self.on_click)

        #Text input
        self.textInput.resize(470, 60)
        self.textInput.move(5, 485)

        # Text viewer
        self.textView.resize(540, 470)
        self.textView.move(5, 5)
        self.textView.setReadOnly(True)

        self.show()

    @pyqtSlot()
    def on_click(self):
        #TODO: implement "SEND" button functionality
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
