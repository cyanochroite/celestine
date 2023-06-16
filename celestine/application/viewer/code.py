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
    images = iter(images)

    grid = window.load("grid")
    for _, line in grid.item.items():
        for _, item in line.item.items():
            image = next(images)
            item.update(ring, image)
