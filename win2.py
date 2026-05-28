from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                             QHBoxLayout, QPushButton, QRadioButton, QMessageBox)
from instr import *
from win3 import third_win
class second_win(QWidget):
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
        self.question11 = QLabel(question1)
        self.question11.setWordWrap(True)
        self.answer11 = QRadioButton(answer1_1)
        self.answer12 = QRadioButton(answer1_2)
        self.answer13 = QRadioButton(answer1_3)
        self.answer14 = QRadioButton(answer1_4)
        self.button_next = QPushButton('Далее')
        self.v_line1 = QHBoxLayout()
        self.v_line2 = QHBoxLayout()
        self.v_line3 = QHBoxLayout()
        self.v_line1.addWidget(self.question11, alignment=Qt.AlignCenter)
        self.v_line2.addWidget(self.answer11, alignment=Qt.AlignCenter)
        self.v_line2.addWidget(self.answer12, alignment=Qt.AlignCenter)
        self.v_line3.addWidget(self.answer13, alignment=Qt.AlignCenter)
        self.v_line3.addWidget(self.answer14, alignment=Qt.AlignCenter)
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
        self.answer11.clicked.connect(self.show_lose)
        self.answer12.clicked.connect(self.show_lose)
        self.answer13.clicked.connect(self.show_win)
        self.answer14.clicked.connect(self.show_lose)
        self.button_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = third_win()
