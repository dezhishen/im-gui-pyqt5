from remote.Entity import Mine
from event.LoginSignal import LOGIN_SIGNAL
import typing
from PyQt5 import QtCore, QtWidgets


class LoginWindow(QtWidgets.QWidget):
    """登录窗口

    Args:
        QtWidgets ([type]): [description]
    """
    _account: QtWidgets.QLineEdit = None
    _password: QtWidgets.QLineEdit = None

    def __init__(self,
                 parent: typing.Optional['QtWidgets.QWidget'] = None):
        super().__init__(
            parent=parent,
            flags=QtCore.Qt.WindowType.SubWindow
        )
        self._init_gui()
        LOGIN_SIGNAL.after_login_success.connect(self._close)

    def _close(self, mine: Mine):
        self.close()

    def _init_gui(self):
        main_box = QtWidgets.QVBoxLayout(self)
        self._account = QtWidgets.QLineEdit(self)
        self._password = QtWidgets.QLineEdit(self)
        self._password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        main_box.addWidget(self._account)
        main_box.addWidget(self._password)
        btn_box = QtWidgets.QHBoxLayout()
        btn_box.addStretch(1)
        ok_btn = QtWidgets.QPushButton("登录")
        ok_btn.clicked.connect(self._login)
        btn_box.addWidget(ok_btn)
        main_box.addLayout(btn_box)
        self.setLayout(main_box)
        self.setWindowTitle("登录")

    def _login(self):
        mine = Mine()
        mine.id = self._account.text()
        mine.password = self._password.text()
        LOGIN_SIGNAL.login.emit(mine)
