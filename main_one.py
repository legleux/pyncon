import configparser, json, random, os, subprocess, sys, time
from PySide2.QtWidgets import ( QAction, QApplication, QCheckBox, QComboBox, QDialog,
                                QFrame, QGridLayout, QGroupBox, QHBoxLayout, QLabel,
                                QLineEdit, QLineEdit, QListView, QMainWindow, QMessageBox,
                                QPushButton, QRadioButton, QTextEdit, QVBoxLayout, QWidget
                              )
from PySide2.QtGui import QIcon, QStandardItem, QStandardItemModel
from PySide2.QtCore import QObject, QRunnable, Qt, QThread, QThreadPool, Signal, Slot

WHITE = 'background-color: rgba(255, 255, 255, 1);'
GREEN = 'background-color: rgba(100, 215, 100, 1);'
BLUE  = 'background-color: rgba(200, 225, 240, 1);'
RED   = 'background-color: rgba(245, 205, 215, 1);'
"""
Textbox for where Project lives
While parsing conan config, show user spinny ball in window
While generating, pop up window saying as much
Find profiles? Install Profiles?
Should use the real conans python modules?
---------
Tabs
___________
|recipe| dependency graph|
recipe:
    recipe info
dependency graph:
    button for internal vs external
"""
""""
while the app is running the button fires the signal
to a slot in the labels
    button name "generating"
    method to run conan

"""
USER_OPTIONS = {}
RECIPE_DIR = sys.argv[1]
BUILD_DIR = os.path.join(RECIPE_DIR, "build")

if sys.platform == 'win32':
    new_line = b'\r\n'
else:
    new_line = b'\n'

def get_profile():
    profile_output = subprocess.run("conan profile show default", shell=True, stdout=subprocess.PIPE).stdout # preferred python
    cfg = [i.decode() for i in profile_output.split(new_line)]
    cfg.remove('') # what is really going on here?!?
    return "\n".join(cfg[1:])

def get_settings():
    cfg = get_conan_config()
    return cfg._sections['settings']

def get_options():
    return get_conan_config()._sections['options']

def get_recipe_version():
    pass #TODO:

def get_dependencies():
    requirements = subprocess.run("conan info %s -n requires" % RECIPE_DIR, shell=True, stdout=subprocess.PIPE).stdout # preferred python
    cfg = [i.decode().strip() for i in requirements.split(new_line)]
    cfg.remove('') # what is really going on here?!?
    dependencies = [i for i in cfg[cfg.index("conanfile.py (HPS/6.0.0@None/None)") + 2 :]]
    return dependencies

def get_options():
    options = subprocess.run("conan inspect %s" % RECIPE_DIR, shell=True, stdout=subprocess.PIPE).stdout # preferred python
    cfg = [i.decode().strip() for i in options.split(new_line)]
    cfg.remove('') # what is really going on here?!?
    return [i for i in cfg[cfg.index("default_options:") + 1:]]

def get_conan_config():
    """
    make this take options or settings parameters and computed profile by default
    """
    pr = get_profile()
    config = configparser.ConfigParser(allow_no_value=True)
    config.read_string(pr)
    return config

def get_git_rev(N):
    return(subprocess.check_output('git --git-dir="C:\\Users\\emel\\dev\\visualize\\.git" rev-parse HEAD~%s' % N).decode("utf-8"))


# class AThread(QThread):

#     def run(self):
#         while True:
#             time.sleep(1)
#             print(get_git_rev(random.randrange(10)))


class Recipe(QStandardItemModel):
    def __init__(self):
        super(Recipe, self).__init__()

class RLabel(QLabel):
    def __init__(self, label):
        super(RLabel, self).__init__(label)
        self.setText(label)

class PButton(QPushButton):
    def __init__(self, label):
        super(PButton, self).__init__()
        self.setText(label)
        #self.setStyleSheet(WHITE)

