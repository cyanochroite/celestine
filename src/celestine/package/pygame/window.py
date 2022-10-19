from celestine.package.master.window import Window as master

from celestine.package.master.collection import Rectangle

from . import package
from .page import Page

import pygame


class Window(master):
    def page(self, document):
        index = len(self.item)
        self.item_set(index, document)
        rectangle = Rectangle(0, 0, 640, 480, 0, 0)
        page = Page(self, rectangle)
        self.frame = page
        return page

    def turn(self, page):
        rectangle = Rectangle(0, 0, 640, 480, 0, 0)
        with Page(self, rectangle) as page2:
            self.frame = page2
            self.item_get(page)(page2)
        package.display.flip()


    def __enter__(self):
        super().__enter__()
        pygame.init()
        self.book = pygame.display.set_mode((self.width, self.height), 8, 0)
        self.font = pygame.font.SysFont('Arial', 40)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        while True:
            match pygame.event.wait().type:
                case pygame.QUIT:
                    break
                case pygame.MOUSEBUTTONDOWN:
                    self.frame.select(*pygame.mouse.get_pos())
        return False

    def __init__(self, session, **kwargs):
        super().__init__(session, **kwargs)
        self.book = None
        self.frame = None
        self.width = 640
        self.height = 480
