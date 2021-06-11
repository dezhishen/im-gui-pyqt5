from datetime import datetime

from remote.User import Receiver, Self, Sender
from typing import Dict, List


class MessageElement(object):
    """消息列表
    """
    _type = None
    _content = None
    _meta = {}

    def __init__(self, type, content, meta={}):
        super().__init__()
        self._type = type
        self._content = content
        self._meta = meta
        if self._meta is None:
            self._meta = {}

    def type(self) -> str:
        return self._type

    def meta(self) -> Dict:
        return self._meta

    def content(self) -> bytes:
        return self._content

    def put_meta(self, key: str, value):
        self._meta[key] = value
        return self

    def get_meta(self, key: str):
        return self._meta.get(key)


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

    def elements(self) -> List[MessageElement]:
        return self._elements

    def sender(self) -> Sender:
        return self._sender

    def receiver(self) -> Receiver:
        return self._receiver
