from abc import abstractmethod
from im_instance.Entity import Message
import sys

sys.path.append("../")


class MessageSenderInstance(object):
    """
    发送消息
    """
    @abstractmethod
    def send(self, messages: list[Message]):
        pass
