import shelve
import os


def create_dir_if_not_exists(dir: str):
    if not os.path.exists(dir):
        os.makedirs(dir)


class _CacheUtil:
    _db: shelve.DbfilenameShelf = None

    def __init__(self) -> None:
        create_dir_if_not_exists("./resources/cache")
        self._db = shelve.open("./resources/cache/message.cache")

    def set(self, key: str, value: object):
        self._db[key] = value

    def get(self, key: str) -> object:
        return self._db.get(key)


CACHE_UTIL = _CacheUtil()
