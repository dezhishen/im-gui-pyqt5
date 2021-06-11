from remote.Message import Message, MessageElement
from event.MessageSignal import MESSAGE_SIGNAL
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QScrollArea, QToolBar,\
    QVBoxLayout, QWidget
"""
聊天框
"""


class ChatBox(QWidget):
    """
    消息展示框
    """
    _chat_box = None
    """
    消息展示框上方的toolbar
    """
    _toolbar = None

    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.__init_gui()

    def __init_gui(self):
        # 消息信号
        MESSAGE_SIGNAL.receive.connect(self.after_receive_message)
        MESSAGE_SIGNAL.send.connect(self.after_send_message)
        self.setObjectName("chat-box")
        # toolbar
        self._toolbar = QToolBar(self)

        # 消息框
        self._chat_box = QScrollArea(self)
        self._chat_box.setLayout(QVBoxLayout(self))
        # 主布局
        mainBox = QVBoxLayout()
        mainBox.addWidget(self._toolbar)
        mainBox.addWidget(self._chat_box)
        self.setLayout(mainBox)

    def chat_box(self):
        return self._chat_box

    def toolbar(self):
        return self._toolbar

    def receive_message(self, message: Message):
        MESSAGE_SIGNAL.receive.emit(message)

    def send_message(self, message: Message):
        print("chatbox:send_message")
        MESSAGE_SIGNAL.send.emit(message)

    def after_receive_message(self, message: Message):
        mes_item_widget = self.render_receive_message(message)
        self.chat_box().layout().addWidget(mes_item_widget)

    def after_send_message(self, message: Message):
        print("chatbox:after_send_message")
        mes_item_widget = self.render_send_message(message)
        self.chat_box().layout().addWidget(mes_item_widget)

    def render_receive_message(self, message: Message):
        la = QHBoxLayout()
        la.addWidget(QLabel(text=message.sender().get_name_for_show()))
        for e in message.elements():
            la.addWidget(self.render_item(e))
        result = QWidget()
        result.setLayout(la)
        return result

    def render_send_message(self, message: Message):
        la = QHBoxLayout()
        la.addWidget(QLabel(text=message.sender().get_name_for_show()))
        for e in message.elements():
            la.addWidget(self.render_item(e))
        result = QWidget()
        result.setLayout(la)
        return result

    def render_item(self, element: MessageElement):
        if element.type() == "text":
            return QLabel(text=str(element.content(), encoding="utf-8"))
        return
