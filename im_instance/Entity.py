class Sender(object):
    __id = None
    __type = None
    __code = None
    __name = None
    __meta = {}

    def __init__(self,
                 id: str,
                 type: str,
                 code: str,
                 name: str,
                 meta: dict = None) -> None:
        super().__init__()
        self.__id = id
        self.__type = type
        self.__code = code
        self.__name = name
        self.__meta = meta

    @property
    def id(self):
        return self.__id

    @property
    def type(self):
        return self.__type

    @property
    def code(self):
        return self.__code

    @property
    def name(self):
        return self.__name

    @property
    def meta(self):
        return self.__meta


class Message(object):
    __type = None
    __content = None
    __sender = None

    def __init__(self, type: str, content: bytes, sender: Sender):
        super().__init__()
        self.__type = type
        self.__content = content
        self.__sender = sender

    @property
    def type(self):
        return self.__type

    @property
    def content(self):
        return self.__content

    @property
    def sender(self):
        return self.__sender
