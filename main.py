from remote.Entity import Mine
from examples.CqWsClient import CqWsClient
from gui.WindowController import WindowController
from gui.LoginWindow import LoginWindow
from gui.MainWindow import MainWindow
import sys
from tools.FileUtil import FileUtil
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtSvg
from event import LoggingFunc
from alembic.config import Config
import alembic.command
config = Config('alembic.ini')
config.attributes['configure_logger'] = False

alembic.command.upgrade(config, 'head')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    styleFile = FileUtil.read_qss("./assets/style/global.qss")
    app.setStyleSheet(styleFile)
    client = CqWsClient()
    LoggingFunc.connect_log()

    main_window = MainWindow()
    # 自定义 toolbar的按钮
    fileSvg = QtSvg.QSvgWidget("./assets/icons/wenjian.svg")
    main_window.chat_input.toolbar.addWidget(fileSvg)
    login_win = LoginWindow()
    win_control = WindowController(login_win=login_win, main_win=main_window)
    # win_control.load_login_window()
    mine = Mine()
    client.do_login(mine)
    # win_control.load_main_window(mine)
    sys.exit(app.exec_())
