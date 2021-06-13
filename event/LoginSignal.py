from remote.Entity import Mine
from PyQt5 import QtCore


class _LoginSignal(QtCore.QObject):
    login = QtCore.pyqtSignal(Mine)
    after_login_success = QtCore.pyqtSignal(Mine)
    logout = QtCore.pyqtSignal(Mine)
    after_logout = QtCore.pyqtSignal(Mine)


LOGIN_SIGNAL = _LoginSignal()
