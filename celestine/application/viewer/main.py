""""""

import os

from celestine.load.directory import walk_file


def _execute(session, directory):
    """"""
    image_format = session.interface.image_format()

    def file_extension(path):
        (_, ext) = os.path.splitext(path)
        extension = ext.lower()
        return extension in image_format

    file = walk_file(directory)
    image = filter(file_extension, file)
    return list(image)


def _setup(window):
    """"""
    directory = window.session.attribute.directory
    image = _execute(window.session, directory)
    return image
