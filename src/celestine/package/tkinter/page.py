from . import package
from .line import Line


class Page():
    def item_get(self, tag):
        return self.item[tag]

    def item_set(self, tag, value):
        self.item[tag] = value
        return value

    def __init__(self, window, document):
        self.window = window
        self.item = {}
        self.frame = package.Frame(
            self.window.root,
            padx=5,
            pady=5,
            bg="skyblue",
        )

    def __enter__(self):
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.index = len(self.window.item)
        self.window.frame_set(self.frame)
        return self

    def __exit__(self, *_):
        return False

    def line(self, tag):
        return self.item_set(tag, Line(self, tag))
