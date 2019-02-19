import json, random, sys, subprocess,  time
from PySide2.QtWidgets import ( QMainWindow, QFrame, QLineEdit, QPushButton,
                                QApplication, QTextEdit, QLabel, QRadioButton, QAction, QLineEdit, QMessageBox,
                                QVBoxLayout, QListView, QComboBox, QCheckBox, QHBoxLayout, QDialog, QGroupBox, QWidget, QGridLayout
                                )
from PySide2.QtGui import QIcon, QStandardItemModel, QStandardItem
from PySide2.QtCore import QObject, Signal, Slot, QRunnable, QThread, QThreadPool
import configparser

WHITE = 'background-color: rgba(255, 255, 255, 1);'
GREEN = 'background-color: rgba(100, 215, 100, 1);'
BLUE  = 'background-color: rgba(200, 225, 240, 1);'
RED   = 'background-color: rgba(245, 205, 215, 1);'
"""
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

def get_profile():
    profile_output = subprocess.run("conan profile show default", shell=True, stdout=subprocess.PIPE).stdout # preferred python
    # windows
    #cfg = [i.decode() for i in profile_output.split(b'\r\n')]
    # mac
    cfg = [i.decode() for i in profile_output.split(b'\n')]
    #print(cfg)
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
    requirements = subprocess.run("conan info ~/dev/visualize/hps/ -n requires", shell=True, stdout=subprocess.PIPE).stdout # preferred python
    cfg = [i.decode().strip() for i in requirements.split(b'\n')]
    cfg.remove('') # what is really going on here?!?
    dependencies = [i for i in cfg[cfg.index("conanfile.py (HPS/6.0.0@None/None)") :]]
    # print(_reqs)
    # _deps = [i for i in cfg[_reqs.index("Requires:") :]]
    # real_requirements = []
    # remotes = set()
    #for idx,i in enumerate(_deps):
       # print(idx)
        #req = (i.split('@'))
        #print(i)
        #(name,version) = req[0].split('/')
        #(remote,channel) = req[1].split('/')
        #real_requirements.append({"name":name, "remote":remote, "version": version, "channel":channel})
        #remotes.add(remote)
    #print(_reqs.index("Requires:"))
    #print(cfg.index("conanfile.py (HPS/6.0.0@None/None)"))
    return dependencies

    requirements = subprocess.run("conan info ~/dev/visualize/hps/ -n requires", shell=True, stdout=subprocess.PIPE).stdout # preferred python

def get_options():
    options = subprocess.run("conan inspect ~/dev/visualize/hps/", shell=True, stdout=subprocess.PIPE).stdout # preferred python
    cfg = [i.decode().strip() for i in options.split(b'\n')]
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

class SettingsBox(QGroupBox):
    def __init__(self, label):
        super(SettingsBox, self).__init__(label)
        self.layout = QVBoxLayout(self)

class RecipeBox(QGroupBox):
    def __init__(self, label):
        super(RecipeBox, self).__init__(label)
        self.layout = QHBoxLayout(self)

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

    # def __del__(self):
    #     print self.id, 'died'

    def init_ui(self):
        self.button = PButton("Generate...")
        #settings = get_conan_config() # should be a tree?

        #h_box.addStretch()
        self.recipeBox = RecipeBox("HPS")
        self.settings = SettingsBox("Settings")
        #self.lab = RLabel("huh")
        self.layout.addWidget(self.recipeBox)
#        self.layout.addWidget(self.lab)
        self.options = OptionsBox("Options")
        self.deps = DepsBox("Dependencies")
        self.recipeBox.layout.addWidget(self.settings)
        self.recipeBox.layout.addWidget(self.deps)
        self.recipeBox.layout.addWidget(self.options)

        for k,v  in self.settings_dict.items():
            self.settings.layout.addWidget(QLabel("%s : %s" % (k,v)))

        for option  in self.options_list:
            self.options.layout.addWidget(QLabel("%s" % option))

        #self.recipeBox.layout.addWidget(self.lab)

        self.layout.addWidget(self.button)

        #self.setLayout(v_box)
        self.setWindowTitle("pyncone")

        self.button.clicked.connect(self.button_click)
        self.show()

    def button_click(self):
        #self.lab.setText(pr)
        self.options.layout.addWidget(QLabel("poop"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_res = app.desktop().screenGeometry()
    width, height = screen_res.width(), screen_res.height()
    main_window = MainWindow()
    if sys.platform == 'darwin':
        main_window.resize(width/2, height/2)
    else:
        main_window.resize(width/4, height/4)
    # thread = AThread()

    main_window.show()
    # thread.finished.connect(main_window.destroyed)
    # thread.start()
    sys.exit(app.exec_())
