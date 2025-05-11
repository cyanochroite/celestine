""""""

import os

from celestine import (
    bank,
    language,
    load,
)
from celestine.interface import View
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
    draw,
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
    files = list(load.walk_file(path, include, exclude))
    return files


@draw
def main(view: View) -> N:
    """"""
    view.button(
        "load",
        "setup",
        text=language.VIEWER_MAIN_BUTTON,
    )
    name = "grid"
    row = 2
    col = 4
    with view.zone(name, row=row, col=col, mode=Zone.GRID) as grid:
        for range_y in range(row):
            for range_x in range(col):
                key = f"{name}_{range_x}-{range_y}"
                grid.element(
                    key,
                    action="see",
                    fit=Image.FULL,
                    goto="picture",
                )


@draw
def picture(view: View) -> N:
    """"""
    view.element("photo", fit=Image.FILL, goto="main")


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


ignore(Session, main, picture, see, setup)


class Self:
    """"""