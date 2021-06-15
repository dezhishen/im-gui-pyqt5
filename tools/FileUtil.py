import uuid
from concurrent.futures import ALL_COMPLETED, wait
from mimetypes import guess_extension

import requests

from tools.CacheUtil import CACHE_UTIL
from tools.ThreadPoolUtil import THREAD_POOL


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
    def _download_url(url: str, key: str, file_path: str):
        r = requests.get(url)
        type = guess_extension(
            r.headers['content-type'].partition(';')[0].strip())
        all_file_path = file_path+type
        with open(all_file_path, "wb") as f:
            f.write(r.content)
        CACHE_UTIL.set(key, all_file_path)

    @staticmethod
    def get_storage_from_url(url: str, key: str, dir: str) -> str:
        path = dir+"/"+str(uuid.uuid1())
        t = THREAD_POOL.submit(FileUtil._download_url, url, key, path)
        wait([t], return_when=ALL_COMPLETED)
        return path
