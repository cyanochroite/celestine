""""""
from celestine.load.many import file
from celestine.typed import (
    LP,
    LS,
    A,
    N,
    P,
    R,
)


def find_image(ring: R, directory: P) -> LP:
    """"""
    path = directory
    include = ring.window.extension()
    exclude: LS = []
    files = list(file(path, include, exclude))
    return files


def setup(*, ring: R, window: A, **star) -> N:
    """"""
    directory = ring.attribute.directory
    find = find_image(ring, directory)
    images = iter(find)

    grid = window.load("grid")
    for _, item in grid.item.items():
        image = next(images)
        item.update(ring, image)
