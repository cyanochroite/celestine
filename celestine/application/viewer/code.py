""""""
from celestine import load
from celestine.data import code
from celestine.typed import (
    LP,
    LS,
    H,
    N,
    P,
    R,
    S,
)


def find_image(hold: H, directory: P) -> LP:
    """"""
    path = directory
    include = hold.window.extension()
    exclude: LS = []
    files = list(load.walk_file(path, include, exclude))
    return files


@code
def setup(hold: H, **star: R) -> N:
    """"""
    window = hold.window.page
    directory = hold.attribute.directory
    find = find_image(hold, directory)
    images = iter(find)

    grid = window.get("grid")
    try:
        for _, item in grid:
            image = next(images)
            item.update(image)
    except StopIteration:
        pass


@code
def see(hold: H, caller: S, **star: R) -> N:
    """"""
    window = hold.window
    source = window.find(caller)
    destination = window.find("photo")
    destination.update(source.path)
