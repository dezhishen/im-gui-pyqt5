from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5.QtGui import QIcon
from Ui_im_mainWindow import Ui_MainWindow
from im_chartPluginWidget import ImChartPluginWidget


class ImAppMainWindow(QMainWindow):
    def __init__(self):
        super(ImAppMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setStyleSheet("QMainWindow#MainWindow{"
                           # "background:white"
                           "}"
                           "QToolBar#toolbarPlugins{"
                           "background:silver"
                           "}")
        '''
            todo: can be refactor as plugins
            当toolbar 添加一项 action 时 在 stackedwidget中插入一个插件 widget
        '''
        '''
            demo:icon 参数传图片路径可展示icon
        '''
        self.action_pluginChart = QAction(QIcon(), "chart")
        self.ui.toolbarPlugins.addAction(self.action_pluginChart)

        self.chartPluginWidget = ImChartPluginWidget(self)
        self.ui.stackedWidgetPluginContainer.addWidget(self.chartPluginWidget)
        self.ui.stackedWidgetPluginContainer.setCurrentIndex(0)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = ImAppMainWindow()
    ui.show()
    sys.exit(app.exec_())
