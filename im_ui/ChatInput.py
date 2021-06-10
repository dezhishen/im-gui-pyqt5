from im_instance.User import Sender
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from im_instance.Message import Message, MessageElement

from PyQt5 import QtSvg
# from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QApplication, QTextEdit, QToolBar, QWidget,
                             QPushButton, QHBoxLayout, QVBoxLayout)


class ChatInput(QWidget):
    _toolbar = None
    _text_edit = None

    def __init__(self, parent: QWidget):
        super().__init__()
        self.parent = parent
        self.initUI()

    def initUI(self):
        # 自身属性设置
        self.setObjectName("chat-input")
        # toolbar
        toolbar = QToolBar(self)
        imageSvg = QtSvg.QSvgWidget("./assets/icons/tupian.svg")
        toolbar.addWidget(imageSvg)
        self._toolbar = toolbar
        # 按钮组
        # closeButton = QPushButton("关闭")
        sendButton = QPushButton("发送")
        sendButton.clicked.connect(self.send_message)
        bottonsHbox = QHBoxLayout()
        bottonsHbox.addStretch(1)
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

    def send_message(self):
        print("chat-input:send_message")
        message_content_str = self._text_edit.toPlainText()
        if message_content_str is None or message_content_str == "":
            return
        the_message = Message(sender=Sender(id=1,
                                            type="pri",
                                            code="1",
                                            name="a",
                                            alias_name="我自己",
                                            header_image_url="test",
                                            meta={"foo": "bar"}),
                              receiver=None,
                              elements=[
                                  MessageElement(type="text",
                                                 content=bytes(
                                                     message_content_str,
                                                     encoding="utf-8"))
                              ])
        self.parent.send_message(message=the_message)
        self._text_edit.clear()
        self._text_edit.setFocus()

    def text_edit(self):
        return self._text_edit

    def toolbar(self):
        return self._toolbar


class ChatTextEdit(QTextEdit):
    def __init__(self, parent: ChatInput):
        QtWidgets.QTextEdit.__init__(self)
        self.parent = parent

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            if int(QApplication.keyboardModifiers()) == 0:
                self.parent.send_message()
            elif QApplication.keyboardModifiers() == Qt.ControlModifier:
                self.textCursor().insertText("\n")
        else:
            QtWidgets.QTextEdit.keyPressEvent(self, event)
