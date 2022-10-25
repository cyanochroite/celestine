from celestine.package.master.page import Page as master

from . import package
from .line import Line


class Page(master):
    def cords_y(self):
        value = self.cord_y
        self.cord_y += 1
        return value

    def line(self, tag):
        return self.item_set(tag, Line(self, tag))

    def __init__(self, window, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.height = 24
        self.width = 80
        self.frame = package.window(
            1,
            1,
            self.width - 1,
            self.height - 2,
        )
        self.cord_x = 0
        self.cord_y = 0
