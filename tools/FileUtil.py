from tools.CacheUtil import CACHE_UTIL


class FileUtil:

    def __init__(self):
        pass

    @staticmethod
    def read_qss(style):
        with open(style, "r") as f:
            return f.read()

    @staticmethod
    def put_cache(key: str, path: str, file: bytes):
        with open(path, 'wb') as fd:
            fd.write(file)
        CACHE_UTIL.set(key, path)

    def get_cache_path(key: str) -> str:
        return CACHE_UTIL.get(key)
