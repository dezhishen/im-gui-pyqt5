from im_ui.ChatBox import ChatBox
import sys
import time
from typing import List
from tools.FileUtil import FileUtil
from im_ui.ChatInput import ChatInput
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from im_instance.Entity import Message, MessageElement, Sender
from im_instance.MessageSenderInstance import MessageSenderInstance
from PyQt5 import QtSvg


class TestSender(MessageSenderInstance):
    def send(self, messages: List[Message]):
        for msg in messages:
            print(str(msg.content, encoding="utf8"))


def send_msg():
    time.sleep(5)
    sender = Sender(id=1,
                    type="pri",
                    code="1",
                    name="a",
                    alias_name="别名",
                    meta={"headerImageUrl": "test"})
    elements = [
        MessageElement(type="text", content=bytes("收到一条消息", encoding="utf-8"))
    ]
    msg = Message(sender=sender, elements=elements)
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
    send_msg()
    sys.exit(app.exec_())
