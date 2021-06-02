from abc import abstractmethod
from lib.im.im_instance.Entity import Message


class MessageSenderInstance(object):
    """
    发送消息
    """
    @abstractmethod
    def send(self, message: Message):
        pass
