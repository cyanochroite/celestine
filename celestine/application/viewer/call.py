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


def setup(window):
    """"""
    print("cow")
    directory = window.session.attribute.directory
    images = _execute(window.session, directory)
    grid = window.load("grid")

    items = zip(grid.items(), images)

    for (item, image) in items:
        item.image = image

    grid.refresh()
