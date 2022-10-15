from celestine.application.master.window import Window as master


from . import package
from .page import Page


import pygame
from .rectangle import Rectangle


class Window(master):
    def page(self, document):
        self.document.append(document)
        rectangle = Rectangle(0, 0, 640, 480, 0, 0)
        page = Page(self, document, rectangle)
        self.session_window.append(page)
        self.now_frame = page
        return page

    def turn(self, index):
        rectangle = Rectangle(0, 0, 640, 480, 0, 0)
        with Page(self, None, rectangle) as page:
            self.now_frame = page
            self.document[index](page)

    def __enter__(self):
        width = 640
        height = 480
        self.screen = pygame.display.set_mode((width, height), 8, 0)
        self.font = pygame.font.SysFont('Arial', 40)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        while True:
            match pygame.event.wait().type:
                case pygame.QUIT:
                    break
                case pygame.MOUSEBUTTONDOWN:
                    self.now_frame.select(*pygame.mouse.get_pos())

        return False

    def __init__(self, session):
        super().__init__(session)
        self.window = 0
        self.now_frame = None
        self.session_window = []
        self.document = []

        pygame.init()
        self.font = pygame.font.SysFont("Arial", 64)
