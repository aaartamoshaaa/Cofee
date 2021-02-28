from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic
import sys
import sqlite3


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()

        self.pushButton.clicked.connect(self.update_base)
        self.drawing = True
        self.initUI()
        self.update_base()

    def initUI(self):
        self.setWindowTitle('Кофе')
        self.show()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels([
            'ID',
            'Название',
            'Обжарка',
            'Тип',
            'Вкус',
            'Цена',
            'Объем'
        ])

    def update_base(self):
        self.info = self.cur.execute('SELECT * FROM coffee').fetchall()
        self.tableWidget.setRowCount(0)
        for i, lst in enumerate(self.info):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for s, item in enumerate(lst):
                self.tableWidget.setItem(i, s, QTableWidgetItem(str(item)))
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    sys.exit(app.exec_())
