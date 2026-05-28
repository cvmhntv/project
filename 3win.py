from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

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
        self.move(win_x, win_y)
    def initUI(self):
        self.question22 = QLabel(question2)
        self.answer21 = QRadioButton(answer2_1)
        self.answer22 = QRadioButton(answer2_2)
        self.answer23 = QRadioButton(answer2_3)
        self.answer24 = QRadioButton(answer2_4)
        self.v_line1 = QHBoxLayout()
        self.v_line2 = QHBoxLayout()
        self.v_line3 = QHBoxLayout()
        self.v_line1.addWidget(question22, alignment = Qt.AlignCenter)
        self.v_line2.addWidget(answer21, alignment = Qt.AlignCenter)
        self.v_line2.addWidget(answer22, alignment = Qt.AlignCenter)
        self.v_line3.addWidget(answer23, alignment = Qt.AlignCenter)
        self.v_line3.addWidget(answer24, alignment = Qt.AlignCenter)
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
        answer22.clicked.connect(show_win)
        answer23.clicked.connect(show_lose)
        answer24.clicked.connect(show_lose)

app = QApplication([])
mw = third_win()
app.exec_()
