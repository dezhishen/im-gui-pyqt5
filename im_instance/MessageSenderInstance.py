from abc import abstractmethod
from typing import List
from im_instance.Entity import Message
import sys

sys.path.append("../")


class MessageSenderInstance(object):
    """
    发送消息
    """
    @abstractmethod
    def send(self, messages: List[Message]):
        pass
