import sys
from PySide2.QtWidgets import QSlider, QApplication, QMainWindow, QDialog, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from button import PButton
from text import Label
from form import Ui_MainWindow
from conan import call_conan
import sys

from PySide2.QtGui import QIcon, QStandardItem, QStandardItemModel
from PySide2.QtCore import QObject, QRunnable, Qt, QThread, QThreadPool, Signal, Slot

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

    @Slot(str)
    def cs(self):
        print("x")
        self.lineEdit.setPlaceholderText("gnuh")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    options_model = QStandardItemModel(w.listView)
    individual_option = QStandardItem("butts")
    options_model.appendRow(individual_option)

    w.pushButton.clicked.connect(w.cs)
    w.pushButton.clicked.connect(call_conan)

    w.verticalLayout.addWidget(QPushButton("wee!"))
    w.verticalLayout.addWidget(Label("An Label"))
    w.show()
    sys.exit(app.exec_())