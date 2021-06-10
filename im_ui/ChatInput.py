from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from im_instance.MessageSenderInstance import MessageSenderInstance
from im_instance.Entity import Message

from PyQt5 import QtSvg
# from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QApplication, QTextEdit, QToolBar, QWidget,
                             QPushButton, QHBoxLayout, QVBoxLayout)


class ChatTextEdit(QTextEdit):
    def __init__(self, parent):
        QtWidgets.QTextEdit.__init__(self)
        self.parent = parent

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            if int(QApplication.keyboardModifiers()) == 0:
                self.parent.send_msg()
            elif QApplication.keyboardModifiers() == Qt.ControlModifier:
                self.textCursor().insertText("\n")
        else:
            QtWidgets.QTextEdit.keyPressEvent(self, event)


class ChatInput(QWidget):
    _toolbar = None
    _text_edit = None
    _message_send_handler = None

    def __init__(self, message_send_handler: MessageSenderInstance):
        super().__init__()
        self._message_send_handler = message_send_handler
        self.initUI()

    def initUI(self):
        # 自身属性设置
        self.setObjectName("chat-input")
        # toolbar
        toolbar = QToolBar()
        imageSvg = QtSvg.QSvgWidget("./assets/icons/tupian.svg")
        toolbar.addWidget(imageSvg)
        self._toolbar = toolbar
        # 按钮组
        # closeButton = QPushButton("关闭")
        sendButton = QPushButton("发送")
        sendButton.clicked.connect(self.send_msg)
        bottonsHbox = QHBoxLayout()
        bottonsHbox.addStretch(1)
        # bottonsHbox.addWidget(closeButton)
        bottonsHbox.addWidget(sendButton)
        # 输入文本框
        text_edit = ChatTextEdit(self)
        text_edit.setAcceptRichText(False)
        self._text_edit = text_edit
        # 整体布局
        mainBox = QVBoxLayout()
        mainBox.addWidget(toolbar)
        mainBox.addWidget(text_edit)
        mainBox.addLayout(bottonsHbox)
        # 设置布局
        self.setLayout(mainBox)

    def send_msg(self):
        message_content_str = self._text_edit.toPlainText()
        if message_content_str is None or message_content_str == "":
            return
        self._message_send_handler.send(messages=[
            Message(type="text",
                    content=bytes(message_content_str, encoding="utf-8"),
                    sender=None)
        ])
        self._text_edit.clear()
        self._text_edit.setFocus()

    def text_edit(self):
        return self._text_edit

    def toolbar(self):
        return self._toolbar

    def message_sender(self):
        return self._message_send_handler
