import sys

from im_instance.MessageSenderInstance import MessageSenderInstance
from im_instance.Entity import Message

from PyQt5 import QtSvg
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QTextEdit, QToolBar, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout)

sys.path.append("../")


class ChatInput(QWidget):

    __toolbar = None
    __text_edit = None
    __message_send_handler = None

    def __init__(self, message_send_handler: MessageSenderInstance):
        super().__init__()
        self.__message_send_handler = message_send_handler
        self.initUI()

    def initUI(self):
        # toolbar
        toolbar = QToolBar()
        imageSvg = QtSvg.QSvgWidget("./assets/icons/tupian.svg")
        imageSvg.setMaximumSize(QSize(20, 20))
        toolbar.addWidget(imageSvg)
        self.__toolbar = toolbar
        # 按钮组
        closeButton = QPushButton("关闭")
        sendButton = QPushButton("发送")
        sendButton.clicked.connect(self.send_button_click)
        bottonsHbox = QHBoxLayout()
        bottonsHbox.addStretch(1)
        bottonsHbox.addWidget(closeButton)
        bottonsHbox.addWidget(sendButton)
        mainBox = QVBoxLayout()
        mainBox.addWidget(toolbar)
        text_edit = QTextEdit()
        text_edit.setAcceptRichText(False)
        self.__text_edit = text_edit
        mainBox.addWidget(text_edit)
        # mainBox.addStretch(1)
        mainBox.addLayout(bottonsHbox)
        self.setLayout(mainBox)

    def send_button_click(self):
        message_content_str = self.__text_edit.toPlainText()
        if message_content_str is None or message_content_str == "":
            return
        self.__message_send_handler.send(messages=[
            Message(type="text",
                    content=bytes(message_content_str, encoding="utf-8"),
                    sender=None)
        ])
        self.__text_edit.clear()
        self.__text_edit.setFocus()

    def text_edit(self):
        return self.__text_edit

    def toolbar(self):
        return self.__toolbar

    def message_sender(self):
        return self.__message_send_handler
