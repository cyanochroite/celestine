from celestine.package.master.window import Window as master

from . import package
from .page import Page


class Window(master):
    def page(self, document):
        self.document.append(document)
        page = Page(self, document)
        self.session_window.append(page)
        self.now_frame = page
        return page

    def turn(self, page):
        self.now_frame = Page(self, self.document[page])
        self.now_frame.document(self.now_frame)
        self.stdscr.noutrefresh()
        self.background.noutrefresh()
        self.now_frame.noutrefresh()
        package.doupdate()

    def __enter__(self):
        self.stdscr = package.initscr()
        package.noecho()
        package.cbreak()
        self.stdscr.keypad(1)
        package.start_color()

        # start

        self.background = package.window(0, 0, self.width, self.height)
        self.background.box()

        header1 = package.subwindow(self.background, 0, 0, self.width, 1)
        header1.addstr(self.session.language.APPLICATION_TITLE)

        header2 = package.subwindow(
            self.background, 0, self.height - 1, self.width, 1)
        header2.addstr(self.session.language.CURSES_EXIT)

        self.stdscr.noutrefresh()
        self.background.noutrefresh()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        while True:
            match self.stdscr.getch():
                case 258 | 259 | 260 | 261 as key:
                    match key:
                        case package.KEY_UP:
                            self.cord_y -= 1
                        case package.KEY_DOWN:
                            self.cord_y += 1
                        case package.KEY_LEFT:
                            self.cord_x -= 1
                        case package.KEY_RIGHT:
                            self.cord_x += 1

                    self.cord_x %= self.width
                    self.cord_y %= self.height
                    self.stdscr.move(self.cord_y, self.cord_x)
                case package.KEY_Q:
                    break
                case package.KEY_SPACE as key:
                    for key, thing in self.now_frame.item.items():
                        if thing.select(self.cord_x - 1, self.cord_y - 1):
                            if thing.type == "button":
                                self.turn(thing.action)

        self.stdscr.keypad(0)
        package.echo()
        package.nocbreak()
        package.endwin()

        return False

    def __init__(self, session):
        super().__init__(session)
        self.cord_x = 0
        self.cord_y = 0
        self.height = 24
        self.width = 80

        self.window = 0
        self.now_frame = None
        self.session_window = []
        self.document = []
