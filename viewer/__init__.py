""""""

import os

import celestine
from celestine import (
    bank,
    language,
    load,
    walk,
)
from celestine.interface import Element
from celestine.session.argument import Optional
from celestine.session.session import SuperSession
from celestine.typed import (
    DA,
    LP,
    LS,
    B,
    N,
    P,
    R,
    S,
    ignore,
)
from celestine.window.container import (
    Image,
    Zone,
)
from celestine.window.decorator import (
    call,
    view,
)


class Session(SuperSession):
    """"""

    output: S

    @classmethod
    def dictionary(cls) -> DA:
        """"""
        ignore(cls)
        return super().dictionary() | {
            "output": Optional(
                os.getcwd(),
                language.VIEWER_SESSION_DIRECTORY,
            ),
        }


def find_image(directory: P) -> LP:
    """"""
    path = directory
    include = bank.window.extension()
    exclude: LS = []
    files = list(walk.file(path, include, exclude))
    return files


def main():
    """"""
    celestine.init(__package__)
    celestine.main("viewer:run", __package__)


@view
def run(element: Element) -> N:
    """"""
    element.button(
        "load",
        "setup",
        text=language.VIEWER_MAIN_BUTTON,
    )
    name = "grid"
    with element.zone(name, row=row, col=col, mode=Zone.GRID) as grid:
        for range_y in range(row):
            for range_x in range(col):
                key = f"{name}_{range_x}-{range_y}"
                grid.element(
                    key,
                    action="see",
                    fit=Image.FULL,
                    goto="picture",
                )


@view
def picture(element: Element) -> N:
    """"""
    element.element("photo", fit=Image.FILL, goto="run")


@call
def see(caller: S, **star: R) -> B:
    """"""
    ignore(star)
    window = bank.window
    source = window.find(caller)
    destination = window.find("photo")
    destination.reimage(source.path)
    return True


@call
def setup(**star: R) -> B:
    """"""
    ignore(star)
    window = bank.window.page
    directory = bank.directory
    find = find_image(directory)
    images = iter(find)

    grid = window.get("grid")
    try:
        for value in grid.values():
            image = next(images)
            value.reimage(image)
    except StopIteration:
        pass

    return True


ignore(Session, main, picture, run, see, setup)
