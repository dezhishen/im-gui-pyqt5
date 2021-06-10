from im_ui.MainWindow import MainWindow
import sys
import time
import threading
from typing import List
from tools.FileUtil import FileUtil
from PyQt5.QtWidgets import QApplication
from im_instance.Entity import Message, MessageElement, Sender
from im_instance.MessageSenderInstance import MessageSenderInstance
from PyQt5 import QtSvg


class TestSender(MessageSenderInstance):
    def send(self, messages: List[Message]):
        for msg in messages:
            print(str(msg.content, encoding="utf8"))


def send_msg():
    while True:
        time.sleep(5)
        sender = Sender(id=1,
                        type="pri",
                        code="1",
                        name="a",
                        alias_name="别名",
                        meta={"headerImageUrl": "test"})
        elements = [
            MessageElement(type="text",
                           content=bytes("收到一条消息", encoding="utf-8"))
        ]
        msg = Message(sender=sender, elements=elements)
        mainWindow.receive_msg(message=msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    styleFile = FileUtil.readQss("./assets/style/global.qss")
    app.setStyleSheet(styleFile)
    mainWindow = MainWindow(title="测试", message_send_handler=TestSender)
    # 自定义 toolbar的按钮
    fileSvg = QtSvg.QSvgWidget("./assets/icons/wenjian.svg")
    mainWindow.chat_input().toolbar().addWidget(fileSvg)
    mainWindow.show()
    t1 = threading.Thread(target=send_msg)
    t1.start()
    sys.exit(app.exec_())
