import sys
import conan
from PySide2.QtCore import QObject, QRunnable, Qt, QThread, QThreadPool, Signal, Slot
from PySide2.QtWidgets import QSlider, QApplication, QMainWindow, QDialog, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PySide2.QtGui import QIcon, QStandardItem, QStandardItemModel
from mainWindow import Ui_MainWindow

## TODO: populate dependencies with tree view of everything!
RECIPE_DIR = "~/dev/visualize/hps/"

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

    @Slot(str)
    def cs(self):
        self.conanfilePathLineEdit.setPlaceholderText("gnuh")
    @Slot()
    def hs(self):
        print(self.conanfilePathLineEdit.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()

    options_model = QStandardItemModel(w.optionsListView)
    for option in conan.get_options():
        #TODO: Clean this up and get it out of ui init before it gets out of hand
        opt = option.split(":")
        value = opt.pop().strip()
        key = ":".join(opt)
        individual_option = QStandardItem(key)
        individual_option.setCheckable(True)
        individual_option.setEditable(False)
        if value == "True":
            individual_option.setCheckState(Qt.Checked)
        options_model.appendRow(individual_option)

    w.optionsListView.setModel(options_model)

    w.generatePushButton.clicked.connect(w.cs)
    w.conanfilePathLineEdit.returnPressed.connect(w.hs)
    w.show()
    sys.exit(app.exec_())