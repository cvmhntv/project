from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                             QHBoxLayout, QPushButton, QRadioButton, QMessageBox)
from instr import *
from win4 import fourth_win

class third_win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(text3_title)
        self.resize(win_width, win_height)
    def initUI(self):
        self.question22 = QLabel(question2)
        self.question22.setWordWrap(True)
        self.answer21 = QRadioButton(answer2_1)
        self.answer22 = QRadioButton(answer2_2)
        self.answer23 = QRadioButton(answer2_3)
        self.answer24 = QRadioButton(answer2_4)
        self.button_next = QPushButton('Далее')
        self.v_line1 = QHBoxLayout()
        self.v_line2 = QHBoxLayout()
        self.v_line3 = QHBoxLayout()
        self.v_line1.addWidget(self.question22, alignment=Qt.AlignCenter)
        self.v_line2.addWidget(self.answer21, alignment=Qt.AlignCenter)
        self.v_line2.addWidget(self.answer22, alignment=Qt.AlignCenter)
        self.v_line3.addWidget(self.answer23, alignment=Qt.AlignCenter)
        self.v_line3.addWidget(self.answer24, alignment=Qt.AlignCenter)
        self.layout_main = QVBoxLayout()
        self.layout_main.addLayout(self.v_line1)
        self.layout_main.addLayout(self.v_line2)
        self.layout_main.addLayout(self.v_line3)
        self.layout_main.addWidget(self.button_next)
        self.setLayout(self.layout_main)
    def show_win(self):
        self.win = QMessageBox()
        self.win.setText('Верно')
        self.win.exec_()
    def show_lose(self):
        self.lose = QMessageBox()
        self.lose.setText(f'Неверно\nПравильный ответ: {answer2_2}')
        self.lose.exec_()
    def connects(self):
        self.answer21.clicked.connect(self.show_lose)
        self.answer22.clicked.connect(self.show_win)
        self.answer23.clicked.connect(self.show_lose)
        self.answer24.clicked.connect(self.show_lose)
        self.button_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = fourth_win()
