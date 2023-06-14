""""""
from celestine.load.many import file
from celestine.typed import (
    LS,
    A,
    N,
    R,
    S,
)


def find_image(ring: R, directory: S) -> LS:
    """"""
    path = directory
    include = ring.window.extension()
    exclude = []
    files = list(file(path, include, exclude))
    return files


def setup(*, ring: R, window: A, **star) -> N:
    """"""
    print("cow")
    directory = ring.attribute.directory
    images = find_image(ring, directory)
    grid = window.load("grid")

    items = zip(grid.__iter__(), images)

    for group, image in items:
        (_, item) = group
        item.update(ring=ring, image=image)
