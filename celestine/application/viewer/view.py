
""""""

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


@scene
def picture(view: View) -> N:
    """"""
    view.element("photo", fit=Image.FULL, goto="display")


@main
def display(view: View) -> N:
    """"""
    view.button(
        "load",
        "setup",
        text=view.hold.language.VIEWER_MAIN_BUTTON,
    )
    with view.zone("grid", row=2, col=4, mode=Zone.GRID) as grid:
        for name, _ in grid:
            # grid.image(name, path=r"D:\done\unknown.png")
            grid.element(
                name,
                action="see",
                path=r"D:\done\unknown.png",
                fit=Image.FILL,
                goto="picture",
            )
