import pygame
from . import package
from .line import Line

from .rectangle import Rectangle


class Page(Rectangle):
    def item_get(self, tag):
        return self.item[tag]

    def item_set(self, tag, value):
        self.item[tag] = value
        return value

    def __init__(self, window, document):
        super().__init__(0, 0, 640, 480)  # load from window
        self.document = document
        self.window = window.screen
        self.font = window.font
        self.item = {}

    def __enter__(self):
        self.window.fill((0, 0, 0))
        return self

    def __exit__(self, *_):
        pygame.display.flip()
        return False

    def line(self, tag):
        return self.item_set(tag, Line(self, tag))

    def action(self):
        pass
