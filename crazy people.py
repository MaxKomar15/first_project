from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle("Визначник переможця")
main_win.resize(400, 250)

text =  QLabel("Натисність щоб дізнатись пропереможця")
result = QLabel("?")
btn = QPushButton("Згенерувати")

line = QVBoxLayout()
line.addWidget(text, alignment= Qt.AlignCenter)
line.addWidget(result, alignment= Qt.AlignCenter)
line.addWidget(btn , alignment= Qt.AlignCenter)


def random_winner():
    winner = randint (1, 100)
    result.setText(str(winner))

btn.clicked.connect(random_winner)


main_win.setLayout(line)
main_win.show()
app.exec_()