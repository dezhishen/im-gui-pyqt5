from im_ui.ChatBox import ChatBox
import sys
import time
import threading
from typing import List
from tools.FileUtil import FileUtil
from im_ui.ChatInput import ChatInput
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from im_instance.Entity import Message, Sender
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
                        name="爸爸",
                        meta={"headerImageUrl": "test"})
        localtime = time.asctime(time.localtime(time.time()))
        msg = Message(type="text",
                      content=bytes(localtime, encoding="utf-8"),
                      sender=sender)
        chat_box.receiver_msg(message=msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    styleFile = FileUtil.readQss("./assets/style/global.qss")
    app.setStyleSheet(styleFile)

    mainWindow = QWidget()

    # 聊天框初始化
    chat_box = ChatBox()

    # 输入框初始化
    chat_input = ChatInput(message_send_handler=TestSender())
    # 自定义 toolbar的按钮
    fileSvg = QtSvg.QSvgWidget("./assets/icons/wenjian.svg")
    chat_input.toolbar().addWidget(fileSvg)
    # 展示
    # 主窗口布局
    mainWindowLayout = QVBoxLayout()
    mainWindowLayout.addWidget(chat_box)
    mainWindowLayout.addWidget(chat_input)
    mainWindow.setLayout(mainWindowLayout)
    mainWindow.setWindowTitle("示例")
    mainWindow.show()
    t1 = threading.Thread(target=send_msg)
    t1.start()
    sys.exit(app.exec_())
