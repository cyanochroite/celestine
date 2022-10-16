from celestine.package.master.page import Page as master

from . import package
from .line import Line


class Page(master):
    def line(self, tag):
        return self.item_set(tag, Line(self, tag))

    def __init__(self, window, document, tag):
        self.window = window
        self.item = {}
        self.tag = tag
        self.frame = package.window(tag=tag)

    def __enter__(self):
        self.frame.__enter__()
        package.configure_item(self.tag, show=False)
        return super().__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        self.frame.__exit__(exc_type, exc_value, traceback)
        return super().__exit__(exc_type, exc_value, traceback)
