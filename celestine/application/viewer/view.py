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
                    path=r"D:\done\unknown.png",
                    fit=Image.FULL,
                    goto="picture",
                )
