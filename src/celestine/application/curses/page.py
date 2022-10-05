from . import curses
from .line import Line

HEIGHT = 24
WIDTH = 80

class Page():
    def clear(self):
        self.frame.clear()

    def noutrefresh(self):
        self.frame.noutrefresh()

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
        self.frame = curses.window(
            1,
            1,
            WIDTH - 1,
            HEIGHT - 2,
        )
        self.cord_x = 0
        self.cord_y = 0

    def __enter__(self):
        # clear
        self.clear()
        return self

    def __exit__(self, *_):
        self.frame.noutrefresh()
        return False

    def line(self, tag):
        return self.item_set(tag, Line(self, tag))
