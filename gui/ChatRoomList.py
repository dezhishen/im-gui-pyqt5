from PyQt5 import QtCore
from im_instance.Message import Message
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

    # 接收到消息的信号
    __receive_message_signal = QtCore.pyqtSignal(Message)

    # 发送到消息的信号
    __send_message_signal = QtCore.pyqtSignal(Message)

    # """
    # 消息监听接口
    # """
    # __msg_listener = None

    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.__init_gui()

    def __init_gui(self):
        # 消息信号
        self.__receive_message_signal.connect(self.after_receive_message)
        self.__send_message_signal.connect(self.after_send_message)
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

    def receive_message(self, message: Message):
        self.__receive_message_signal.emit(message)

    def send_message(self, message: Message):
        self.__send_message_signal.emit(message)

    def after_receive_message(self, message: Message):
        # todo 接收到消息的信号后的处理方法
        pass

    def after_send_message(self, message: Message):
        # todo 接收到消息的信号后的处理方法
        pass