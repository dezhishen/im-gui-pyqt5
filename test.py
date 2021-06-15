from tools.FileUtil import FileUtil
import uuid

if __name__ == "__main__":
    FileUtil.get_storage_from_url(
        url="https://avatars.githubusercontent.com/u/26274059?v=4",
        key=str(uuid.uuid1()),
        dir="./resources/images")
