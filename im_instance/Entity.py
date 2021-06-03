from datetime import datetime
from typing import List


class Sender(object):
    __id = None
    __type = None
    __code = None
    __name = None
    __alias_name = None
    __meta = {}

    def __init__(self,
                 id: str,
                 type: str,
                 code: str,
                 name: str,
                 alias_name: str = None,
                 meta: dict = None) -> None:
        super().__init__()
        self.__id = id
        self.__type = type
        self.__code = code
        self.__name = name
        self.__alias_name = alias_name
        self.__meta = meta
        if self.__meta is None:
            self.__meta = {}

    def id(self):
        return self.__id

    def type(self):
        return self.__type

    def code(self):
        return self.__code

    def name(self):
        return self.__name

    def alias_name(self):
        return self.__alias_name

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
        return self.__meta

    def put_meta(self, key, value):
        self.__meta[key] = value
        return self


class MessageElement(object):
    __type = None
    __content = None
    __meta = {}

    def __init__(self, type, content, meta={}):
        super().__init__()
        self.__type = type
        self.__content = content
        self.__meta = meta
        if self.__meta is None:
            self.__meta = {}

    def type(self):
        return self.__type

    def meta(self):
        return self.__meta

    def content(self):
        return self.__content

    def put_meta(self, key: str, value):
        self.__meta[key] = value
        return self


class Message(object):
    __sender = None
    __elements = None
    __datetime = None

    def __init__(self,
                 sender: Sender,
                 elements: List[MessageElement],
                 msg_datetime: datetime = None):
        super().__init__()
        self.__sender = sender
        self.__elements = elements
        self.__datetime = msg_datetime
        if self.__datetime is None:
            self.__datetime = datetime.now()

    def elements(self):
        return self.__elements

    def sender(self):
        return self.__sender
