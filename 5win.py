from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from instr import *

class fifth_win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(text3_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.outro = QLabel(text4_outro)
        self.buttonn = QPushButton(text5_button)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.outro)
        self.layout.addWidget(self.buttonn)
        self.setLayout(self.layout)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
app = QApplication([])
mw = fifth_win()
app.exec_()
