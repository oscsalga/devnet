## using forms from ui

from datetime import datetime

from PyQt5 import QtWidgets, uic
import sys
import datetime

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('form.ui', self)
        self.show()

        self.pushButton1.clicked.connect(self.fecha)
        self.pushButton2.clicked.connect(self.mayusculas)

    def mayusculas(self):
        self.textEdit.setPlainText(str(self.textEdit.toPlainText()).upper())
        self.textEdit.repaint()


    def fecha(self):
        self.label.setText(str(datetime.datetime.now()))
        self.label.repaint()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
