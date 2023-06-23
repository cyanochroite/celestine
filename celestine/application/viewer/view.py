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
    view.new("photo", path=NULL, mode=Image.FULL)


def main(ring: R, view: View) -> N:
    """"""
    view.new("load", text="Load image.", call="setup", window=view)
    with view.zone("grid", row=2, col=4, mode=Zone.GRID) as grid:
        for name, _ in grid:
            grid.new(name, path=NULL, mode=Image.FILL)
            # grid.new(name, path=NULL, mode=Image.FILL, call="picture")
