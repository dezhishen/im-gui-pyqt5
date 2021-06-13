from datetime import datetime

from remote.Entity import Receiver,  Sender
from typing import Dict, List


class MessageElement(object):
    """消息列表
    """
    _id: str = None
    _type: str = None
    _content: bytes = None
    _db_content: str = None
    _meta: Dict = {}

    def __init__(self,
                 id: str,
                 type: str,
                 content: bytes,
                 db_content: str = None,
                 meta: Dict[str, object] = None):
        super().__init__()
        self._id = id
        self._type = type
        self._content = content
        self._db_content = db_content
        self._meta = meta
        if self._meta is None:
            self._meta = {}

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str):
        self._id = id

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

    @property
    def db_content(self) -> str:
        return self._db_content

    @db_content.setter
    def db_content(self, db_content: str):
        self._db_content = db_content

    def get_db_content(self) -> str:
        if self.db_content is not None:
            return self.db_content
        return str(self.content)

    @property
    def meta(self) -> Dict[str, Dict]:
        return self._meta

    def get_meta(self, key: str) -> object:
        return self._meta.get(key)


class Message(object):
    _id = None
    _sender = None
    _elements = None
    _message_date = None
    _receiver = None

    def __init__(self,
                 id: str,
                 sender: Sender,
                 receiver: Receiver,
                 elements: List[MessageElement],
                 messsage_date: datetime = None):
        super().__init__()
        self._id = id
        self._sender = sender
        self._receiver = receiver
        self._elements = elements
        self._message_date = messsage_date
        if self._message_date is None:
            self._message_date = datetime.now()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: str):
        self._id = id

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

    @property
    def message_date(self) -> datetime:
        return self._message_date

    @message_date.setter
    def message_date(self, message_date: datetime):
        self._message_date = message_date
