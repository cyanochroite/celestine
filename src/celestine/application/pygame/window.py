"""Package celestine."""
import pygame

from celestine.application.window import Window as Window_


from .page import Page

from . import package


from .rectangle import Rectangle


class Window(Window_):

    def __init__(self, session):
        super().__init__(session)
        self.window = 0
        self.now_frame = None
        self.session_window = []
        self.document = []

        pygame.init()
        self.font = pygame.font.SysFont("Arial", 64)

    def turn(self, index):
        rectangle = Rectangle(0, 0, 640, 480, 0, 0)
        with Page(self, None, rectangle) as page:
            self.now_frame = page
            self.document[index](page)


    def page(self, document):
        self.document.append(document)
        rectangle = Rectangle(0, 0, 640, 480, 0, 0)
        page = Page(self, document, rectangle)
        self.session_window.append(page)
        self.now_frame = page
        return page

    def select(self, cord_x, cord_y):
        for self.key, thing in self.now_frame.item.items():
            select = thing.select(cord_x, cord_y)
            if select:
                return select
        return self.now_frame




    def __enter__(self):
        width = 640
        height = 480
        self.screen = pygame.display.set_mode((width, height), 8, 0)
        self.font = pygame.font.SysFont('Arial', 40)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        cord_x = 0
        cord_y = 0
        while True:
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        return False
                    case pygame.MOUSEBUTTONDOWN:
                        cord_x, cord_y = pygame.mouse.get_pos()
                        self.now_frame.select(cord_x, cord_y)

