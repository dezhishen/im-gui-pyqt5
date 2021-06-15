import typing

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QWidget
from remote.Message import Message, MessageElement
from tools.FileUtil import FileUtil


class MessageBox(QWidget):
    _message: Message = None
    _message_type: str = None
    _head: QLabel = None
    _name: QLabel = None
    _content: QWidget = None

    def __init__(self,
                 parent: typing.Optional['QWidget'],
                 message: Message,
                 message_type: str = "receive") -> None:
        super().__init__(parent=parent)
        self._message = message
        self._message_type = message_type
        self._init_gui()

    @property
    def message(self) -> Message:
        return self._message

    @message.setter
    def message(self, message: Message):
        self._message = message

    def reset_head_image(self, path):
        pixmap = QPixmap(path).scaled(
            50, 50, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self._head.setPixmap(pixmap)
        # self._head.setScaledContents(True)

    def _init_gui(self):
        if self._message_type == "receive":
            # 只有receive需要显示头像
            self._name = QLabel(self.message.sender.get_name_for_show())
        self._content = QWidget()
        self._content.setLayout(QVBoxLayout(self._content))
        for e in self._message.elements:
            self._content.layout().addWidget(self._gen_message_content(e))
        self._head = QLabel(self)
        # todo 布局
        main_box = QVBoxLayout(self)
        title_context = QHBoxLayout()
        content_box = QVBoxLayout()
        if self._message_type == "receive":
            title_context.addWidget(self._head)
            title_context.addWidget(self._name)
            content_box.addWidget(self._content)
        else:
            title_context.addWidget(self._head)
            content_box.addWidget(self._content)
        main_box.addLayout(title_context)
        main_box.addLayout(content_box)

        url = self.message.sender.header_image_url
        FileUtil.get_storage_from_url(
            url=url,
            dir="./resources/images/header",
            callback=self.reset_head_image
        )

    def _gen_message_content(self, element: MessageElement) -> QWidget:
        if element.type == "text":
            return QLabel(text=str(element.content, encoding="utf-8"))
        pass
