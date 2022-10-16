from celestine.package.master.page import Page as master

from . import package
from .line import Line

from .rectangle import Col


class Page(master, Col):
    def line(self, tag):
        return self.item_set(
            tag,
            Line(
                self,
                tag,
                self.spawn(),
            ),
        )

    def __enter__(self):
        super().__enter__()
        self.window.fill((0, 0, 0))
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        package.display.flip()
        return False

    def __init__(self, window, rectangle, **kwargs):
        super().__init__(
            cord_x_min=rectangle.cord_x_min,
            cord_y_min=rectangle.cord_y_min,
            cord_x_max=rectangle.cord_x_max,
            cord_y_max=rectangle.cord_y_max,
            **kwargs,
        )
        self.turn = window.turn
        self.window = window.book
        self.font = window.font
