# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui',
# licensing of 'mainWindow.ui' applies.
#
# Created: Fri Feb 22 19:21:30 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.findConanfilePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.findConanfilePushButton.setObjectName("findConanfilePushButton")
        self.horizontalLayout.addWidget(self.findConanfilePushButton)
        self.conanfilePathLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.conanfilePathLineEdit.setObjectName("conanfilePathLineEdit")
        self.horizontalLayout.addWidget(self.conanfilePathLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.recipeVerticalLayout = QtWidgets.QVBoxLayout()
        self.recipeVerticalLayout.setObjectName("recipeVerticalLayout")
        self.staticConfig = QtWidgets.QWidget(self.centralwidget)
        self.staticConfig.setObjectName("staticConfig")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.staticConfig)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.settingsGroupBox = QtWidgets.QGroupBox(self.staticConfig)
        self.settingsGroupBox.setCheckable(False)
        self.settingsGroupBox.setObjectName("settingsGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.settingsGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.settingsListView = QtWidgets.QListView(self.settingsGroupBox)
        self.settingsListView.setToolTipDuration(4000)
        self.settingsListView.setObjectName("settingsListView")
        self.horizontalLayout_2.addWidget(self.settingsListView)
        self.horizontalLayout_3.addWidget(self.settingsGroupBox)
        self.dependenciesGroupBox = QtWidgets.QGroupBox(self.staticConfig)
        self.dependenciesGroupBox.setObjectName("dependenciesGroupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.dependenciesGroupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.dependenciesListView = QtWidgets.QListView(self.dependenciesGroupBox)
        self.dependenciesListView.setObjectName("dependenciesListView")
        self.horizontalLayout_5.addWidget(self.dependenciesListView)
        self.horizontalLayout_3.addWidget(self.dependenciesGroupBox)
        self.recipeVerticalLayout.addWidget(self.staticConfig)
        self.optionsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.optionsGroupBox.setObjectName("optionsGroupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.optionsGroupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.optionsListView = QtWidgets.QListView(self.optionsGroupBox)
        self.optionsListView.setObjectName("optionsListView")
        self.horizontalLayout_4.addWidget(self.optionsListView)
        self.recipeVerticalLayout.addWidget(self.optionsGroupBox)
        self.verticalLayout.addLayout(self.recipeVerticalLayout)
        self.generatePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.generatePushButton.setToolTip("")
        self.generatePushButton.setStatusTip("")
        self.generatePushButton.setWhatsThis("")
        self.generatePushButton.setObjectName("generatePushButton")
        self.verticalLayout.addWidget(self.generatePushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.optionsListView, self.settingsListView)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "PynCone", None, -1))
        self.findConanfilePushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Find conanfile.py", None, -1))
        self.conanfilePathLineEdit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "/path/to/conanfile", None, -1))
        self.settingsGroupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.settingsListView.setToolTip(QtWidgets.QApplication.translate("MainWindow", "butts muthafucka!!!!!!!!", None, -1))
        self.dependenciesGroupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Dependencies", None, -1))
        self.optionsGroupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Options", None, -1))
        self.generatePushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Generate", None, -1))

