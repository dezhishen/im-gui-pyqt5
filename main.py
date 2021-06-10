from im_instance.Client import Client
from im_instance.User import Receiver, Sender
from im_ui.MainWindow import MainWindow
import sys
import time
# import threading
from typing import Callable
from tools.FileUtil import FileUtil
from PyQt5.QtWidgets import QApplication
from im_instance.Message import Message, MessageElement
from PyQt5 import QtSvg


class TestClient(Client):
    def send_message(self, message: Message):
        for element in message.elements():
            print(str(element.content(), encoding="utf8"))

    def listen_receive_message(self, process_message: Callable[[Message],
                                                               None]):
        """监听方法

        Args:
            callback (typing.Callable[[Message], ]): 回调函数,方法内部应该回调该方法,处理消息的接收
        """
        # t1 = threading.Thread(target=self.__listen_message,
        #                       args=[process_message])
        # t1.start()
        pass

    def __listen_message(self, process_message):
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
            process_message(message=msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    styleFile = FileUtil.readQss("./assets/style/global.qss")
    app.setStyleSheet(styleFile)
    client = TestClient()
    mainWindow = MainWindow(title="测试", client=client)
    # 自定义 toolbar的按钮
    fileSvg = QtSvg.QSvgWidget("./assets/icons/wenjian.svg")
    mainWindow.chat_input().toolbar().addWidget(fileSvg)
    mainWindow.show()
    mainWindow.listen_message()
    sys.exit(app.exec_())
