import curses

WIDTH = 80
HEIGHT = 24


class Cursor():
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.x = 0
        self.y = 0
        self.width = WIDTH
        self.height = HEIGHT

    def move(self):
        self.stdscr.move(self.y, self.x)

    def input(self, key):
        match key:
            case curses.KEY_DOWN:
                self.y += 1
            case curses.KEY_UP:
                self.y -= 1
            case curses.KEY_RIGHT:
                self.x += 1
            case curses.KEY_LEFT:
                self.x -= 1
        self.x %= self.width
        self.y %= self.height


def new_window(column, row, width, height):
    nlines = height
    ncols = width
    begin_y = row
    begin_x = column
    return curses.newwin(nlines, ncols, begin_y, begin_x)


def new_subwindow(window, column, row, width, height):
    nlines = height
    ncols = width
    begin_y = row
    begin_x = column
    return window.subwin(nlines, ncols, begin_y, begin_x)


def draw_menu(stdscr):
    key = 0

    cursor = Cursor(stdscr)

    quote_window = new_window(0, 0, WIDTH, HEIGHT)
    quote_text_window = new_subwindow(quote_window, 2, 3, 17, 14)

    quote_text_window.addstr("Press 'R' to get your first quote!")
    quote_window.box()

    stdscr.noutrefresh()
    quote_window.noutrefresh()
    curses.doupdate()

    while (key != ord('q')):
        stdscr.refresh()

        cursor.input(key)
        cursor.move()

        key = stdscr.getch()


curses.wrapper(draw_menu)