class RecipeBox(QGroupBox):
    def __init__(self, label):
        super(RecipeBox, self).__init__(label)
        self.layout = QHBoxLayout(self)
class SettingsBox(QGroupBox):
    def __init__(self, label):
        super(SettingsBox, self).__init__(label)
        self.layout = QVBoxLayout(self)

class OptionsBox(QGroupBox):
    def __init__(self, label):
        super(OptionsBox, self).__init__(label)
        self.layout = QVBoxLayout(self)

class DepsBox(QGroupBox):
    def __init__(self, label):
        super(DepsBox, self).__init__(label)
        self.layout = QVBoxLayout(self)
        for i in get_dependencies():
           # l = " : ".join((i["name"],i["version"]))
            self.layout.addWidget(QLabel(i))

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        #self.setStyleSheet(GREEN)
        self.layout = QVBoxLayout(self)
        self.settings_dict = get_settings()
        self.options_list = get_options()

        self.init_ui()

    def init_ui(self):
        self.button = PButton("Generate...")
        #settings = get_conan_config() # should be a tree?
        self.recipeBox = RecipeBox("HPS")
        self.settings = SettingsBox("Settings")
        self.layout.addWidget(self.recipeBox)
        self.options = OptionsBox("Options")
        self.deps = DepsBox("Dependencies")
        self.recipeBox.layout.addWidget(self.settings)
        self.recipeBox.layout.addWidget(self.deps)
        self.recipeBox.layout.addWidget(self.options)

        for k,v  in self.settings_dict.items():
            self.settings.layout.addWidget(QLabel("%s : %s" % (k,v)))

        option_list_view = QListView()
        self.options_model = QStandardItemModel(option_list_view)
        for item in self.options_list:
            #TODO: Clean this up and get it out of ui init before it gets out of hand
            opt = item.split(":")
            v = opt.pop().strip()
            k = ":".join(opt)
            self.individual_option = QStandardItem(k)
            self.individual_option.setCheckable(True)
            self.individual_option.setEditable(False)
            if v == "True":
                self.individual_option.setCheckState(Qt.Checked)
            self.options_model.appendRow(self.individual_option)
        option_list_view.setModel(self.options_model)
        option_list_view.setAlternatingRowColors(True)
        self.options.layout.addWidget(option_list_view)

        self.layout.addWidget(self.button)
        self.setWindowTitle("PynCon")
        self.button.clicked.connect(self.button_click)
        self.show()

    def button_click(self):
        self.options.layout.addWidget(QLabel("poop"))
        for index in range(self.options_model.rowCount()):
            item = self.options_model.item(index)
            if item.isCheckable() and item.checkState() == Qt.Checked:
                USER_OPTIONS.update({item.text(): "True"})
            else:
                USER_OPTIONS.update({item.text(): "False"})

        conan_command(USER_OPTIONS)
                #print("item: %s" % item.text())
                #item.setCheckState(QtCore.Qt.Checked)

def conan_command(options):
    cc = ["conan", "install", BUILD_DIR]
    print("Calling conan with options:\n")
    clo = ["-o %s=%s" % opt for opt in USER_OPTIONS.items()]
    for option in clo:
        cc.append(option)
    print(cc)

if __name__ == '__main__':
    """
    Before we start, traverse up dirs until find a conanfile to use
    if we don't find one, just set the text box empty. (maybe this is overkill)
    """

    app = QApplication(sys.argv)
    screen_res = app.desktop().screenGeometry()
    width, height = screen_res.width(), screen_res.height()
    main_window = MainWindow()
    # TODO: figure out how to set window size properly?
    # if sys.platform == 'darwin':
    #     main_window.resize(width/2, height/2)
    # else:
    #     main_window.resize(width/4, height/4)
    # thread = AThread()

    main_window.show()
    # thread.finished.connect(main_window.destroyed)
    # thread.start()
    sys.exit(app.exec_())
