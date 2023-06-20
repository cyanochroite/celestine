""""""


from celestine.session.session import Session
from celestine.typed import N
from celestine.window.container import Container as View

from celestine import load

NULL = load.pathway.asset("null.png")
NULL = load.pathway.asset("32.png")


def main(ring: Session, view: View) -> N:
    """"""
    view.call("load", "Load image.", "setup", window=view)
    with view.grid("grid", 4, 2) as grid:
        for name, _ in grid:
            grid.image(name, None)  # , mode="one")


def main(ring: Session, view: View) -> N:
    """"""
    view.call("load", "Load image.", "setup", window=view)
    with view.drop("grid") as grid:
        for range_y in range(2):
            with grid.span(f"line-{range_y}") as line:
                for range_x in range(4):
                    name = f"grid_{range_x}-{range_y}"
                    line.image(name, NULL)  # , mode="one")
