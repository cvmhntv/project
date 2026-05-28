from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from instr import *

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
        self.answer31 = QRadioButton(answer3_1)
        self.answer32 = QRadioButton(answer3_2)
        self.answer33 = QRadioButton(answer3_3)
        self.answer34 = QRadioButton(answer3_4)
        self.v_line1 = QHBoxLayout()
        self.v_line2 = QHBoxLayout()
        self.v_line3 = QHBoxLayout()
        self.v_line1.addWidget(question33, alignment = Qt.AlignCenter)
        self.v_line2.addWidget(answer31, alignment = Qt.AlignCenter)
        self.v_line2.addWidget(answer32, alignment = Qt.AlignCenter)
        self.v_line3.addWidget(answer33, alignment = Qt.AlignCenter)
        self.v_line3.addWidget(answer34, alignment = Qt.AlignCenter)
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
        answer21.clicked.connect(show_lose)
        answer22.clicked.connect(show_lose)
        answer23.clicked.connect(show_lose)
        answer24.clicked.connect(show_win) 

app = QApplication([])
mw = fourth_win()
app.exec_()
