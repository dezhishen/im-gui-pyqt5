from PyQt5 import QtCore
from remote.Message import Message


class _MessageSignal(QtCore.QObject):
    receive = QtCore.pyqtSignal(Message)
    to_send = QtCore.pyqtSignal(Message)
    after_send = QtCore.pyqtSignal(Message)


MESSAGE_SIGNAL = _MessageSignal()
