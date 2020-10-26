import os


class OS:
    @classmethod
    def working_directory(cls):
        # one = Path.Make(os.path.abspath("."))
        return os.getcwd()

    @classmethod
    def join_path(cls, one, two):
        return os.path.join(one, two)

    def remove(cls, path):
        if os.path.isfile(path):
            os.remove(path)

    @classmethod
    def rename(cls, source, destination):
        if not os.path.isfile(destination):
            os.rename(source, destination)

    @classmethod
    def filenames(cls, path):
        file = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            for name in filenames:
                file.append(os.path.join(dirpath, name))
        return file

    def _image_save(image, path):
        if os.path.isfile(path):
            os.remove(path)
        with open(path, "wb") as file:
            image.save(file, "PNG", optimize=True)

    def walk_directory(top='.'):
        path = []
        file = []
        for (dirpath, dirnames, filenames) in os.walk(top):
            for dirname in dirnames:
                path.append(os.path.join(dirpath, dirname))
            for filename in filenames:
                file.append(File(filename, dirpath))
        return (path, file)

    def makedirs(paths):
        for path in paths:
            os.mkdir(path)

    def chdir(path, call, *args):
        cwd = os.getcwd()
        os.chdir(path)
        ring = call(*args)
        os.chdir(cwd)
        return ring


class Path:
    def __init__(self, path=None, file=None):
        self.path = OS.working_directory()
        if path is not None:
            self.change_directory(path)
        self.file = file

    def change_directory(self, path):
        self.path = OS.join_path(self.path, path)

    def get_path(self):
        return self.path

    def get_file(self):
        return OS.join_path(self.path, self.file)


class File:
    def __init__(self, name=None, path=None):
        self.name = name
        self.path = path

    def full(self):
        return OS.join_path(self.path, self.name)

