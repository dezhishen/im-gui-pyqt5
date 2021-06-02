import sys
from typing import List
from PyQt5.QtCore import QSize
from tools.FileUtil import FileUtil
from im_ui.ChatInput import ChatInput
from PyQt5.QtWidgets import QApplication
from im_instance.Entity import Message
from im_instance.MessageSenderInstance import MessageSenderInstance
from PyQt5 import QtSvg


class TestSender(MessageSenderInstance):
    def send(self, messages: List[Message]):
        for msg in messages:
            print(str(msg.content, encoding="utf8"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    styleFile = FileUtil.readQss("./assets/style/global.qss")
    app.setStyleSheet(styleFile)
    # 输入框初始化
    chat_input = ChatInput(message_send_handler=TestSender())
    # 自定义 toolbar的按钮
    fileSvg = QtSvg.QSvgWidget("./assets/icons/wenjian.svg")
    fileSvg.setMaximumSize(QSize(20, 20))
    chat_input.toolbar().addWidget(fileSvg)
    # 展示
    chat_input.setWindowTitle("输入框示例")
    chat_input.show()
    sys.exit(app.exec_())
