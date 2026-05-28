from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from instr import *

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
        self.answer11 = QRadioButton(answer1_1)
        self.answer12 = QRadioButton(answer1_2)
        self.answer13 = QRadioButton(answer1_3)
        self.answer14 = QRadioButton(answer1_4)
        self.v_line1 = QHBoxLayout()
        self.v_line2 = QHBoxLayout()
        self.v_line3 = QHBoxLayout()
        self.v_line1.addWidget(question11, alignment = Qt.AlignCenter)
        self.v_line2.addWidget(answer11, alignment = Qt.AlignCenter)
        self.v_line2.addWidget(answer12, alignment = Qt.AlignCenter)
        self.v_line3.addWidget(answer13, alignment = Qt.AlignCenter)
        self.v_line3.addWidget(answer14, alignment = Qt.AlignCenter)
        self.layout_main = QVBoxLayout()
        self.layout_main.addLayout(v_line1)
        self.layout_main.addLayout(v_line2)
        self.layout_main.addLayout(v_line3)
        self.window.setLayout(layout_main)
    def show_win():
        self.win = QMessageBox()
        self.win.setText('верно')
        self.win.exec_()
    def show_lose():
        self.lose = QMessageBox()
        self.lose.setText('неверно')
        self.lose.exec_()
    def connects(self):
        answer11.clicked.connect(show_lose)
        answer12.clicked.connect(show_lose)
        answer13.clicked.connect(show_win)
        answer14.clicked.connect(show_lose)

app = QApplication([])
mw = second_win()
app.exec_()
