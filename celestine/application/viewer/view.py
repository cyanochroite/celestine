""""""

from celestine import load
from celestine.data import (
    main,
    scene,
)
from celestine.interface import View
from celestine.typed import N
from celestine.window.container import (
    Image,
    Zone,
)

NULL = load.asset("null.png")


@scene
def picture(view: View) -> N:
    """"""
    view.new("photo", path=NULL, mode=Image.FULL, view="display")


@main
def display(view: View) -> N:
    """"""
    view.new(
        "load",
        text=view.hold.language.VIEWER_MAIN_BUTTON,
        code="setup",
    )
    view.new("me", text="text", code="test")
    with view.zone("grid", row=2, col=4, mode=Zone.GRID) as grid:
        for name, _ in grid:
            # grid.new(name, path=NULL, mode=Image.FILL)
            grid.new(name, path=NULL, mode=Image.FILL, view="picture")
