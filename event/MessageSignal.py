from remote.Entity import Entity
from PyQt5 import QtCore
from remote.Message import Message


class _MessageSignal(QtCore.QObject):
    receive = QtCore.pyqtSignal(Message)
    to_send = QtCore.pyqtSignal(Message)
    after_send = QtCore.pyqtSignal(Message)
    to_change_msg_session = QtCore.pyqtSignal(Entity)
    after_change_msg_session = QtCore.pyqtSignal(Entity)


MESSAGE_SIGNAL = _MessageSignal()
