from Ui_im_chartPluginWidget import Ui_chartPluginWidget
from PyQt5.QtWidgets import QWidget
from im_chartTabWidget import  ImChartTabWidget

class ImChartPluginWidget(QWidget):
    def __init__(self,parent = None):
        super(ImChartPluginWidget, self).__init__()
        self.ui = Ui_chartPluginWidget()
        self.ui.setupUi(self)
        self.setParent(parent)
        '''
        todo:此类中可开放对于聊天公告等tab的接口
        考虑到右侧工具的复杂性，暂未提供ui层次的实现
        '''

        '''
        demo:以下加载聊天tab
        '''

        self.chartTabWidget = ImChartTabWidget(self)
        self.ui.tabWidgetChartContainer.addTab(self.chartTabWidget,"聊天")

