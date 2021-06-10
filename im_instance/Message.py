from datetime import datetime
from im_instance.User import MessageElement, Receiver, Self, Sender
from typing import List


class Message(object):
    _sender = None
    _elements = None
    _datetime = None
    _receiver = None

    def __init__(self,
                 sender: Sender,
                 receiver: Receiver,
                 elements: List[MessageElement],
                 msg_datetime: datetime = None):
        super().__init__()
        self._sender = sender
        Self._receiver = receiver
        self._elements = elements
        self._datetime = msg_datetime
        if self._datetime is None:
            self._datetime = datetime.now()

    def elements(self):
        return self._elements

    def sender(self):
        return self._sender

    def receiver(self):
        return self._receiver
