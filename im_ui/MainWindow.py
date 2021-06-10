from im_instance.Client import Client
from im_instance.Message import Message
from im_ui.ChatInput import ChatInput
from im_ui.ChatBox import ChatBox
from im_ui.ChatRoomList import ChatRoomList
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QWidget):
    _chat_box = None
    _chat_room = None
    _chat_input = None
    _client = None

    def __init__(self, title: str, client: Client):
        super().__init__()
        self._client = client
        self._title = title
        self.__init_gui()

    def __init_gui(self):
        self._chat_room = ChatRoomList(self)
        # 聊天框初始化
        self._chat_box = ChatBox(self)
        # 输入框初始化
        self._chat_input = ChatInput(self)
        # 自定义 toolbar的按钮
        # fileSvg = QtSvg.QSvgWidget("./assets/icons/wenjian.svg")
        # self._chat_input.toolbar().addWidget(fileSvg)
        # 展示
        # 主窗口布局
        mainLayOut = QtWidgets.QHBoxLayout()
        mainLayOut.addWidget(self._chat_room)
        rightLayout = QtWidgets.QVBoxLayout()
        rightLayout.addWidget(self._chat_box)
        rightLayout.addWidget(self._chat_input)
        mainLayOut.addLayout(rightLayout)
        self.setLayout(mainLayOut)
        self.setWindowTitle(self._title)

    def chat_box(self):
        return self._chat_box

    def chat_room(self):
        return self._chat_room

    def chat_input(self):
        return self._chat_input

    def send_message(self, message: Message):
        print("window.send_message")
        self._chat_box.send_message(message)
        self._chat_room.send_message(message)
        self._client.send_message(message)

    def receive_message(self, message: Message):
        self._chat_box.receive_message(message)
        self._chat_room.receive_message(message)

    def listen_message(self):
        self._client.listen_receive_message(
            process_message=self.receive_message)
