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
    def new_window(self, column, row, width, height):
        nlines = height
        ncols = width
        begin_y = row
        begin_x = column
        return curses.newwin(nlines, ncols, begin_y, begin_x)

    def new_subwindow(self, window, column, row, width, height):
        nlines = height
        ncols = width
        begin_y = row
        begin_x = column
        return window.subwin(nlines, ncols, begin_y, begin_x)

    def draw_menu(self, stdscr):
        key = 0

        cursor = Cursor(self.session, stdscr)

        quote_window = self.new_window(0, 0, WIDTH, HEIGHT)
        quote_text_window = self.new_subwindow(quote_window, 2, 3, 17, 14)

        quote_text_window.addstr("Press 'R' to get your first quote!")
        quote_window.box()

        stdscr.noutrefresh()
        quote_window.noutrefresh()
        curses.doupdate()

        while key != ord('q'):
            stdscr.refresh()

            cursor.input(key)
            cursor.move()

            key = stdscr.getch()

    def __init__(self, session):
        self.session = session

    def run(self, app):
        # app.setup(self)
        # app.view(self)
        curses.wrapper(self.draw_menu)
