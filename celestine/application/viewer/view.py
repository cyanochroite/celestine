""""""


from celestine import load
from celestine.session.session import Session
from celestine.typed import N
from celestine.window.container import Container as View

NULL = load.pathway.asset("null.png")
NULL = load.pathway.asset("32.png")


def main(ring: Session, view: View) -> N:
    """"""
    view.call("load", "Load image.", "setup", window=view)
    with view.grid("grid", row=2, col=4) as grid:
        for name, _ in grid:
            grid.image(name, NULL, mode="A")
