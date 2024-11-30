import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QTableWidget, QApplication, QTableWidgetItem


class MainWind(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        # self.tableWidget.itemChanged.connect(self.updateresult)
        self.updateresult()

    def updateresult(self):
        cur = self.con.cursor()
        result = cur.execute('SELECT * FROM Coffee').fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWind()
    ex.show()
    sys.exit(app.exec())