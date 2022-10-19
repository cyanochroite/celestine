from celestine.package.master.page import Page as master

from . import package
from .line import Line


class Page(master):
    def line(self, tag):
        return self.item_set(tag, Line(self, tag))

    def __enter__(self):
        super().__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        return False

    def __init__(self, window, **kwargs):
        super().__init__(**kwargs)
        self.turn = window.turn
        self.frame = package.Frame(
            window.root,
            padx=5,
            pady=5,
            bg="skyblue",
        )
