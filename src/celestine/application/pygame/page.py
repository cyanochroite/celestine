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
            cord_x=rectangle.cord_x,
            cord_y=rectangle.cord_y,
            width=rectangle.width,
            height=rectangle.height,
        )
        self.document = document
        self.window = window.screen
        self.font = window.font
        self.item = {}
