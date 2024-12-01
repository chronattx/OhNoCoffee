import sys
import sqlite3
import io

from PyQt6 import uic
from PyQt6.QtWidgets import QButtonGroup, QWidget, QTableWidget, QApplication, QTableWidgetItem

from interface import interface
from add_edit_interface import a


class MainWind(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ff = io.StringIO(interface)
        uic.loadUi(ff, self)
        self.con = sqlite3.connect('../coffee.sqlite')
        # self.tableWidget.itemChanged.connect(self.updateresult)
        self.updateresult()
        self.pushButton.clicked.connect(self.open_addedit)
        self.updateButton.clicked.connect(self.updateresult)

    def open_addedit(self):
        self.wid = AddEdit()
        self.wid.setCon(self.con)
        self.wid.show()

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


class AddEdit(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.gr1 = QButtonGroup()
        self.gr1.addButton(self.addBtn)
        self.gr1.addButton(self.changeBtn)
        self.addBtn.setChecked(True)
        self.grindBtn.setChecked(True)
        self.pushButton.clicked.connect(self.done)

    def setCon(self, con):
        self.con = con

    def done(self):
        if self.addBtn.isChecked():
            self.new()
        else:
            try:
                self.edit()
            except Exception as e:
                print(e)
        self.con.commit()

    def new(self):
        cur = self.con.cursor()
        i = len(cur.execute("SELECT * FROM Coffee").fetchall()) + 1
        i2 = 1 if self.grindBtn.isChecked() else 0
        t = (i, self.kindEdit.text(), self.gradeEdit.text(), i2, self.descriptionEdit.text(),
             self.priceEdit.value(), self.volumeEdit.value())
        cur.execute("""INSERT INTO Coffee VALUES(?, ?, ?, ?, ?, ?, ?)""", t)

    def edit(self):
        cur = self.con.cursor()
        i = self.idEdit.value()
        i2 = 1 if self.grindBtn.isChecked() else 0
        cur.execute("""UPDATE Coffee SET
        kind = ?, grade = ?, type = ?, description = ?, price = ?, volume = ?
        WHERE id = ?""",
                    (self.kindEdit.text(), self.gradeEdit.text(), i2,
                     self.descriptionEdit.text(), self.priceEdit.value(),
                     self.volumeEdit.value(), i))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWind()
    ex.show()
    sys.exit(app.exec())