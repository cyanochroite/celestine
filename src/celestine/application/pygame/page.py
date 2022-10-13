import pygame
from . import package
from .line import Line

from .rectangle import Col
from .rectangle import Collection


class Page(Col, Collection):
    def action(self):
        pass

    def line(self, tag):
        return self.item_set(
            tag,
            Line(
                self,
                tag,
                self.spawn(),
            ),
        )

    def select(self, cord_x, cord_y):
        if self.inside(cord_x, cord_y):
            self.action()
            for child in self.children():
                child.select(cord_x, cord_y)

    def __enter__(self):
        self.window.fill((0, 0, 0))
        return self

    def __exit__(self, *_):
        pygame.display.flip()
        return False

    def __init__(self, window, document, rectangle):
        super().__init__(
            cord_x_min=rectangle.cord_x_min,
            cord_y_min=rectangle.cord_y_min,
            cord_x_max=rectangle.cord_x_max,
            cord_y_max=rectangle.cord_y_max,
        )
        self.book = window
        self.document = document
        self.window = window.screen
        self.font = window.font
        self.item = {}
