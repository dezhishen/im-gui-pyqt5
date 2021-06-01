# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Test\im-gui-pyqt5\im-gui-pyqt5\ui\im_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolbarPlugins = QtWidgets.QToolBar(self.centralwidget)
        self.toolbarPlugins.setMinimumSize(QtCore.QSize(100, 0))
        self.toolbarPlugins.setMaximumSize(QtCore.QSize(100, 16777215))
        self.toolbarPlugins.setAllowedAreas(QtCore.Qt.LeftToolBarArea)
        self.toolbarPlugins.setOrientation(QtCore.Qt.Vertical)
        self.toolbarPlugins.setIconSize(QtCore.QSize(24, 24))
        self.toolbarPlugins.setObjectName("toolbarPlugins")
        self.horizontalLayout.addWidget(self.toolbarPlugins)
        self.stackedWidgetPluginContainer = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidgetPluginContainer.setObjectName("stackedWidgetPluginContainer")
        self.horizontalLayout.addWidget(self.stackedWidgetPluginContainer)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidgetPluginContainer.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

