import sys
from PyQt6 import QtWidgets
from PyQt6 import QtCore
import random
import json

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Vocabulary Helper')
        self.setStyleSheet('background:#FFFFFF')
        self.resize(600, 500)
        self.ui()

    def ui(self):
        # title
        self.title_label = QtWidgets.QLabel(self)
        self.title_label.move(90, 50)
        self.title_label.setText('Vocabulary Helper')
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet('font-size:50px; color:#000000')
        # start button
        self.start_btn = QtWidgets.QPushButton(self)
        self.start_btn.setText('START')
        self.start_btn.setGeometry(200, 300, 200, 100)
        self.start_btn.setStyleSheet('''
        QPushButton{
            border:1px solid #000;
            background:#a8a8a8;
        }
        QPushButton:hover{
            border:5px solid #000;
            background:#616161;
        }
        ''')
        self.start_btn.clicked.connect(self.game_start)
        # choice btn
        self.cbtn1 = QtWidgets.QPushButton(self)
        self.cbtn1.setGeometry(125, 300, 150, 100)
        self.cbtn1.setText('1')
        self.cbtn1.setStyleSheet('''
        QPushButton{
            border:1px solid #000;
            background:#a8a8a8;
            font-size:30px
        }
        QPushButton:hover{
            border:5px solid #000;
            background:#616161;
        }
        ''')
        self.cbtn2 = QtWidgets.QPushButton(self)
        self.cbtn2.setGeometry(325, 300, 150, 100)
        self.cbtn2.setText('2')
        self.cbtn2.setStyleSheet('''
        QPushButton{
            border:1px solid #000;
            background:#a8a8a8;
            font-size:30px
        }
        QPushButton:hover{
            border:5px solid #000;
            background:#616161;
            font-size:30px
        }
        ''')
        self.cbtn1.hide()
        self.cbtn2.hide()

    def game_start(self):
        self.start_btn.hide()
        self.voc_bank = open(r'vocabulary_helper\resource\level1.json', 'r', encoding='utf-8')
        self.data = json.load(self.voc_bank)
        self.voc_bank.close()
        self.count = random.randint(1, 1600)
        self.word = self.data[self.count]['word']
        self.ans = self.data[self.count]['definitions'][0]['text']
        self.title_label.setText(self.word)
        self.ans_pos = random.randint(0, 1)
        self.cbtn1.show()
        self.cbtn2.show()
        if self.ans_pos == 1:
            self.fake_ans = str(self.data[random.randint(0, 1600)]['definitions'][0]['text'])
            self.cbtn1.setText(str(self.ans))
            self.cbtn2.setText(self.fake_ans)
            self.cbtn1.clicked.connect(self.check_right)
            self.cbtn2.clicked.connect(self.check_fake)
        else:
            self.fake_ans = str(self.data[random.randint(0, 1600)]['definitions'][0]['text'])
            self.cbtn1.setText(self.fake_ans)
            self.cbtn2.setText(str(self.ans))
            self.cbtn1.clicked.connect(self.check_fake)
            self.cbtn2.clicked.connect(self.check_right)
    def check_fake(self):
        self.title_label.setText('NO')
    def check_right(self):
        self.title_label.setText('YES')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())