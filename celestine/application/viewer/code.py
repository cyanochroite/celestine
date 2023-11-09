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


def find_image(hold: R, directory: P) -> LP:
    """"""
    path = directory
    include = hold.window.extension()
    exclude: LS = []
    files = list(file(path, include, exclude))
    return files


def setup(*, hold: R, window: A, **star) -> N:
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
