import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from remote.Message import Message


class MessageBox(QWidget):
    _message: Message = None

    def __init__(self,
                 parent: typing.Optional['QWidget'],
                 message: Message,
                 flags: typing.Union[QtCore.Qt.WindowFlags,
                                     QtCore.Qt.WindowType]) -> None:
        super().__init__(parent=parent, flags=flags)
        self._message = message

    @property
    def message(self) -> Message:
        return self._message

    @message.setter
    def message(self, message: Message):
        self._message = message

    def init_gui(self):
        pass
