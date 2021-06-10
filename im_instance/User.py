from typing import Dict


class User(object):
    _id = None
    _type = None
    _code = None
    _name = None
    _header_image_url = None
    _alias_name = None
    _meta = {}

    def __init__(self,
                 id: str,
                 type: str,
                 code: str,
                 name: str,
                 alias_name: str = None,
                 header_image_url: str = None,
                 meta: dict = None) -> None:
        super().__init__()
        self._id = id
        self._type = type
        self._code = code
        self._name = name
        self._alias_name = alias_name
        self._meta = meta
        self._header_image_url = header_image_url
        if self._meta is None:
            self._meta = {}

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @property
    def code(self):
        return self._code

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def alias_name(self) -> str:
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        self._alias_name = alias_name

    @property
    def meta(self) -> Dict:
        return self._meta

    def put_meta(self, key, value):
        self._meta[key] = value
        return self

    @property
    def header_image_url(self) -> str:
        return self._header_image_url

    @header_image_url.setter
    def header_image_url(self, header_image_url):
        self._header_image_url = header_image_url

    def get_name_for_show(self):
        """按照顺序 alias_name,name,code,id ,获取第一个非空字段
        """
        if self._alias_name is not None and self._alias_name != "":
            return self._alias_name
        if self._name is not None and self._name != "":
            return self._name
        if self._code is not None and self._code != "":
            return self._code
        return self._id


class Receiver(User):
    """接收人
    """


class Sender(User):
    """发送人
    """


class Self(User):
    """自身信息
    """
