"""Package celestine."""
import curses


HEIGHT = 24
WIDTH = 80


class Cursor():
    def __init__(self, session, stdscr):
        self.session = session
        self.stdscr = stdscr
        self.x = 0
        self.y = 0
        self.width = WIDTH
        self.height = HEIGHT

    def move(self):
        self.stdscr.move(self.y, self.x)

    def input(self, key):
        (x, y) = self.session.python.curses_cursor_input_match(
            key,
            curses,
            self.x,
            self.y
        )
        self.x = x % self.width
        self.y = y % self.height


def file_dialog(tag, bind):
    _add_string(quote_text_window, "File dialog thing.")
    item[tag] = tag


def image(tag, image):
    _add_string(quote_text_window, image)
    item[tag] = tag


def image_load(file):
    return file


def label(tag, text):
    _add_string(quote_text_window, "This is a label.")
    item[tag] = tag


def _new_window(column, row, width, height):
    nlines = height
    ncols = width
    begin_y = row
    begin_x = column
    return curses.newwin(nlines, ncols, begin_y, begin_x)


def _new_subwindow(window, column, row, width, height):
    nlines = height
    ncols = width
    begin_y = row
    begin_x = column
    return window.subwin(nlines, ncols, begin_y, begin_x)


def _add_string(window, string):
    global line

    y = line
    x = 0
    line += 1
    window.addstr(y, x, string)


def main(**kwargs):
    """def main"""
    global session
    session = kwargs["session"]
    window = kwargs["window"]

    global item
    item = {}

    global line
    line = 0

    global quote_window
    quote_window = None

    global quote_text_window
    quote_text_window = None

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    try:
        key = 0

        cursor = Cursor(session, stdscr)

        quote_window = _new_window(0, 0, WIDTH, HEIGHT)
        quote_window.box()

        header1 = _new_subwindow(quote_window, 0, 0, WIDTH, 1)
        header1.addstr(session.language.APPLICATION_TITLE)

        header2 = _new_subwindow(quote_window, 0, HEIGHT - 1, WIDTH, 1)
        header2.addstr(session.language.CURSES_EXIT)

        quote_text_window = _new_subwindow(quote_window, 1, 1, WIDTH - 1, HEIGHT - 2)

        window.setup()
        window.view()

        stdscr.noutrefresh()
        quote_window.noutrefresh()
        curses.doupdate()

        while key != ord('q'):
            stdscr.refresh()

            cursor.input(key)
            cursor.move()

            key = stdscr.getch()

    finally:
        stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()
