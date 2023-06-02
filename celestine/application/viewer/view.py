""""""


from celestine.typed import N
from celestine.window.container import Container as Page


def main(page: Page) -> N:
    """"""
    page.call("load", "Load image.", "setup", window=page)
    with page.grid("grid", 4, 2) as grid:
    #with page.grid("grid", 4, 2) as grid:
        for key, value in grid:
            grid.image(key, value)
