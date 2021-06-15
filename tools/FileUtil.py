import typing
import uuid
from mimetypes import guess_extension
import requests
from pathlib import Path

from tools.CacheUtil import CACHE_UTIL
from tools.ThreadPoolUtil import THREAD_POOL


class FileUtil:

    def __init__(self):
        pass

    @staticmethod
    def _process_key(key: str) -> str:
        return "file_cache:"+key

    @staticmethod
    def read_qss(style):
        with open(style, "r") as f:
            return f.read()

    @staticmethod
    def put_cache(key: str, path: str, file: bytes):
        with open(path, 'wb') as fd:
            fd.write(file)
        CACHE_UTIL.set(FileUtil._process_key(key), path)

    @staticmethod
    def get_cache_path(key: str) -> str:
        return CACHE_UTIL.get(FileUtil._process_key(key))

    @staticmethod
    def _download_url(
            url: str,
            file_path: str,
            callback: typing.Callable[[str], None] = None
    ):
        r = requests.get(url)
        type = guess_extension(
            r.headers['content-type'].partition(';')[0].strip())
        all_file_path = file_path+type
        with open(all_file_path, "wb") as f:
            f.write(r.content)
        CACHE_UTIL.set(FileUtil._process_key(url), all_file_path)
        if callback is not None:
            callback(all_file_path)

    @staticmethod
    def get_storage_from_url(url: str,
                             dir: str,
                             callback: typing.Callable[[str], None] = None
                             ) -> str:
        # 检查是否存在
        now_path = FileUtil.get_cache_path(url)
        if now_path is not None and now_path != "":
            # 校验文件是否存在
            the_file = Path(now_path)
            if the_file.is_file():
                if callback is not None:
                    callback(now_path)
                return
        path = dir+"/"+str(uuid.uuid1())
        THREAD_POOL.submit(FileUtil._download_url,
                           url,  path, callback)
        # wait([f], return_when=ALL_COMPLETED)
