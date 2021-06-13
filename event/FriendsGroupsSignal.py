from PyQt5 import QtCore


class _FriendsGroupSignal(QtCore.QObject):
    do_load_friends = QtCore.pyqtSignal(list)
    after_load_friends = QtCore.pyqtSignal(list)
    do_load_groups = QtCore.pyqtSignal(list)
    after_load_groups = QtCore.pyqtSignal(list)


FRIENDS_GROUP_SIGNAL = _FriendsGroupSignal()
