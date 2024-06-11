""""""

from celestine import language
from celestine.data import draw
from celestine.interface import View
from celestine.typed import N
from celestine.window.container import (
    Image,
    Zone,
)


@draw
def picture(view: View) -> N:
    """"""
    view.element("photo", fit=Image.FILL, goto="main")


@draw
def main(view: View) -> N:
    """"""
    view.button(
        "load",
        "setup",
        text=language.VIEWER_MAIN_BUTTON,
    )
    with view.zone("grid", row=2, col=4, mode=Zone.GRID) as grid:
        for key in grid.keys():
            # grid.image(name, path=r"D:\done\unknown.png")
            grid.element(
                key,
                action="see",
                path=r"D:\done\unknown.png",
                fit=Image.FILL,
                goto="picture",
            )
