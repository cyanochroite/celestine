from . import package
from .line import Line


class Page():
    def item_get(self, tag):
        return self.item[tag]

    def item_set(self, tag, value):
        self.item[tag] = value
        return value

    def cords_y(self):
        value = self.cord_y
        self.cord_y += 1
        return value

    def __init__(self, window, document):
        self.document = document
        self.window = window
        self.item = {}

        self.frame = window.screen

        self.cord_x = 0
        self.cord_y = 0

    def __enter__(self):
        self.frame.fill((0, 0, 0))
        return self

    def __exit__(self, *_):
        return False

    def line(self, tag):
        return self.item_set(tag, Line(self, tag))
