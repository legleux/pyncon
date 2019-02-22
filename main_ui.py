# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyncon.ui',
# licensing of 'pyncon.ui' applies.
#
# Created: Thu Feb 21 21:19:31 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QWidget

class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(507, 406)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainVerticalLayout = QtWidgets.QVBoxLayout()
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")
        self.conanfileLineEdit = QtWidgets.QLineEdit(Form)
        self.conanfileLineEdit.setObjectName("conanfileLineEdit")
        self.mainVerticalLayout.addWidget(self.conanfileLineEdit)
        self.recipeGroupBox = QtWidgets.QGroupBox(Form)
        self.recipeGroupBox.setObjectName("recipeGroupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.recipeGroupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.settingsGroupBox = QtWidgets.QGroupBox(self.recipeGroupBox)
        self.settingsGroupBox.setObjectName("settingsGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.settingsGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.settingsListView = QtWidgets.QListView(self.settingsGroupBox)
        self.settingsListView.setObjectName("settingsListView")
        self.verticalLayout_2.addWidget(self.settingsListView)
        self.horizontalLayout_3.addWidget(self.settingsGroupBox)
        self.optionsGroupBox = QtWidgets.QGroupBox(self.recipeGroupBox)
        self.optionsGroupBox.setObjectName("optionsGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.optionsGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.optionsListView = QtWidgets.QListView(self.optionsGroupBox)
        self.optionsListView.setObjectName("optionsListView")
        self.verticalLayout_3.addWidget(self.optionsListView)
        self.horizontalLayout_3.addWidget(self.optionsGroupBox)
        self.mainVerticalLayout.addWidget(self.recipeGroupBox)
        self.dependenciesGroupBox = QtWidgets.QGroupBox(Form)
        self.dependenciesGroupBox.setObjectName("dependenciesGroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dependenciesGroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.dependenciesListView = QtWidgets.QListView(self.dependenciesGroupBox)
        self.dependenciesListView.setObjectName("dependenciesListView")
        self.verticalLayout_4.addWidget(self.dependenciesListView)
        self.mainVerticalLayout.addWidget(self.dependenciesGroupBox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainVerticalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.generatePushButton = QtWidgets.QPushButton(Form)
        self.generatePushButton.setObjectName("generatePushButton")
        self.horizontalLayout_2.addWidget(self.generatePushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.mainVerticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.mainVerticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "PynCone", None, -1))
        self.conanfileLineEdit.setText(QtWidgets.QApplication.translate("Form", "/path/to/conanfile", None, -1))
        self.recipeGroupBox.setTitle(QtWidgets.QApplication.translate("Form", "recipe/version", None, -1))
        self.settingsGroupBox.setTitle(QtWidgets.QApplication.translate("Form", "settings", None, -1))
        self.optionsGroupBox.setTitle(QtWidgets.QApplication.translate("Form", "options", None, -1))
        self.dependenciesGroupBox.setTitle(QtWidgets.QApplication.translate("Form", "dependencies", None, -1))
        self.generatePushButton.setText(QtWidgets.QApplication.translate("Form", "Generate", None, -1))
