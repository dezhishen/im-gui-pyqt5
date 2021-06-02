import sys
from PyQt5.QtCore import QSize
from im_ui.ChatInput import ChatInput
from PyQt5.QtWidgets import QApplication, QWidget
from im_instance.Entity import Message
from im_instance.MessageSenderInstance import MessageSenderInstance
from PyQt5 import QtSvg


class TestSender(MessageSenderInstance):
    def send(self, messages: list[Message]):
        for msg in messages:
            print(str(msg.content, encoding="utf8"))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    root_widget = QWidget()
    root_widget.setStyleSheet("QToolBar{spacing:20px;}")

    # 输入框初始化
    chat_input = ChatInput(parent=root_widget,
                           message_send_handler=TestSender())
    # 自定义 toolbar的按钮
    fileSvg = QtSvg.QSvgWidget("./assets/icons/wenjian.svg")
    fileSvg.setMaximumSize(QSize(20, 20))
    chat_input.toolbar().addWidget(fileSvg)

    # 展示
    root_widget.setWindowTitle("输入框示例")
    root_widget.show()
    sys.exit(app.exec_())
