""""""


from celestine.typed import N
from celestine.window.container import Container as Page


def main(page: Page) -> N:
    """"""
    page.call("load", "Load image.", "setup", window=page)
    images = ["D:\\file\\test.jpg"] * 8
    with page.grid("grid", 4) as grid:
        for image in images:
            grid.image("image", None)
