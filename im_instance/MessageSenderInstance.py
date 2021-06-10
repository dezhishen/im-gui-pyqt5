from abc import abstractmethod
from typing import List
from im_instance.Message import Message
import sys

sys.path.append("../")


class MessageSendInstance(object):
    """
    发送消息
    """
    @abstractmethod
    def send(self, messages: List[Message]):
        pass
