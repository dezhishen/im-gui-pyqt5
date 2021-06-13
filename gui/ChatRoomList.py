from PyQt5 import QtCore
from event.MessageSignal import MESSAGE_SIGNAL
from remote.Message import Message
from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QListWidget, QToolBar,\
    QVBoxLayout, QWidget


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

    # """
    # 消息监听接口
    # """
    # __msg_listener = None

    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.__init_gui()

    def __init_gui(self):
        # 消息信号
        MESSAGE_SIGNAL.receive.connect(self.after_receive_message)
        MESSAGE_SIGNAL.send.connect(self.after_send_message)
        self.setObjectName("chat-room-list")
        # 搜索框
        self._search_input = QLineEdit(self)
        # toolbar
        self._rooms = QListWidget(self)

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
        MESSAGE_SIGNAL.receive.emit(message)

    def send_message(self, message: Message):
        MESSAGE_SIGNAL.send.emit(message)

    def after_receive_message(self, message: Message):
        print("chat-room-list:after_receive_message")
        # todo 接收到消息的信号后的处理方法
        pass

    def after_send_message(self, message: Message):
        # todo 接收到消息的信号后的处理方法
        print("chat-room-list:after_send_message")
        pass
