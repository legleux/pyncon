import sys
import conan
from PySide2.QtCore import QObject, QRunnable, Qt, QThread, QThreadPool, Signal, Slot
from PySide2.QtWidgets import QSlider, QApplication, QMainWindow, QDialog, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PySide2.QtGui import QIcon, QStandardItem, QStandardItemModel
from mainWindow import Ui_MainWindow

## TODO: populate dependencies with tree view of everything!

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
    @Slot()
    def update_profile_lineEdit(self): # TODO: maybe make this a list from the available profiles
        fileName = QFileDialog.getOpenFileName(self, "Load Profile",
                                       "/Users/emel/.conan/profiles/",
                                       "Profile (*)")
        print(fileName[0])
        self.profileLineEdit.setText(fileName[0])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()

    options_model = QStandardItemModel(w.optionsListView)
    for option, value in conan.get_options().items():
        individual_option = QStandardItem(option)
        individual_option.setCheckable(True)
        individual_option.setEditable(False)
        if value == "True":
            individual_option.setCheckState(Qt.Checked)
        options_model.appendRow(individual_option)
    w.optionsListView.setModel(options_model)

    settings_model = QStandardItemModel(w.settingsTreeView)
    #settings_model.
    root_node = QStandardItem("poop")
    #for i in range(3):
    #    node = QStandardItem("another")
    c = conan.get_settings()
    for k,v in list(enumerate(c['settings'].items())):
        print(k,v)
        setting = QStandardItem(v[0])
        value =  QStandardItem(v[1])

        setting.setChild(0,value)
        settings_model.appendRow(setting)
        print(setting.text())
#         if( k != 0):
#             print("split")
#             print(setting.text().split(".") or setting.text().split("_"))
#             if setting.text().startswith(last_setting):
# #                setting.appendRow(value)
#                 print("set child of: "+str(k-1)+ " " + last_setting)
        last_setting = setting.text()
        print("last is " +  last_setting)

    w.settingsTreeView.setModel(settings_model)
    w.generatePushButton.clicked.connect(w.cs)
    w.profilePushButton.clicked.connect(w.update_profile_lineEdit)


    w.generatePushButton.clicked.connect(w.cs)
    w.conanfilePathLineEdit.returnPressed.connect(w.hs)
    w.show()
    sys.exit(app.exec_())