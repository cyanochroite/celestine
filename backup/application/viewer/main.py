from celestine.application.viewer.core import os


def _execute(session, directory):
    (path, file) = os.walk_directory(directory)
    images = []
    for filenames in file:
        (dirpath, name) = filenames
        ext = os.file_extension(name).lower()
        if ext in session.interface.image_format():
            merge = os.join(dirpath, name)
            images.append(merge)
    return images


def _setup(window):
    directory = window.session.attribute.directory
    image = _execute(window.session, directory)
    return image

