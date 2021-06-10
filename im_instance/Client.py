from abc import abstractmethod
from im_instance.MessageSenderInstance import MessageSendInstance
from im_instance.Message import Message


class Client(object):
    """客户端
    """

    # 连接持有对象
    _instant = None
    _message_send_instance = None

    def __init__(self, message_send_instance: MessageSendInstance) -> None:
        """客户端

        Args:
            message_send_instance (MessageSendInstance): [消息发送工具]
        """
        super().__init__()
        self._message_send_instance = message_send_instance

    def send_message(self, message: Message):
        """发送消息

        Args:
            message (Message): 消息对象
        """
        self._message_send_instance.send(message)

    def message_send_instance(self) -> MessageSendInstance:
        return self._message_send_instance

    @abstractmethod
    def start_receive_message(self):
        pass
