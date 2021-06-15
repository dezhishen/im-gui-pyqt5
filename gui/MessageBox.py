from tools.FileUtil import FileUtil
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from remote.Message import Message, MessageElement


class MessageBox(QWidget):
    _message: Message = None
    _message_type: str = None
    _head: QWidget = None
    _name: QLabel = None
    _content: QWidget = None

    def __init__(self,
                 parent: typing.Optional['QWidget'],
                 message: Message,
                 flags: typing.Union[
                     QtCore.Qt.WindowFlags,
                     QtCore.Qt.WindowType
                 ],
                 message_type: str = "receive") -> None:
        super().__init__(parent=parent, flags=flags)
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
        # todo 网络图片缓存后,重新渲染头像
        pass

    def _init_gui(self):
        # todo 根据message_type=="receive"/"send"形成不同的消息布局
        # todo 名称
        self._name = QLabel(self.message.sender.get_name_for_show())
        # todo 消息
        self._content = QWidget()
        self._content.setLayout(QVBoxLayout(self._content))
        for e in self._message.elements:
            self._content.layout().addWidget(self._gen_message_content(e))
        # todo 头像框
        self._head = None
        # todo 加入layout中
        url = self.message.sender.header_image_url
        FileUtil.get_storage_from_url(
            url=url,
            dir="./resources/images/header",
            callback=self.reset_head_image
        )

    def _gen_message_content(element: MessageElement) -> QWidget:
        if element.type == "text":
            return QLabel(str(element.content))
        pass
