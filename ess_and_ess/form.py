# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui',
# licensing of 'form.ui' applies.
#
# Created: Fri Feb 22 01:04:42 2019
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
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(-1, 2, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listView = QtWidgets.QListView(self.groupBox_4)
        self.listView.setToolTipDuration(4000)
        self.listView.setObjectName("listView")
        self.horizontalLayout_2.addWidget(self.listView)
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.listView_2 = QtWidgets.QListView(self.groupBox_3)
        self.listView_2.setObjectName("listView_2")
        self.horizontalLayout_4.addWidget(self.listView_2)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.listView_3 = QtWidgets.QListView(self.groupBox_6)
        self.listView_3.setObjectName("listView_3")
        self.horizontalLayout_5.addWidget(self.listView_3)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.verticalLayout.addWidget(self.groupBox)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setToolTip("")
        self.pushButton.setStatusTip("")
        self.pushButton.setWhatsThis("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.lineEdit.paste)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "PynCone", None, -1))
        self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "/path/to/conanfile", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "recipe/version", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.listView.setToolTip(QtWidgets.QApplication.translate("MainWindow", "butts muthafucka!!!!!!!!", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Dependencies", None, -1))
        self.groupBox_6.setTitle(QtWidgets.QApplication.translate("MainWindow", "Options", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Generate", None, -1))
