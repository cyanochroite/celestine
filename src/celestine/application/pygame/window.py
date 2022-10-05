"""Package celestine."""
import pygame

from celestine.application.window import Window as Window_
from celestine.application.window import Frame as Frame_

from .widget import Widget

from .page import Page

from . import package


HEIGHT = 24
WIDTH = 80

class Cursor():
    def __init__(self, session, stdscr):
        self.session = session
        self.stdscr = stdscr
        self.cord_x = 0
        self.cord_y = 0
        self.width = WIDTH
        self.height = HEIGHT

    def move(self):
        self.stdscr.move(self.cord_y, self.cord_x)

    def input(self, key):
        (cord_x, cord_y) = self.session.python.curses_cursor_input_match(
            key,
            curses,
            self.cord_x,
            self.cord_y
        )
        self.cord_x = cord_x % self.width
        self.cord_y = cord_y % self.height





class String(Widget):
    def __init__(self, x, y, text):
        super().__init__(x, y, len(text), 1)
        self.text = text
        self.type = "string"

    def draw(self, window):
        window.addstr(self.cord_y, self.cord_x, self.text)


class Window(Window_):

    def __init__(self, session):
        super().__init__(session)
        self.window = 0
        self.now_frame = None
        self.session_window = []
        self.document = []


    def turn(self, page):
        pass

    def page(self, document):
        self.document.append(document)
        page = Page(self, document)
        self.session_window.append(page)
        self.now_frame = page
        return page

    def __enter__(self):
        pygame.init()
        window = pygame.display.set_mode([600, 600])
        window.fill((0, 0, 0))

        pygame.draw.line(window, (255, 255, 255), (200, 20), (200, 580), 5)
        pygame.draw.line(window, (255, 255, 255), (400, 20), (400, 580), 5)
        pygame.draw.line(window, (255, 255, 255), (20, 200), (580, 200), 5)
        pygame.draw.line(window, (255, 255, 255), (20, 400), (580, 400), 5)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

            pygame.display.flip()

        return False

