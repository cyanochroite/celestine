""""""

from celestine import (
    bank,
    load,
)
from celestine.data import call
from celestine.typed import (
    LP,
    LS,
    B,
    P,
    R,
    S,
)


def find_image(directory: P) -> LP:
    """"""
    path = directory
    include = bank.window.extension()
    exclude: LS = []
    files = list(load.walk_file(path, include, exclude))
    return files


@call
def setup(**star: R) -> B:
    """"""
    window = bank.window.page
    directory = bank.directory
    find = find_image(directory)
    images = iter(find)

    grid = window.get("grid")
    try:
        for _, item in grid:
            image = next(images)
            item.update(image)
    except StopIteration:
        pass

    return True


@call
def see(caller: S, **star: R) -> B:
    """"""
    window = bank.window
    source = window.find(caller)
    destination = window.find("photo")
    destination.update(source.path)
    return True
