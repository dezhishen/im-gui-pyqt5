from tools.FileUtil import FileUtil

url = "https://avatars.githubusercontent.com/u/26274059?v=4"


def print_file_path(path):
    print(path)
    print(FileUtil.get_cache_path(url))


if __name__ == "__main__":
    FileUtil.get_storage_from_url(
        url=url,
        dir="./resources/images",
        callback=print_file_path)
