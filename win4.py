from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                             QHBoxLayout, QPushButton, QRadioButton, QMessageBox)
from instr import *
from win5 import fifth_win
class fourth_win(QWidget):
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
        self.question33 = QLabel(question3)
        self.question33.setWordWrap(True)
        self.answer31 = QRadioButton(answer3_1)
        self.answer32 = QRadioButton(answer3_2)
        self.answer33 = QRadioButton(answer3_3)
        self.answer34 = QRadioButton(answer3_4)
        self.button_next = QPushButton('Далее')
        self.v_line1 = QHBoxLayout()
        self.v_line2 = QHBoxLayout()
        self.v_line3 = QHBoxLayout()
        self.v_line1.addWidget(self.question33, alignment=Qt.AlignCenter)
        self.v_line2.addWidget(self.answer31, alignment=Qt.AlignCenter)
        self.v_line2.addWidget(self.answer32, alignment=Qt.AlignCenter)
        self.v_line3.addWidget(self.answer33, alignment=Qt.AlignCenter)
        self.v_line3.addWidget(self.answer34, alignment=Qt.AlignCenter)
        self.layout_main = QVBoxLayout()
        self.layout_main.addLayout(self.v_line1)
        self.layout_main.addLayout(self.v_line2)
        self.layout_main.addLayout(self.v_line3)
        self.layout_main.addWidget(self.button_next)
        self.setLayout(self.layout_main)
    def show_win(self):
        self.win = QMessageBox()
        self.win.setText('верно')
        self.win.exec_()
    def show_lose(self):
        self.lose = QMessageBox()
        self.lose.setText('неверно')
        self.lose.exec_()
    def connects(self):
        self.answer31.clicked.connect(self.show_lose)
        self.answer32.clicked.connect(self.show_lose)
        self.answer33.clicked.connect(self.show_lose)
        self.answer34.clicked.connect(self.show_win)
        self.button_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = fifth_win()
