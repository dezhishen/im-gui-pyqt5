from tools.ThreadPoolUtil import THREAD_POOL
from tools.CacheUtil import CACHE_UTIL
import requests
import uuid


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

    @staticmethod
    def get_cache_path(key: str) -> str:
        return CACHE_UTIL.get(key)

    @staticmethod
    def _download_url(url: str, file_path: str):
        r = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(r.content)
        CACHE_UTIL.set("file_cache:"+url, file_path)

    @staticmethod
    def get_storage_from_url(url: str, dir: str) -> str:
        path = dir+"/"+uuid.uuid1()
        THREAD_POOL.submit(FileUtil._download_url, url, path)
        return path
