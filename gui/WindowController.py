from event.LoginSignal import LOGIN_SIGNAL
from remote.Entity import Mine
from gui.MainWindow import MainWindow
from gui.LoginWindow import LoginWindow


class WindowController:
    _login_window: LoginWindow = None
    _main_window: MainWindow = None

    def __init__(self,  login_win: LoginWindow,
                 main_win: MainWindow) -> None:
        self._login_window = login_win
        self._main_window = main_win
        LOGIN_SIGNAL.after_login_success.connect(self.load_main_window)

    def load_login_window(self):
        self._login_window.show()

    def load_main_window(self, mine: Mine):
        self._main_window.show()
