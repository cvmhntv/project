from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from instr import *

class first_win(QWidget):
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
        self.intro = QLabel(text1_intro)
        self.button = QPushButton(text2_button)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.intro)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = second_win()

app = QApplication([])
mw = MainWin()
app.exec_()
