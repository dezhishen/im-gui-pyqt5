from datetime import datetime

from remote.Entity import Receiver,  Sender
from typing import Dict, List


class MessageElement(object):
    """消息列表
    """
    _type = None
    _content = None
    _meta = {}

    def __init__(self,
                 type: str,
                 content: bytes,
                 meta: Dict[str, object] = None):
        super().__init__()
        self._type = type
        self._content = content
        self._meta = meta
        if self._meta is None:
            self._meta = {}

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, type: str):
        self._type = type

    @property
    def content(self) -> bytes:
        return self._content

    @content.setter
    def content(self, content: str):
        self._content = content

    def put_meta(self, key: str, value):
        self._meta[key] = value
        return self

    @property
    def meta(self) -> Dict[str, Dict]:
        return self._meta

    def get_meta(self, key: str) -> object:
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
        self._receiver = receiver
        self._elements = elements
        self._datetime = msg_datetime
        if self._datetime is None:
            self._datetime = datetime.now()

    @property
    def elements(self) -> List[MessageElement]:
        return self._elements

    @elements.setter
    def elements(self, elements: List[MessageElement]):
        self._elements = elements

    @property
    def sender(self) -> Sender:
        return self._sender

    @sender.setter
    def sender(self, sender: Sender):
        self._sender = sender

    @property
    def receiver(self) -> Receiver:
        return self._receiver

    @receiver.setter
    def receiver(self, receiver: Sender):
        self._receiver = receiver
