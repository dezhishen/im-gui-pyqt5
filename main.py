from im_instance.Client import Client
from im_instance.User import Receiver, Sender
from im_ui.MainWindow import MainWindow
import sys
import time
import threading
from typing import List
from tools.FileUtil import FileUtil
from PyQt5.QtWidgets import QApplication
from im_instance.Message import Message, MessageElement
from im_instance.MessageSenderInstance import MessageSendInstance
from PyQt5 import QtSvg


class TestSender(MessageSendInstance):
    def send(self, messages: List[Message]):
        for msg in messages:
            print(str(msg.content, encoding="utf8"))


class TestClient(Client):
    def start_receive_message(self):
        pass


def send_msg():
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
        mainWindow.receive_msg(message=msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    styleFile = FileUtil.readQss("./assets/style/global.qss")
    app.setStyleSheet(styleFile)
    client = TestClient(message_send_instance=TestSender)
    mainWindow = MainWindow(title="测试", client=client)
    # 自定义 toolbar的按钮
    fileSvg = QtSvg.QSvgWidget("./assets/icons/wenjian.svg")
    mainWindow.chat_input().toolbar().addWidget(fileSvg)
    mainWindow.show()
    t1 = threading.Thread(target=send_msg)
    t1.start()
    sys.exit(app.exec_())
