import os


def join(path, *paths):
    return os.path.join(path, *paths)


def file_extension(path):
    (root, ext) = os.path.splitext(path)
    return ext


def walk_directory(top='.'):
    path = []
    file = []
    for (dirpath, dirnames, filenames) in os.walk(top):
        for dirname in dirnames:
            path.append((dirpath, dirname))
        for filename in filenames:
            file.append((dirpath, filename))
    return (path, file)


def _execute(session, directory):
    (path, file) = walk_directory(directory)
    images = []
    for filenames in file:
        (dirpath, name) = filenames
        ext = file_extension(name).lower()
        if ext in session.interface.image_format():
            merge = join(dirpath, name)
            images.append(merge)
    return images


def _setup(window):
    directory = window.session.attribute.directory
    image = _execute(window.session, directory)
    return image

