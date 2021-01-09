from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import *
from DBConnection import *

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

