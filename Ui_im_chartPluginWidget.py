# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Test\im-gui-pyqt5\im-gui-pyqt5\im_chartPluginWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_chartPluginWidget(object):
    def setupUi(self, chartPluginWidget):
        chartPluginWidget.setObjectName("chartPluginWidget")
        chartPluginWidget.resize(692, 544)
        self.gridLayout_2 = QtWidgets.QGridLayout(chartPluginWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(chartPluginWidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(200, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 198, 542))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, -1, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEditSeachChart = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditSeachChart.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditSeachChart.setObjectName("lineEditSeachChart")
        self.horizontalLayout.addWidget(self.lineEditSeachChart)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.listViewCharts = QtWidgets.QListView(self.scrollAreaWidgetContents)
        self.listViewCharts.setObjectName("listViewCharts")
        self.gridLayout.addWidget(self.listViewCharts, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidgetChartContainer = QtWidgets.QTabWidget(chartPluginWidget)
        self.tabWidgetChartContainer.setObjectName("tabWidgetChartContainer")
        self.gridLayout_2.addWidget(self.tabWidgetChartContainer, 0, 1, 1, 1)

        self.retranslateUi(chartPluginWidget)
        self.tabWidgetChartContainer.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(chartPluginWidget)

    def retranslateUi(self, chartPluginWidget):
        _translate = QtCore.QCoreApplication.translate
        chartPluginWidget.setWindowTitle(_translate("chartPluginWidget", "Form"))

