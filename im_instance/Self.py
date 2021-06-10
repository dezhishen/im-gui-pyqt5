class Self(object):
    _id = None
    _name = None
    _header_image_url = None
    _meta = {}

    def __init__(self, id: str) -> None:
        super().__init__()
        self._id = id

    @property
    def id(self):
        return self._uid

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def header_image_url(self):
        return self._header_image_url

    @header_image_url.setter
    def header_image_url(self, header_image_url):
        self._header_image_url = header_image_url

    @property
    def meta(self):
        return self._meta

    def get_meta(self, key: str):
        return self._meta.get(key)

    def put_meta(self, key: str, value):
        self._meta[key] = value
