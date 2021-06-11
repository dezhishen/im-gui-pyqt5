from abc import abstractmethod
from remote.Message import Message


class Client(object):
    """客户端
    """

    def __init__(self) -> None:
        """客户端

        Args:
            message_send_instance (MessageSendInstance): [消息发送工具]
        """
        super().__init__()

    def start_listen_receive_message(self):
        self.listen_receive_message()

    @abstractmethod
    def send_message(self, message: Message):
        """发送消息

        Args:
            message (Message): 消息对象
        """
        pass

    @abstractmethod
    def listen_receive_message(self):
        """监听方法

        Args:
            callback (typing.Callable[[Message], ]): 回调函数,方法内部应该回调该方法,处理消息的接收
        """
        pass
