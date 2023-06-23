""""""


from celestine import load
from celestine.typed import (
    N,
    R,
)
from celestine.window.container import (
    Image,
    View,
    Zone,
)

NULL = load.pathway.asset("null.png")
NULL = load.pathway.asset("32.png")


def picture(ring: R, view: View) -> N:
    """"""
    view.image("photo", NULL, mode=Image.FULL)


def main(ring: R, view: View) -> N:
    """"""
    view.text("load", "Load image.", call="setup", window=view)
    with view.zone("grid", row=2, col=4, mode=Zone.GRID) as grid:
        for name, _ in grid:
            grid.image(name, NULL, mode=Image.FILL, call="picture")
