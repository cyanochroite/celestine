from celestine.package.master.page import Page as master

from . import package
from .line import Line


class Page(master):
    def line(self, tag):
        return self.item_set(tag, Line(self, tag))

    def __init__(self, window, tag, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.tag = tag
        self.frame = package.window(tag=tag)
