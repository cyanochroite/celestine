""""""


from celestine.typed import N
from celestine.window.container import Container as Page

from .main import _setup


def main(page: Page) -> N:
    """"""
    page.call("load", "Load image.", "setup", window=page)
    images = ["D:\\file\\test.jpg"] * 8
    #    images = _setup(page)
    with page.grid("grid", 4) as grid:
        for image in images:
            grid.image("image", None)
