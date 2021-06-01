from Ui_im_chartTabWidget import Ui_im_chartTabWidget
from  PyQt5.QtWidgets import QWidget

class ImChartTabWidget(QWidget):
    def __init__(self,parent = None):
        super(ImChartTabWidget, self).__init__()
        self.ui = Ui_im_chartTabWidget()
        self.ui.setupUi(self)
        self.setParent(parent)

        #todo:可在此类开放对截图等工具的添加接口


