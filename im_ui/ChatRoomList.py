from PyQt5 import QtCore
from im_instance.Entity import Message
import typing
from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QScrollArea, QToolBar,\
     QVBoxLayout, QWidget
"""
聊天框
"""


class ChatRoomList(QWidget):

    __conf_toolbar = None
    """
    消息搜索框
    """
    __search_input = None
    """
    消息展示框上方的toolbar
    """
    __rooms = None
    """
    接收到消息的信号
    """
    __message_signal = QtCore.pyqtSignal(Message)

    # """
    # 消息监听接口
    # """
    # __msg_listener = None

    def __init__(self, parent: typing.Optional['QWidget'] = None):
        super().__init__(parent=parent)
        self.__init_gui()

    def __init_gui(self):
        # 消息信号
        self.__message_signal.connect(self.process_msg)
        self.setObjectName("chat-room-list")
        # 搜索框
        self.__search_input = QLineEdit(self)
        # toolbar
        self.__rooms = QScrollArea(self)

        self.__rooms.setLayout(QVBoxLayout(self))
        # 主布局
        mainBox = QHBoxLayout()
        self.__toolbar = QToolBar(self)
        self.__toolbar.setOrientation(QtCore.Qt.Vertical)
        mainBox.addWidget(self.__toolbar)
        rightBox = QVBoxLayout()
        rightBox.addWidget(self.__search_input)
        rightBox.addWidget(self.__rooms)
        mainBox.addLayout(rightBox)
        self.setLayout(mainBox)

    def search_input(self):
        return self.__search_input

    def rooms(self):
        return self.__rooms

    def receiver_msg(self, message: Message):
        self.__message_signal.emit(message)

    def process_msg(self, message: Message):
        # todo 接收到消息的信号后的处理方法
        pass
