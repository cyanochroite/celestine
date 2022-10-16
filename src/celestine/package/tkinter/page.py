from celestine.package.master.page import Page as master

from . import package
from .line import Line


class Page(master):
    def line(self, tag):
        return self.item_set(tag, Line(self, tag))

    def __enter__(self):
        self.frame.grid(row=0, column=0, sticky="nsew")
        return super().__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        return super().__exit__(exc_type, exc_value, traceback)

    def __init__(self, window):
        super().__init__()
        self.turn = window.turn
        self.frame = package.Frame(
            window.root,
            padx=5,
            pady=5,
            bg="skyblue",
        )
