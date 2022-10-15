from celestine.application.master.window import Window as master


import curses
from celestine.application.window import Window as Window_

from celestine.application.window import Frame as Frame_

from .widget import Widget

from .page import Page

from . import curses


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


class Window(master):

    def __init__(self, session):
        super().__init__(session)
        self.window = 0
        self.now_frame = None
        self.session_window = []
        self.document = []

    def turn(self, page):
        self.now_frame = Page(self, self.document[page])
        self.now_frame.document(self.now_frame)
        self.stdscr.noutrefresh()
        self.background.noutrefresh()
        self.now_frame.noutrefresh()
        curses.doupdate()

    def image_load(self, file):
        return file

    def curses_string(self, frame, tag, string, cord_x, cord_y):
        window = self.frame_get(frame)
        thing = String(cord_x, cord_y, string)
        thing.draw(window)
        self.item_set(frame, tag, thing)


    def file_dialog(self, frame, tag, _):
        item = Label(
            self.frame_get(frame),
            "File dialog thing.",
        )
        self.item_set(frame, tag, item)
        return item

    def image(self, frame, tag, _image):
        item = Label(
            self.frame_get(frame),
            _image,
        )
        self.item_set(frame, tag, item)
        return item


    def page(self, document):
        self.document.append(document)
        page = Page(self, document)
        self.session_window.append(page)
        self.now_frame = page
        return page

    def __enter__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(1)
        curses.start_color()

        # start

        self.cursor = Cursor(self.session, self.stdscr)

        self.background = curses.window(0, 0, WIDTH, HEIGHT)
        self.background.box()

        header1 = curses.subwindow(self.background, 0, 0, WIDTH, 1)
        header1.addstr(self.session.language.APPLICATION_TITLE)

        header2 = curses.subwindow(self.background, 0, HEIGHT - 1, WIDTH, 1)
        header2.addstr(self.session.language.CURSES_EXIT)

        self.stdscr.noutrefresh()
        self.background.noutrefresh()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        while True:
            match self.stdscr.getch():
                case 258 | 259 | 260 | 261 as key:
                    self.cursor.input(key)
                    self.cursor.move()
                case curses.KEY_Q:
                    break
                case curses.KEY_SPACE as key:
                    for key, thing in self.now_frame.item.items():
                        if thing.select(self.cursor.cord_x - 1, self.cursor.cord_y - 1):
                            if thing.type == "button":
                                self.turn(thing.action)

        self.stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()

        return False

