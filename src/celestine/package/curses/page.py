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

    def __enter__(self):
        self.frame.clear()
        return super().__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        self.frame.noutrefresh()
        return super().__exit__(exc_type, exc_value, traceback)

    def __init__(self, window):
        self.window = window
        self.item = {}
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
