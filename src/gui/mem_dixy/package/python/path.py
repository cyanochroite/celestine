# https://docs.python.org/3/library/os.path.html
import os.path as _path


class path:
    @staticmethod
    def basename(path):
        return _path.basename(path)

    @staticmethod
    def dirname(path):
        return _path.dirname(path)

    @staticmethod
    def join(path, *paths):
        return _path.join(path, *paths)
