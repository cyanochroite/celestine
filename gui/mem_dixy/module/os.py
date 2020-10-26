import os


class OS:
    @classmethod
    def working_directory(cls):
        # one = Path.Make(os.path.abspath("."))
        return os.getcwd()

    @classmethod
    def join(cls, path, *paths):
        return os.path.join(path, *paths)

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
                file.append((filename, dirpath))
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
