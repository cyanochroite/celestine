""""""
from celestine.load.many import file


def find_image(ring, directory):
    """"""
    path = directory
    include = ring.window.extension()
    exclude = []
    files = list(file(path, include, exclude))
    return files


def setup(*, ring, window, **star):
    """"""
    print("cow")
    directory = ring.attribute.directory
    images = find_image(ring, directory)
    grid = window.load("grid")

    items = zip(grid.__iter__(), images)

    for group, image in items:
        (_, item) = group
        item.update(ring=ring, image=image)
