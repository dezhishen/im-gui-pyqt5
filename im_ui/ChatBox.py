from im_instance.Entity import Message, MessageElement
import typing
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QScrollArea, QToolBar,\
     QVBoxLayout, QWidget
"""
聊天框
"""


class ChatBox(QWidget):
    """
    消息展示框
    """
    __chat_box = None
    """
    消息展示框上方的toolbar
    """
    __toolbar = None

    # """
    # 消息监听接口
    # """
    # __msg_listener = None

    def __init__(self, parent: typing.Optional['QWidget'] = None):
        super().__init__(parent=parent)
        self.__init_gui()

    def __init_gui(self):
        self.setObjectName("chat-box")
        # toolbar
        self.__toolbar = QToolBar(self)

        # 消息框
        self.__chat_box = QScrollArea(self)
        self.__chat_box.setLayout(QVBoxLayout(self))
        # 主布局
        mainBox = QVBoxLayout()
        mainBox.addWidget(self.__toolbar)
        mainBox.addWidget(self.__chat_box)
        self.setLayout(mainBox)

    def chat_box(self):
        return self.__chat_box

    def toolbar(self):
        return self.__toolbar

    def receiver_msg(self, message: Message):
        print("0")
        mes_item_widget = self.render_message(message)
        print("0-")
        print("add")
        self.chat_box().layout().addWidget(mes_item_widget)
        print("add-")

    def render_message(self, message: Message):
        la = QHBoxLayout()
        print("1")
        la.addWidget(QLabel(text=message.sender().get_name_for_show()))
        print("1-")
        for e in message.elements():
            print("2")
            la.addWidget(self.render_item(e))
            print("2-")
        print("3")
        result = QWidget()
        print("3-")
        result.setLayout(la)
        return result

    def render_item(self, element: MessageElement):
        if element.type() == "text":
            return QLabel(text=str(element.content(), encoding="utf-8"))
        return
