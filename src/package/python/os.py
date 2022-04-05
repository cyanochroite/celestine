# https://docs.python.org/3/library/os.html
import os as _os


class os:
    @staticmethod
    def working_directory():
        return _os.getcwd()

    @staticmethod
    def join(path, *paths):
        return _os.path.join(path, *paths)

    @staticmethod
    def remove(path):
        if _os.path.isfile(path):
            _os.remove(path)

    @staticmethod
    def rename(source, destination):
        if not _os.path.isfile(destination):
            _os.rename(source, destination)

    @staticmethod
    def filenames(path):
        file = []
        for (dirpath, dirnames, filenames) in _os.walk(path):
            for name in filenames:
                file.append(_os.path.join(dirpath, name))
        return file

    @staticmethod
    def walk_directory(top='.'):
        path = []
        file = []
        for (dirpath, dirnames, filenames) in _os.walk(top):
            for dirname in dirnames:
                path.append(_os.path.join(dirpath, dirname))
            for filename in filenames:
                file.append((filename, dirpath))
        return (path, file)

    @staticmethod
    def makedirs(paths):
        for path in paths:
            _os.mkdir(path)

    @staticmethod
    def chdir(path, call, *args):
        cwd = _os.getcwd()
        _os.chdir(path)
        ring = call(*args)
        _os.chdir(cwd)
        return ring
