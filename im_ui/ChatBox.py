from im_instance.Entity import Message
import typing
from PyQt5.QtWidgets import QTextBrowser, QToolBar, QVBoxLayout, QWidget
"""
聊天框
"""


class ChatBox(QWidget):
    """
    消息展示框
    """
    __text_browser = None
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
        self.__text_browser = QTextBrowser(self)
        # 主布局
        mainBox = QVBoxLayout()
        mainBox.addWidget(self.__toolbar)
        mainBox.addWidget(self.__text_browser)
        self.setLayout(mainBox)

    def text_browser(self):
        return self.__text_browser

    def toolbar(self):
        return self.__toolbar

    def receiver_msg(self, message: Message):
        # todo 渲染和处理textbrowser
        if message.type == "text":
            self.__text_browser.append(str(message.content, encoding="utf-8"))
        self.__text_browser.moveCursor(self.__text_browser.textCursor().End)
        pass
