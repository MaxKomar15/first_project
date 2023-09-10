from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout, QMessageBox, QLabel, QVBoxLayout


app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle("Визначник переможця")
main_win.resize(400, 200)

question = QLabel("Коли народився Тарас Шевченко ?")
btn1 = QRadioButton("1814р")
btn2 = QRadioButton("1813р")
btn3 = QRadioButton("1812р")
btn4 = QRadioButton("1811р")

vline = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()

vline.addWidget(question, allignment=Qt.Alignment)
row1.addWidget(btn1, allignment=Qt.Alignment)
row1.addWidget(btn2, allignment=Qt.Alignment)
row2.addWidget(btn3, allignment=Qt.Alignment)
row2.addWidget(btn4, allignment=Qt.Alignment)

vline.addLayout(row1)
vline.addLayout(row2)

main_win.setLayout(vline)

def show_win():
    message = QMessageBox()
    message.exec_()


btn3.clicked.connected(show_win)


main_win.show()
app.exec_()