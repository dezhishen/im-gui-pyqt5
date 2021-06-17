from gui.WindowController import WindowController
from gui.LoginWindow import LoginWindow
from tools.ThreadPoolUtil import THREAD_POOL
from event.MessageSignal import MESSAGE_SIGNAL
from remote.Client import Client
from remote.Entity import Mine, Receiver, Sender
from gui.MainWindow import MainWindow
import sys
import time
from tools.FileUtil import FileUtil
from PyQt5.QtWidgets import QApplication
from remote.Message import Message, MessageElement
from PyQt5 import QtSvg
from event import LoggingFunc
from alembic.config import Config
import alembic.command
config = Config('alembic.ini')
config.attributes['configure_logger'] = False

alembic.command.upgrade(config, 'head')


class TestClient(Client):

    def send_message(self, message: Message):
        for element in message.elements():
            print(str(element.content, encoding="utf8"))

    def _listen_receive_message(self):
        """监听方法
        """
        THREAD_POOL.submit(self.__listen_message)
        # wait([f], return_when=ALL_COMPLETED)
        # pass

    def _login(self, mine: Mine):
        return mine

    def __listen_message(self):
        while True:
            sender = Sender(
                id=1,
                type="pri",
                code="1",
                name="a",
                alias_name="别名",
                header_image_url="https://avatars.githubusercontent.com/u/" +
                "26274059?v=4",
                meta={"headerImageUrl": "test"}
            )
            receiver = Receiver(id=1,
                                type="pri",
                                code="1",
                                name="a",
                                alias_name="别名",
                                meta={"headerImageUrl": "test"})
            elements = [
                MessageElement(
                    id=None,
                    type="text",
                    content=bytes("收到一条消息", encoding="utf-8"))
            ]
            msg = Message(id=None, sender=sender,
                          receiver=receiver, elements=elements)
            MESSAGE_SIGNAL.receive.emit(msg)
            time.sleep(5)


def log_send(message: Message):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    styleFile = FileUtil.read_qss("./assets/style/global.qss")
    app.setStyleSheet(styleFile)
    client = TestClient()
    LoggingFunc.connect_log()

    main_window = MainWindow(title="测试", client=client)
    # 自定义 toolbar的按钮
    fileSvg = QtSvg.QSvgWidget("./assets/icons/wenjian.svg")
    main_window.chat_input.toolbar.addWidget(fileSvg)
    login_win = LoginWindow()
    win_control = WindowController(login_win=login_win, main_win=main_window)
    win_control.load_login_window()
    # win_control.load_main_window(mine=Mine())
    sys.exit(app.exec_())
