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


class Window():
    def __init__(self, session):
        self.session = session
        self.item = {}
        self.line = 0
        self.quote_window = None
        self.header = None
        self.quote_text_window = None


    def file_dialog(self, tag, bind):
        self._add_string(self.quote_text_window, "File dialog thing.")
        self.item[tag] = tag

    def image(self, tag, image):
        self._add_string(self.quote_text_window, image)
        self.item[tag] = tag

    def image_load(self, file):
        return file

    def label(self, tag, text):
        self._add_string(self.quote_text_window, "This is a label.")
        self.item[tag] = tag

    def _new_window(self, column, row, width, height):
        nlines = height
        ncols = width
        begin_y = row
        begin_x = column
        return curses.newwin(nlines, ncols, begin_y, begin_x)

    def _new_subwindow(self, window, column, row, width, height):
        nlines = height
        ncols = width
        begin_y = row
        begin_x = column
        return window.subwin(nlines, ncols, begin_y, begin_x)

    def _add_string(self, window, string):
        y = self.line
        x = 0
        self.line += 1
        window.addstr(y, x, string)

    def run(self, app):
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        try:
            key = 0

            cursor = Cursor(self.session, stdscr)

            self.quote_window = self._new_window(0, 0, WIDTH, HEIGHT)
            self.quote_window.box()

            self.header = self._new_subwindow(self.quote_window, 0, 0, WIDTH, 1)
            self.header.addstr(self.session.language.APPLICATION_TITLE)
            self.header.addstr(" - " + self.session.language.CURSES_EXIT)
            
            self.quote_text_window = self._new_subwindow(
                self.quote_window, 1, 1, WIDTH-1, HEIGHT-1)

            app.setup(self)
            app.view(self)

            stdscr.noutrefresh()
            self.quote_window.noutrefresh()
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

