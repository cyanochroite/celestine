""""""


from celestine.session.session import Session
from celestine.typed import N
from celestine.window.container import Container as View


def main(ring: Session, view: View) -> N:
    """"""
    view.call("load", "Load image.", "setup", window=view)
    with view.grid("grid", 4, 2) as grid:
        for key, value in grid:
            grid.image(key, value)  # , mode="one")
