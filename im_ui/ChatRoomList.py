from PyQt5 import QtCore
from im_instance.Entity import Message
import typing
from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QScrollArea, QToolBar,\
     QVBoxLayout, QWidget
"""
聊天框
"""


class ChatRoomList(QWidget):

    _toolbar = None
    """
    消息搜索框
    """
    _search_input = None
    """
    消息展示框上方的toolbar
    """
    _rooms = None
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
        self._search_input = QLineEdit(self)
        # toolbar
        self._rooms = QScrollArea(self)

        self._rooms.setLayout(QVBoxLayout(self))
        # 主布局
        mainBox = QHBoxLayout()
        self._toolbar = QToolBar(self)
        self._toolbar.setOrientation(QtCore.Qt.Vertical)
        leftBox = QVBoxLayout()
        leftBox.addWidget(self._toolbar)
        mainBox.addLayout(leftBox)
        rightBox = QVBoxLayout()
        rightBox.addWidget(self._search_input)
        rightBox.addWidget(self._rooms)
        mainBox.addLayout(rightBox)
        self.setLayout(mainBox)

    def search_input(self):
        return self._search_input

    def rooms(self):
        return self._rooms

    def receive_msg(self, message: Message):
        self.__message_signal.emit(message)

    def process_msg(self, message: Message):
        # todo 接收到消息的信号后的处理方法
        pass
