from datetime import datetime
from typing import List


class Sender(object):
    _id = None
    _type = None
    _code = None
    _name = None
    _alias_name = None
    _meta = {}

    def __init__(self,
                 id: str,
                 type: str,
                 code: str,
                 name: str,
                 alias_name: str = None,
                 meta: dict = None) -> None:
        super().__init__()
        self._id = id
        self._type = type
        self._code = code
        self._name = name
        self._alias_name = alias_name
        self._meta = meta
        if self._meta is None:
            self._meta = {}

    def id(self):
        return self._id

    def type(self):
        return self._type

    def code(self):
        return self._code

    def name(self):
        return self._name

    def alias_name(self):
        return self._alias_name

    """
    按照顺序 alias_name,name,code,id ,获取第一个非空字段
    """

    def get_name_for_show(self):
        if self.alias_name() is not None and self.alias_name() != "":
            return self.alias_name()
        if self.name() is not None and self.name() != "":
            return self.name()
        if self.code() is not None and self.code() != "":
            return self.code()
        if self.id() is not None and self.id() != "":
            return self.id()

    @property
    def meta(self):
        return self._meta

    def put_meta(self, key, value):
        self._meta[key] = value
        return self


class MessageElement(object):
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

    def type(self):
        return self._type

    def meta(self):
        return self._meta

    def content(self):
        return self._content

    def put_meta(self, key: str, value):
        self._meta[key] = value
        return self


class Message(object):
    _sender = None
    _elements = None
    _datetime = None

    def __init__(self,
                 sender: Sender,
                 elements: List[MessageElement],
                 msg_datetime: datetime = None):
        super().__init__()
        self._sender = sender
        self._elements = elements
        self._datetime = msg_datetime
        if self._datetime is None:
            self._datetime = datetime.now()

    def elements(self):
        return self._elements

    def sender(self):
        return self._sender
