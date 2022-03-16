import os


class OS:
    @staticmethod
    def working_directory():
        return os.getcwd()

    @staticmethod
    def join(path, *paths):
        return os.path.join(path, *paths)

    @staticmethod
    def remove(path):
        if os.path.isfile(path):
            os.remove(path)

    @staticmethod
    def rename(source, destination):
        if not os.path.isfile(destination):
            os.rename(source, destination)

    @staticmethod
    def filenames(path):
        file = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            for name in filenames:
                file.append(os.path.join(dirpath, name))
        return file

    @staticmethod
    def walk_directory(top='.'):
        path = []
        file = []
        for (dirpath, dirnames, filenames) in os.walk(top):
            for dirname in dirnames:
                path.append(os.path.join(dirpath, dirname))
            for filename in filenames:
                file.append((filename, dirpath))
        return (path, file)

    @staticmethod
    def makedirs(paths):
        for path in paths:
            os.mkdir(path)

    @staticmethod
    def chdir(path, call, *args):
        cwd = os.getcwd()
        os.chdir(path)
        ring = call(*args)
        os.chdir(cwd)
        return ring
