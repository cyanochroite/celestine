from celestine.package.master.page import Page as master

from . import package
from .line import Line


class Page(master):
    def line(self, tag):
        return self.item_set(tag, Line(self, tag))

    def __enter__(self):
        super().__enter__()
        self.frame.__enter__()
        package.configure_item(self.tag, show=False)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        self.frame.__exit__(exc_type, exc_value, traceback)
        return False

    def __init__(self, window, tag, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.tag = tag
        self.frame = package.window(tag=tag)
