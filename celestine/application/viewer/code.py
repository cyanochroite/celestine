""""""
from celestine import load
from celestine.typed import (
    LP,
    LS,
    A,
    H,
    N,
    P,
    R,
)


def find_image(hold: H, directory: P) -> LP:
    """"""
    path = directory
    include = hold.window.extension()
    exclude: LS = []
    files = list(load.many_file(path, include, exclude))
    return files


def setup(*, hold: H, window: A, **star: R) -> N:
    """"""
    directory = hold.attribute.directory
    find = find_image(hold, directory)
    images = iter(find)

    grid = window.load("grid")
    try:
        for _, item in grid.item.items():
            image = next(images)
            item.update(image)
    except StopIteration:
        pass
