""""""
from celestine import load
from celestine.data import code
from celestine.typed import (
    LP,
    LS,
    A,
    H,
    N,
    P,
)


def find_image(hold: H, directory: P) -> LP:
    """"""
    path = directory
    include = hold.window.extension()
    exclude: LS = []
    files = list(load.walk_file(path, include, exclude))
    return files


@code
def setup(hold: H) -> N:
    """"""
    window = hold.window.page
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
