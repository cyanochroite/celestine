from . import dearpygui
from .line import Line


class Page():
    def item_get(self, tag):
        return self.item[tag]

    def item_set(self, tag, value):
        self.item[tag] = value
        return value

    def __init__(self, window, document, tag):
        self.window = window
        self.item = {}
        self.tag = tag
        self.frame = dearpygui.window(tag=tag)

    def __enter__(self):
        self.frame.__enter__()
        dearpygui.configure_item(self.tag, show=False)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.frame.__exit__(exc_type, exc_value, traceback)
        return False

    def line(self, tag):
        return self.item_set(tag, Line(self, tag))
