from event.MessageSignal import MESSAGE_SIGNAL
from remote.Client import Client
from remote.User import Receiver, Sender
from gui.MainWindow import MainWindow
import sys
import time
import threading
from tools.FileUtil import FileUtil
from PyQt5.QtWidgets import QApplication
from remote.Message import Message, MessageElement
from PyQt5 import QtSvg


class TestClient(Client):
    def send_message(self, message: Message):
        for element in message.elements():
            print(str(element.content(), encoding="utf8"))

    def listen_receive_message(self):
        """监听方法
        """
        t1 = threading.Thread(target=self.__listen_message)
        t1.start()
        # pass

    def __listen_message(self):
        while True:
            time.sleep(5)
            sender = Sender(id=1,
                            type="pri",
                            code="1",
                            name="a",
                            alias_name="别名",
                            meta={"headerImageUrl": "test"})
            receiver = Receiver(id=1,
                                type="pri",
                                code="1",
                                name="a",
                                alias_name="别名",
                                meta={"headerImageUrl": "test"})
            elements = [
                MessageElement(type="text",
                               content=bytes("收到一条消息", encoding="utf-8"))
            ]
            msg = Message(sender=sender, receiver=receiver, elements=elements)
            MESSAGE_SIGNAL.receive.emit(msg)


def log_send(message: Message):
    print("发送消息")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    styleFile = FileUtil.readQss("./assets/style/global.qss")
    app.setStyleSheet(styleFile)
    client = TestClient()
    mainWindow = MainWindow(title="测试", client=client)
    # 自定义 toolbar的按钮
    fileSvg = QtSvg.QSvgWidget("./assets/icons/wenjian.svg")
    mainWindow.chat_input().toolbar().addWidget(fileSvg)
    MESSAGE_SIGNAL.send.connect(log_send)
    mainWindow.show()
    mainWindow.listen_message()
    sys.exit(app.exec_())
