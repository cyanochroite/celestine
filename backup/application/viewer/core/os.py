# <pep8-80 compliant>
import os


def file_extension(path):
    (root, ext) = os.path.splitext(path)
    return ext


def working_directory():
    return os.getcwd()


def join(path, *paths):
    return os.path.join(path, *paths)


def remove(path):
    if os.path.isfile(path):
        os.remove(path)


def rename(source, destination):
    if not os.path.isfile(destination):
        os.rename(source, destination)


def filenames(path):
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
            #path.append(os.path.join(dirpath, dirname))
            path.append((dirpath, dirname))
        for filename in filenames:
            #file.append(os.path.join(dirpath, filename))
            file.append((dirpath, filename))
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
