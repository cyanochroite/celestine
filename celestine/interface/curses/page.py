from celestine.window.page import Page as master

from .package import package
from .line import Line


class Page(master):
    def cords_y(self):
        value = self.cord_y
        self.cord_y += 1
        return value

    def line(self, tag):
        return self.item_set(tag, Line(self, tag))

    def __init__(self, window, **kwargs):
        self.window = window
        self.height = 24
        self.width = 80
        self.cord_x = 0
        self.cord_y = 0
        super().__init__(
            session=window.session,
            frame=package.window(
                1,
                1,
                self.width - 1,
                self.height - 2,
            ),
            **kwargs,
        )
