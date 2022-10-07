"""Package celestine."""
import pygame

from celestine.application.window import Window as Window_


from .page import Page

from . import package




class Window(Window_):

    def __init__(self, session):
        super().__init__(session)
        self.window = 0
        self.now_frame = None
        self.session_window = []
        self.document = []

    def turn(self, page):
        self.now_frame = Page(self, self.document[page])
        self.now_frame.document(self.now_frame)

    def page(self, document):
        self.document.append(document)
        page = Page(self, document)
        self.session_window.append(page)
        self.now_frame = page
        return page

    def __enter__(self):
        pygame.init()
        self.fps = 60
        self.fpsClock = pygame.time.Clock()
        width = 640
        height = 480
        self.screen = pygame.display.set_mode((width, height), 8, 0)
        self.font = pygame.font.SysFont('Arial', 40)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)

        playing = True
        while playing:
            cord_x = 0
            cord_y = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cord_x, cord_y = pygame.mouse.get_pos()

            for self.key, thing in self.now_frame.item.items():
                if thing.select(cord_x, cord_y):
                    if thing.type == "button":
                        self.turn(thing.action)

            pygame.display.flip()
            self.fpsClock.tick(self.fps)

        return False
