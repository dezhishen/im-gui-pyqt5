from typing import Dict


class Entity(object):
    _id = None
    # _type = None
    _code = None
    _name = None
    _header_image_url = None
    _alias_name = None
    _meta = {}

    def __init__(self,
                 id: str,
                 #  type: str,
                 code: str,
                 name: str,
                 alias_name: str = None,
                 header_image_url: str = None,
                 meta: dict = None) -> None:
        super().__init__()
        self._id = id
        # self._type = type
        self._code = code
        self._name = name
        self._alias_name = alias_name
        self._meta = meta
        self._header_image_url = header_image_url
        if self._meta is None:
            self._meta = {}

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str):
        self._id = id

    @property
    def code(self) -> str:
        return self._code

    @code.setter
    def code(self, code: str):
        self._code = code

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
    def meta(self) -> Dict[str, object]:
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


class Receiver(Entity):
    """接收人
    """
    _type = None

    def __init__(self,
                 id: str,
                 type: str,
                 code: str,
                 name: str,
                 alias_name: str,
                 header_image_url: str = None,
                 meta: dict = None) -> None:
        super().__init__(id, code, name, alias_name=alias_name,
                         header_image_url=header_image_url, meta=meta)
        self._type = type

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, type: str):
        self._type = type


class Sender(Entity):
    """发送人
    """
    _type = None

    def __init__(self,
                 id: str,
                 type: str,
                 code: str,
                 name: str,
                 alias_name: str,
                 header_image_url: str = None,
                 meta: dict = None) -> None:
        super().__init__(id, code, name, alias_name=alias_name,
                         header_image_url=header_image_url, meta=meta)
        self._type = type

    @property
    def type(self) -> str:
        return self._type


class Self(Entity):
    """自身信息
    """
