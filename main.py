import sys
from PyQt5.QtCore import QSize
from im_ui.ChatInput import ChatInput
from PyQt5.QtWidgets import QApplication
from im_instance.Entity import Message
from im_instance.MessageSenderInstance import MessageSenderInstance
from PyQt5 import QtSvg


class TestSender(MessageSenderInstance):
    def send(self, messages: list[Message]):
        for msg in messages:
            print(str(msg.content, encoding="utf8"))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ChatInput(message_send_handler=TestSender())
    fileSvg = QtSvg.QSvgWidget("./assets/icons/wenjian.svg")
    fileSvg.setMaximumSize(QSize(20, 20))
    ex.toolbar().addWidget(fileSvg)
    sys.exit(app.exec_())
