import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_Form

class ApplicationWindow(QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)


def main():
    app = QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
