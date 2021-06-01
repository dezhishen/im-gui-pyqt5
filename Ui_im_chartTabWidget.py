# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Test\im-gui-pyqt5\im-gui-pyqt5\im_chartTabWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_im_chartTabWidget(object):
    def setupUi(self, im_chartTabWidget):
        im_chartTabWidget.setObjectName("im_chartTabWidget")
        im_chartTabWidget.resize(481, 583)
        self.gridLayout = QtWidgets.QGridLayout(im_chartTabWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowserChartRecord = QtWidgets.QTextBrowser(im_chartTabWidget)
        self.textBrowserChartRecord.setObjectName("textBrowserChartRecord")
        self.verticalLayout.addWidget(self.textBrowserChartRecord)
        self.toolbarChartTools = QtWidgets.QToolBar(im_chartTabWidget)
        self.toolbarChartTools.setMinimumSize(QtCore.QSize(100, 0))
        self.toolbarChartTools.setMaximumSize(QtCore.QSize(100, 16777215))
        self.toolbarChartTools.setAllowedAreas(QtCore.Qt.LeftToolBarArea)
        self.toolbarChartTools.setOrientation(QtCore.Qt.Horizontal)
        self.toolbarChartTools.setIconSize(QtCore.QSize(24, 24))
        self.toolbarChartTools.setObjectName("toolbarChartTools")
        self.verticalLayout.addWidget(self.toolbarChartTools)
        self.textEditInput = QtWidgets.QTextEdit(im_chartTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditInput.sizePolicy().hasHeightForWidth())
        self.textEditInput.setSizePolicy(sizePolicy)
        self.textEditInput.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEditInput.setObjectName("textEditInput")
        self.verticalLayout.addWidget(self.textEditInput)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(im_chartTabWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(im_chartTabWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(im_chartTabWidget)
        QtCore.QMetaObject.connectSlotsByName(im_chartTabWidget)

    def retranslateUi(self, im_chartTabWidget):
        _translate = QtCore.QCoreApplication.translate
        im_chartTabWidget.setWindowTitle(_translate("im_chartTabWidget", "Form"))
        self.pushButton.setText(_translate("im_chartTabWidget", "关闭"))
        self.pushButton_2.setText(_translate("im_chartTabWidget", "发送"))

