from remote.Entity import Mine
from event.LoginSignal import LOGIN_SIGNAL
import typing
from PyQt5 import QtCore, QtWidgets


class LoginWindow(QtWidgets.QWidget):
    """登录窗口

    Args:
        QtWidgets ([type]): [description]
    """

    def __init__(self, parent: typing.Optional['QtWidgets.QWidget'],
                 flags: typing.Union[QtCore.Qt.WindowFlags,
                                     QtCore.Qt.WindowType]) -> None:
        super().__init__(parent=parent, flags=flags)

    def _init_gui(self):

        LOGIN_SIGNAL.login.emit()
        pass

    def _login(self):
        mine = Mine()
        mine.id = ""
        mine.password = ""
        LOGIN_SIGNAL.login.emit(mine)
